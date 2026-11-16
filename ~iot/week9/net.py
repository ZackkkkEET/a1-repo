# net.py: join Wi-Fi, or say clearly why not
import network
from time import sleep
def connect_wifi(ssid, password, timeout_s=10):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Joining", ssid, "...")
        wlan.connect(ssid, password)
        for _ in range(timeout_s * 2):        # poll every half second
            if wlan.isconnected():
                break
            sleep(0.5)
    if not wlan.isconnected():
        raise RuntimeError("Wi-Fi failed: check SSID, password, and that the network is 2.4 GHz")
    print("Wi-Fi OK, address:", wlan.ifconfig()[0])
    return wlan
