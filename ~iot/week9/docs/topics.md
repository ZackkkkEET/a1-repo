# Station s04 MQTT Topics

| Topic | Payload Format | QoS | Retained | Publisher | Subscriber(s) |
| :--- | :--- | :---: | :---: | :--- | :--- |
| `bench/s04/light` | Float string (`0.0` to `100.0`, e.g. `"98.5"`) | 0 | No | ESP32 (`node-s04`) | Pi (`LightMonitor`), `mosquitto_sub` |
| `bench/s04/status` | `"online"` or `"offline"` (Last Will) | 0 | Yes | ESP32 (`node-s04`) / Broker | Pi (`LightMonitor`), `mosquitto_sub` |
| `bench/s04/led/cmd` | `"on"` or `"off"` | 0 | No | Pi (`LightMonitor`) | ESP32 (`node-s04`) |
