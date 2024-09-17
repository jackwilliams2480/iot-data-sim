# iot-data-sim
Allow for easy connection to AWS IoT Core, Azure IoT Hub, or various other cloud capabilities to simulate and publish telemetry data 

## certs
For proper functionality, create and populate a `certs` folder inside the directory of the relevant capability. For example:
```python
iot-data-sim/
|-- lib/
|   |-- mqtt/
|   |   |-- __init__.py
|   |   |-- mqtt_connection.py
|   |   |-- certs/
|   |   |   |-- mosquitto.org.crt
|   |   |   |-- client.crt
|   |   |   |-- client.key
| ...
|-- main.py
```
