import sys
import os
from pathlib import Path
import sys
import time
import logging
import argparse

# Create and configure logger
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# handle command line arguments
parser = argparse.ArgumentParser(description='IoT Sim')
parser.add_argument("--protocol", type=str, help="protocol options: mqtt, http, coap", default="mqtt")
args = parser.parse_args()


sys.path.append(os.path.join(os.path.dirname(__file__), '..')) 

from lib.mqtt import mqtt_connection
from lib.data import simulate

if __name__ == "__main__":
    logging.info("Starting simulation...")
    
    if args.protocol == "mqtt":
        client = mqtt_connection.MQTTConnection()
        
        try:
            while(True):
                print("Publishing data...")
                ret = client.publish(simulate.json_builder(include_temperature=True, include_humidity=True))
                time.sleep(5)
        except KeyboardInterrupt:
            print("Terminating...")