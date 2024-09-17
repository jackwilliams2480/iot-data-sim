import random
import json
from datetime import datetime, timezone

def generate_temperature():
    """
    Generates a random temperature value.
    Common values: 25 to 30 degrees Celsius (float)
    """
    return "{}.{}".format(random.randint(25, 30), random.randint(100000, 999999))

def generate_humidity():
    """
    Generates a random humidity value.
    Common values: 30 to 70 percent (float)
    """
    return "{}".format(random.randint(30, 70))

def generate_decibel():
    """
    Generates a random decibel value.
    Common values: 30 to 130 dB (float)
    """
    return "{}".format(random.randint(30, 130))

def generate_pressure():
    """
    Generates a random pressure value.
    Common values: 950 to 1050 hPa (float)
    """
    return "{}".format(random.randint(950, 1050))

def generate_accelerometer():
    """
    Generates random accelerometer values for x, y, z axes.
    Common values: -365 to 365 d (tuple of floats)
    """
    return "x:{}, y:{}, z:{}".format(random.randint(-365, 365), random.randint(-365, 365), random.randint(-365, 365))

def generate_rotary_encoder():
    """
    Generates a random rotary encoder value.
    Common values: 0 to 1023 (int), high variablity, depends on the encoder used and its resolution
    """
    return "{}".format(random.randint(0, 1023))

def generate_motion():
        """
        Generates a random motion value.
        Common values: 0 (no motion) or 1 (motion detected) (int)
        """
        return "{}".format(random.randint(0, 1))

def generate_ac_current():
    """
    Generates a random AC current value.
    Common values: 0 to 30 A (float)
    """
    return "{}".format(random.randint(0,30))

def generate_light():
    """
    Generates a random light intensity value.
    Common values: 0 to 1000 lux (float)
    """
    return "{}".format(random.randint(0, 1000))

def generate_dry_wet():
    """
    Generates a random dry/wet value.
    Common values: 0 (dry) or 1 (wet) (int)
    """
    return "{}".format(random.randint(0, 1))

def generate_voltage():
    """
    Generates a random voltage value.
    Common values: 0 to 240 V (float)
    """
    return "{}".format(random.randint(0, 240))

def generate_water_level():
    """
    Generates a random water level detection value.
    Common values: 0 to 100 percent (float)
    """
    return "{}".format(random.randint(0, 100))

def generate_pulse_counter():
    """
    Generates a random pulse counter value.
    Common values: 0 to 1000 pulses (int)
    """
    return "{}".format(random.randint(0, 1000))

def generate_gas():
    """
    Generates a random gas concentration value.
    Common values: 0 to 500 ppm (float)
    """
    return "{}".format(random.randint(0, 500))

def generate_air_quality():
    """
    Generates a random air quality index value.
    Common values: 0 to 500 AQI (int)
    """
    return "{}".format(random.randint(0, 500))

def json_builder(include_temperature=False, include_humidity=False, include_decibel=False, include_pressure=False,
                    include_accelerometer=False, include_rotary_encoder=False, include_motion=False, include_ac_current=False,
                    include_light=False, include_dry_wet=False, include_voltage=False, include_water_level=False,
                    include_pulse_counter=False, include_gas=False, include_air_quality=False):
    
    payload = {
        "sensorID": 1,
        "sensorName": "simulink",
        "batteryVoltage": 3,
        "time": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "data": {}
    }
    
    data = payload['data']
    
    if include_temperature:
        data['temperature'] = generate_temperature()
    if include_humidity:
        data['humidity'] = generate_humidity()
    if include_decibel:
        data['decibel'] = generate_decibel()
    if include_pressure:
        data['pressure'] = generate_pressure()
    if include_accelerometer:
        data['accelerometer'] = generate_accelerometer()
    if include_rotary_encoder:
        data['rotary_encoder'] = generate_rotary_encoder()
    if include_motion:
        data['motion'] = generate_motion()
    if include_ac_current:
        data['ac_current'] = generate_ac_current()
    if include_light:
        data['light'] = generate_light()
    if include_dry_wet:
        data['dry_wet'] = generate_dry_wet()
    if include_voltage:
        data['voltage'] = generate_voltage()
    if include_water_level:
        data['water_level'] = generate_water_level()
    if include_pulse_counter:
        data['pulse_counter'] = generate_pulse_counter()
    if include_gas:
        data['gas'] = generate_gas()
    if include_air_quality:
        data['air_quality'] = generate_air_quality()
    
    return json.dumps(payload)