import json
import pdb
import os
import requests
import yaml
from awscrt import io, mqtt
from awsiot import mqtt_connection_builder

# Load the configuration file
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Access AWS and Azure configurations
aws_config = config['aws']['iot_core']
azure_config = config['azure']['iot_hub']

# AWS IoT Core configurations
endpoint = aws_config['endpoint']
root_ca_path = aws_config['root_ca_path']
private_key_path = aws_config['private_key_path']
certificate_path = aws_config['certificate_path']
client_id = aws_config['client_id']

# IoT Core topic
topic = aws_config['topic']

# data file path
data_file_path = r'test.json'

file_name = os.path.basename(data_file_path)

# Initialize the AWS IoT Core connection
event_loop_group = io.EventLoopGroup()
host_resolver = io.DefaultHostResolver(event_loop_group)
client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)

# Establish an MQTT connection
mqtt_connection = mqtt_connection_builder.mtls_from_path(
    endpoint=endpoint,
    cert_filepath=certificate_path,
    pri_key_filepath=private_key_path,
    client_bootstrap=client_bootstrap,
    ca_filepath=root_ca_path,
    on_connection_interrupted=None,
    on_connection_resumed=None,
    client_id=client_id,
    clean_session=False,
    keep_alive_secs=6
)


# Callback when the message is received
def on_message_received(topic, payload, dup, qos, retain, **kwargs):

    message = json.loads(payload)

    if (message.get('type') == 'request'):
        return

    print(message)
    presigned_url = message.get('presigned_url')

    if presigned_url != '':
        print(data_file_path)  # testing purposes
        # pdb.set_trace()
        with open(data_file_path, 'rb') as data_file:
            data = data_file.read()
        response = requests.put(url=presigned_url, data=data)
        if response.status_code == 200:
            print('File uploaded successfully')
        else:
            print('Failed to upload the data. Status code:', response.status_code)
    else:
        print('Failed to get the pre-signed URL from the server.')

    # Disconnect from AWS IoT Core
    mqtt_connection.disconnect()

def init_awsiot():

    # Connect to AWS IoT Core
    connect_future = mqtt_connection.connect()

    # Subscribe to the topic
    subscribe_future, _ = mqtt_connection.subscribe(
        topic=topic,
        qos=mqtt.QoS.AT_LEAST_ONCE,
        callback=on_message_received
    )

    # Send an MQTT message to request the pre-signed URL
    mqtt_message = {
        'file_name': file_name,
        'type': 'request'
    }
    mqtt_connection.publish(
        topic=topic,
        payload=json.dumps(mqtt_message),
        qos=mqtt.QoS.AT_LEAST_ONCE
    )


    # Wait for the message to be received and processed
    mqtt_connection.disconnect()

