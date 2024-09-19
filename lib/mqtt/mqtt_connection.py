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

class MQTTConnection:
    def __init__(self):
        # Load the configuration file
        with open('config.yaml', 'r') as file:
            config = yaml.safe_load(file)
        # Access AWS and Azure configurations
        mqtt_config = config['mqtt']
        
        self.broker = mqtt_config['broker']
        self.port = mqtt_config['port']
        self.username = mqtt_config['auth']['username']
        self.password = mqtt_config['auth']['password']
        self.client = paho.Client(paho.CallbackAPIVersion.VERSION2)
        self.client.username_pw_set(mqtt_config['auth']['username'], mqtt_config['auth']['password'])
        self.mqtt_init()

    def on_message(self, client,userdata,msg):
        msg_payload = msg.payload.decode()

        print(msg_payload)
        sanatized = re.findall(r'[0-9]+.[0-9]+', msg_payload)
    
    def on_connect_fail(self, msg):
        print("Could not connect to MQTT Broker at " + self.broker + ":" + self.port);

    def on_connect(self, client, userdata, flags, rc):
        print("Python Client connected over web sockets with result: " + str(rc));
        
        # subscribe to all sensors 
        subscription1 = "qsi_sensor"
        self.client.subscribe(subscription1);     
        print("Subscribed to: " + subscription1);
    

    def publish(self, msg):
        ret = self.client.publish("sensors", json.dumps(msg))
        if ret.rc != 0:
            logging.info("Failed to publish message: %s", ret)
            return ret
        else:
            logging.info("Published msg: %s", msg)
            logging.info("Return Code: %s", ret)
            return ret
        
    def mqtt_init(self):
        abspath = os.path.abspath(__file__)
        dname = os.path.dirname(abspath)
        os.chdir(dname)
        
        try:
            logging.info("Connecting to MQTT Broker at %s : %s" , self.broker , self.port)
            self.client.on_message = self.on_message; # assign function to callback
            self.client.on_connect = self.on_connect;
            self.client.on_connect_fail = self.on_connect_fail;
            
            self.client.tls_set(ca_certs='certs/mosquitto.org.crt', certfile='certs/client.crt', keyfile='certs/client.key', tls_version=ssl.PROTOCOL_TLSv1_2)
            self.client.connect(self.broker,self.port);    # establish connection
            self.client.loop_forever();    # start loop to process received messages
            return 0
        except Exception as e:
            logging.info("Failed to connect to MQTT Broker: %s", e)
            return -1