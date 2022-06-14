# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Remediate.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import PostgresType_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Remediate.proto',
  package='',
  serialized_pb='\n\x0fRemediate.proto\x1a\x12PostgresType.proto\"\xd6\x02\n\tRemediate\x12\x11\n\ttimeStamp\x18\x01 \x02(\x03\x12#\n\x07\x63ommand\x18\x02 \x02(\x0e\x32\x12.Remediate.Command\x12)\n\nobjectType\x18\x03 \x02(\x0e\x32\x15.Remediate.ObjectType\x12\x12\n\nobjectName\x18\x04 \x02(\t\x12\x1d\n\x15remediationIdentifier\x18\x05 \x02(\x04\x12\x0e\n\x06siteId\x18\x06 \x01(\t\"\"\n\x07\x43ommand\x12\n\n\x06\x45NABLE\x10\x00\x12\x0b\n\x07\x44ISABLE\x10\x01\"\x7f\n\nObjectType\x12\x10\n\x0cTYPE_SERVICE\x10\x01\x12\x0c\n\x08TYPE_BHO\x10\x02\x12\x12\n\x0eTYPE_AUTOSTART\x10\x03\x12\x14\n\x10TYPE_STARTUPFILE\x10\x04\x12\x10\n\x0cTYPE_ACTIVEX\x10\x05\x12\x15\n\x11TYPE_OFFICEPLUGIN\x10\x06\x42\x36\n\"com.ziften.server.protocol.messageB\x10RemediateMessage')



_REMEDIATE_COMMAND = _descriptor.EnumDescriptor(
  name='Command',
  full_name='Remediate.Command',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ENABLE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISABLE', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=219,
  serialized_end=253,
)

_REMEDIATE_OBJECTTYPE = _descriptor.EnumDescriptor(
  name='ObjectType',
  full_name='Remediate.ObjectType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TYPE_SERVICE', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_BHO', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_AUTOSTART', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_STARTUPFILE', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_ACTIVEX', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_OFFICEPLUGIN', index=5, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=255,
  serialized_end=382,
)


_REMEDIATE = _descriptor.Descriptor(
  name='Remediate',
  full_name='Remediate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timeStamp', full_name='Remediate.timeStamp', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='command', full_name='Remediate.command', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='objectType', full_name='Remediate.objectType', index=2,
      number=3, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='objectName', full_name='Remediate.objectName', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='remediationIdentifier', full_name='Remediate.remediationIdentifier', index=4,
      number=5, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='siteId', full_name='Remediate.siteId', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REMEDIATE_COMMAND,
    _REMEDIATE_OBJECTTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=40,
  serialized_end=382,
)

_REMEDIATE.fields_by_name['command'].enum_type = _REMEDIATE_COMMAND
_REMEDIATE.fields_by_name['objectType'].enum_type = _REMEDIATE_OBJECTTYPE
_REMEDIATE_COMMAND.containing_type = _REMEDIATE;
_REMEDIATE_OBJECTTYPE.containing_type = _REMEDIATE;
DESCRIPTOR.message_types_by_name['Remediate'] = _REMEDIATE

class Remediate(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REMEDIATE

  # @@protoc_insertion_point(class_scope:Remediate)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\"com.ziften.server.protocol.messageB\020RemediateMessage')
# @@protoc_insertion_point(module_scope)