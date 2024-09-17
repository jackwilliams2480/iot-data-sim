import paho.mqtt.client as paho
import re
import random 
import time
import datetime
import json
import yaml
import ssl
import os
import sys
import logging

# Create and configure logger
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

sys.path.append(os.path.join(os.path.dirname(__file__), '..')) 
from lib.data import simulate

# Load the configuration file
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Access AWS and Azure configurations
mqtt_config = config['mqtt']

# IPADDRESS = socket.gethostbyname('mqtt')
broker=mqtt_config['broker']
port=mqtt_config['port']

# Optional arguments depending on nessesary security
username = mqtt_config['auth']['username']
password = mqtt_config['auth']['password']

def on_message(client,userdata,msg):
    msg_payload = msg.payload.decode()
    # print("Received->Topic: " + msg.topic + " Message: " + msg_payload)

    print(msg_payload)
    
    sanatized = re.findall(r'[0-9]+.[0-9]+', msg_payload)
    # p = influxdb_client.Point("my_measurement").field("temperature", float(sanatized[0]))
    # write_api.write(bucket=bucket, org=org, record=p)
    
    # p = influxdb_client.Point("my_measurement").field("pressure", float(sanatized[1]))
    # write_api.write(bucket=bucket, org=org, record=p)
    
    # p = influxdb_client.Point("my_measurement").field("humidity", float(sanatized[2]))
    # write_api.write(bucket=bucket, org=org, record=p)
    #print('Parsed message payload')
    # comma separated
    # payload_data_values  = msg_payload.split(",")    
    # for val in payload_data_values:
    #    print(val)

def on_connect_fail(msg):
     print("Could not connect to MQTT Broker at " + broker + ":" + port);

def on_connect(client, userdata, flags, rc):
    print("Python Client connected over web sockets with result: " + str(rc));
    
    # subscribe to all sensors 
    subscription1 = "qsi_sensor"
    client.subscribe(subscription1);     
    print("Subscribed to: " + subscription1);
 

def publish(client, msg):
    ret = client.publish("sensors", json.dumps(msg))
    logging.info("Published msg: %s", msg)
    logging.info("Published return: %s", ret)
    return ret
    
def mqtt_init():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    
    try:
        client= paho.Client(paho.CallbackAPIVersion.VERSION2)
        client.on_message = on_message; # assign function to callback
        client.on_connect = on_connect;
        client.on_connect_fail = on_connect_fail;
        #client.username_pw_set(mqtt_config['auth']['username'], mqtt_config['auth']['password'])
        
        client.tls_set(ca_certs='certs/mosquitto.org.crt', certfile='certs/client.crt', keyfile='certs/client.key', tls_version=ssl.PROTOCOL_TLSv1_2)
        client.connect(broker,port);    # establish connection
        return client
    except: 
        client.disconnect()
        print("All done! bye!")
