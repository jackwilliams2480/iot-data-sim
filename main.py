import sys
import os
from pathlib import Path
import sys
import time
import logging

# Create and configure logger
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

sys.path.append(os.path.join(os.path.dirname(__file__), '..')) 

from lib.mqtt import mqtt_connection
from lib.data import simulate

if __name__ == "__main__":
    logging.info("Starting simulation...")
    
    client = mqtt_connection.mqtt_init()
    try:
        while(True):
            ret = mqtt_connection.publish(client, simulate.json_builder(include_temperature=True, include_humidity=True))
            time.sleep(5)
    except KeyboardInterrupt:
        print("Terminating...")