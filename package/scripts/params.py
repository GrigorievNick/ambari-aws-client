from resource_management.libraries.script.script import Script

# server configurations
config = Script.get_config()

user = config['configurations']['aws-client-env']['app_user']
group = config['configurations']['aws-client-env']['user_group']
data_dir = config['configurations']['aws-client-env']['data_dir']
aws_conf_dir = config['configurations']['aws-client-env']['aws_conf_dir']
aws_config_custom_properties = dict(config['configurations']['aws-config'])
aws_credentials_custom_properties = dict(config['configurations']['aws-credentials'])

download_url = config['configurations']['aws-client-env']['download_url']
# metrics
host_name = config['hostname'].lower()
service_name = config['serviceName']