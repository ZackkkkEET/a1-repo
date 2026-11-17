# pub_light.py: publish the calibrated light level once a second
from umqtt.simple import MQTTClient
from time import sleep
import config
from net import connect_wifi
from lightnode import LightNode

TOPIC = f"bench/{config.STATION}/light".encode()

connect_wifi(config.WIFI_SSID, config.WIFI_PASSWORD)
node   = LightNode(adc_pin=34, pwm_pin=25, dark=300, bright=3400)
client = MQTTClient(f"node-{config.STATION}", config.BROKER_IP)
client.connect()
print("MQTT connected to", config.BROKER_IP)

while True:
    pct = node.read_pct()
    client.publish(TOPIC, f"{pct:.1f}".encode())
    sleep(1)