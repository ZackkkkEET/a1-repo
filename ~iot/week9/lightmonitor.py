# lightmonitor.py: monitor bench s04 status (Rung 1), Pi LED (Rung 2), and MQTT cmd (Rung 3)
import paho.mqtt.client as mqtt
from gpiozero import LED

class LightMonitor:
    """Follows one station's bench subtree; tracks status and drives LEDs."""

    DARK = 30.0

    def __init__(self, broker, station):
        self.station      = station
        self.topic_sub    = f"bench/{station}/#"
        self.topic_light  = f"bench/{station}/light"
        self.topic_status = f"bench/{station}/status"
        self.topic_cmd    = f"bench/{station}/led/cmd"

        self.last_pct = None
        self.count    = 0
        self.cmd_on   = False
        self.led      = LED(17)

        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(broker)

    def on_connect(self, client, userdata, flags, reason_code, properties):
        print(f"Connected ({reason_code}) -> subscribed to {self.topic_sub}")
        client.subscribe(self.topic_sub)

    def on_message(self, client, userdata, msg):
        payload = msg.payload.decode()
        if msg.topic == self.topic_status:
            print(f"[STATUS] {msg.topic}: {payload}")
        elif msg.topic == self.topic_light:
            self.last_pct = float(payload)
            self.count += 1
            self.react()

    def react(self):
        is_dark = self.last_pct < self.DARK
        alert = " [DARK ALERT]" if is_dark else ""
        print(f"[{self.count}] {self.topic_light}: {self.last_pct:.1f}%{alert}")

        # Rung 2: turn on the LED wired to Pi GPIO 17 (Pin 11)
        if is_dark:
            self.led.on()
        else:
            self.led.off()

        # Rung 3: publish 'on'/'off' over MQTT when state changes
        if is_dark and not self.cmd_on:
            self.client.publish(self.topic_cmd, "on")
            self.cmd_on = True
            print(f"  -> Published 'on' to {self.topic_cmd}")
        elif not is_dark and self.cmd_on:
            self.client.publish(self.topic_cmd, "off")
            self.cmd_on = False
            print(f"  -> Published 'off' to {self.topic_cmd}")

    def run(self):
        self.client.loop_forever()

if __name__ == "__main__":
    LightMonitor("localhost", "s04").run()
