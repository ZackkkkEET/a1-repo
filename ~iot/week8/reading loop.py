from machine import ADC, Pin
from time import sleep
adc = ADC(Pin(34))
adc.atten(ADC.ATTN_11DB)
while True:
    raw = adc.read_u16()
    volts = raw / 65535 * 3.3
    print(f"raw={raw:5d}   v={volts:.2f}")
    sleep(0.2)