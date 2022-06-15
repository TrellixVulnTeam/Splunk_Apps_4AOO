#
# SPDX-FileCopyrightText: 2021 Splunk, Inc. <sales@splunk.com>
# SPDX-License-Identifier: LicenseRef-Splunk-8-2021
#
#

import base64
from subprocess import PIPE, Popen
from traceback import format_exc

import java_const
import splunk_ta_jmx_logger_helper as log_helper
from splunk_ta_jmx_utility import ibm_java_args_generator
from splunktaucclib.rest_handler.endpoint.validator import Validator

PROCESS_CONNECTION_TYPE = ["pidCommand", "pidFile", "pid"]
PROTOCOL_CONNECTION_TYPE = [
    "soap",
    "soapssl",
    "hessian",
    "hessianssl",
    "burlap",
    "burlapssl",
    "IBMsoap",
]
PROTOCOL_FIELDS = ["account_name", "account_password"]
URL_FIELDS = ["jmx_url", "account_name", "account_password"]
STUBSOURCE_FIELD_RELATIONS = {
    "ior": ["encodedStub"],
    "stub": ["encodedStub"],
    "jndi": ["host", "jmxport", "lookupPath"],
}
ALL_REQUIRED_FIELDS = [
    "pidCommand",
    "pid",
    "pidFile",
    "jmx_url",
    "host",
    "jmxport",
    "stubSource",
    "encodedStub",
]
PYTHON_JAVA_PARAM_DICT = {
    "jmx_url": "jmxServiceURL",
    "stubSource": "stubSource",
    "account_name": "jmxuser",
    "account_password": "jmxpass",
    "description": "jvmDescription",
}

_LOGGER = log_helper.setup_logging(log_name="ta_jmx_rh_server_field_validation")


class RequiredFieldValidation(Validator):
    """
    Validate required fields
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_connection_type_fields(self, data):
        """
        Returns a List containing two arrays one containing fields to be displayed
        and other with fields to be hidden depended on Connection Type dropdown
        :param data: Dict containing field-value
        :return: List
        """
        shown_fields = []
        selected_connection_type = data.get("protocol")
        if selected_connection_type:
            if selected_connection_type in PROCESS_CONNECTION_TYPE:
                shown_fields.append(selected_connection_type)
            elif (
                selected_connection_type == "rmi" or selected_connection_type == "iiop"
            ):
                shown_fields += PROTOCOL_FIELDS
                shown_fields.append("stubSource")
            elif selected_connection_type == "url":
                shown_fields += URL_FIELDS
            elif selected_connection_type in PROTOCOL_CONNECTION_TYPE:
                shown_fields += PROTOCOL_FIELDS

        return shown_fields

    def get_stubsource_fields(self, data):
        """
        Returns a List containing two arrays one containing fields to be displayed
        and other with fields to be hidden depended on Stub source dropdown
        :param data: Dict containing field-value
        :return: List
        """
        shown_fields = []
        selected_stubsource = data.get("stubSource")
        if selected_stubsource in STUBSOURCE_FIELD_RELATIONS:
            shown_fields += STUBSOURCE_FIELD_RELATIONS[selected_stubsource]
        return shown_fields

    def validate_required_fields(self, msg, fields, data):
        """
        Validates values of fields are not empty. Provides message in UI as well as in log file.
        :param fields: List of field
        :param msg: Error message string
        :param data: Dict containing field-value
        :return: None
        """
        for field in fields:
            if not data.get(field):
                self.put_msg(msg.format(field), high_priority=True)
                _LOGGER.error(msg.format(field))
                return False
        return True

    def validate(self, value, data):
        """
        This method validates all the server fields and returns True on success else False
        :param value: value of the field for which validation is called
        :param data: Contains dictionary of all parameters of the server configuration
        :return: bool
        """
        all_fields = self.get_connection_type_fields(data) + self.get_stubsource_fields(
            data
        )
        required_fields = [
            field for field in all_fields if field in ALL_REQUIRED_FIELDS
        ]
        msg = "{} field is required."
        if not self.validate_required_fields(msg, required_fields, data):
            return False

        if data.get("account_name") and not data.get("account_password"):
            self.put_msg(msg.format("account_password"), high_priority=True)
            _LOGGER.error(msg.format("account_password"))
            return False

        if not data.get("account_name") and data.get("account_password"):
            self.put_msg(msg.format("account_name"), high_priority=True)
            _LOGGER.error(msg.format("account_name"))
            return False

        if not self.validate_server_configuration(data):
            return False

        # Remove server_name field after server is validated
        data.pop("server_name", None)
        return True

    @staticmethod
    def get_key_value_format(data):
        """
        This method takes dictionary and returns a string of following format
        'key=value\n
         key1=value1\n
         .............
         keyn=valuen\n'
        Addtional to that it also encodes 'password' field's value if present
        :param data: dict
        :return: string
        """
        input_parameters = ""
        param_value = "{}={}\n"
        for key, value in list(data.items()):
            if not value:
                continue
            # Encode password field
            if key == "account_password":
                value = base64.b64encode(value.encode("utf-8")).decode()
            key = PYTHON_JAVA_PARAM_DICT.get(key, key)
            input_parameters += param_value.format(key, value)
        return input_parameters

    def validate_server_configuration(self, data):
        """
        Because Splunk can't directly invoke Java , we use this python wrapper script that
        simply proxys through to the Java program.

        This method logs error and success message depending on the type of exit code received
        from Java program. Depending on that exit code it returns boolean value
        :param data: dict
        :return: bool
        """

        input_parameters = self.get_key_value_format(data)
        try:
            if data.get("protocol") == "IBMsoap":
                # If IBMsoap protocol is used while connection to jmx server, update java arguments by adding connection properties files
                ibm_was_server_validation_args = ibm_java_args_generator(
                    java_const.IBM_WAS_JAVA_SERVER_VALIDATION_ARGS,
                    data.get("server_name"),
                    _LOGGER,
                )
                if ibm_was_server_validation_args:
                    process = Popen(  # nosemgrep false-positive : The value ibm_was_server_validation_args is a static value which comes from the java_const.py file. It doesn't take any external/user inputs.
                        ibm_was_server_validation_args, stdin=PIPE
                    )
                else:
                    msg = "Failed to connect with the JMX server. Verify the provided properties files are at expected location."
                    self.put_msg(msg, high_priority=True)
                    _LOGGER.error(msg)
                    return False
            else:
                process = Popen(  # nosemgrep false-positive : The value JAVA_SERVER_VALIDATION_ARGS is a static value which comes from the java_const.py file. It doesn't take any external/user inputs.
                    java_const.JAVA_SERVER_VALIDATION_ARGS, stdin=PIPE
                )

            process.communicate(input=input_parameters.encode("utf-8"))
            process.wait()

        except:
            msg = "Failed to connect with JMX Server."
            self.put_msg(msg, high_priority=True)
            _LOGGER.error("{} Reason: {}".format(msg, format_exc()))
            return False

        else:
            if process.returncode == 2:
                msg = "Failed to connect with the JMX server. Review the values of the fields on this page and try again."
                self.put_msg(msg, high_priority=True)
                _LOGGER.error(msg)
                return False
            elif process.returncode == 1:
                msg = "Invalid parameter found in connection URL. Verify the provided connection configurations."
                self.put_msg(msg, high_priority=True)
                _LOGGER.error(msg)
                return False
            _LOGGER.info("Successfully established connection with JMX server.")
            return True
