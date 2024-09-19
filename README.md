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

## config
You will have to create a yaml file which can hold the configurations for which ever option you choose to use. The file should be formatted as such:
```yaml
# config.yaml

aws:
  iot_core:
    endpoint: "account-specific-prefix.iot.aws-region.amazonaws.com"
    port: 8883
    region: "your-aws-region"
    root_ca: "your-aws-root-ca" # this can be found at https://www.amazontrust.com/repository/AmazonRootCA1.pem
    cert: "your-cert.cert.pem"
    private_key: "your-private-key.private.key"
    client_id: "your-client-id" # note that client_id and topics might need to be explicitly added to your aws policy
    topic: "your-topic" 
    count: 10

azure:
  iot_hub:
    endpoint: "your-azure-iot-hub-endpoint"
    connection_string: "your-azure-connection-string"
    device_id: "your-azure-device-id"

mqtt:
  broker: "test.mosquitto.org"
  port: 8884
  auth:
    username: "rw"
    password: "readwrite"
  topic: "qsi_sensor"
  qos: 1
  retain: false
  interval: 5 # in seconds
```
