i18n_register({plural:function(a){return a==1?0:1},catalog:{}});require.config({paths:{batch_create_view:"../app/website_monitoring/js/views/BatchInputCreateView"}});require(["jquery","underscore","splunkjs/mvc","batch_create_view","splunkjs/mvc/simplexml/ready!"],function(d,c,e,a){var b=new a({el:d("#batch-create-inputs")});b.render()});