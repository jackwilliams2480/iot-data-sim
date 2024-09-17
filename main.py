import sys
import os
from pathlib import Path
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..')) 

from lib.mqtt import mqtt_connection
from lib.data import simulate

if __name__ == "__main__":
    client = mqtt_connection.mqtt_init()
    ret = mqtt_connection.publish(client, simulate.json_builder(include_temperature=True, include_humidity=True))