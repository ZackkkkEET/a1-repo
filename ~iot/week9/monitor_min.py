# monitor_min.py: print every light reading as it arrives
import paho.mqtt.client as mqtt

BROKER = "localhost"
TOPIC  = "bench/s04/light"

def on_connect(client, userdata, flags, reason_code, properties):
    print("Connected:", reason_code)
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    print(msg.topic, msg.payload.decode())

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER)
client.loop_forever()
