from machine import ADC, Pin
from time import sleep

adc = ADC(Pin(32))
adc.atten(ADC.ATTN_11DB)

while True:
    volts = adc.read()
    print(volts)
    sleep(0.2)