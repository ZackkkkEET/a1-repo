from machine import ADC, Pin, PWM
from time import sleep

adc = ADC(Pin(32))
adc.atten(ADC.ATTN_11DB)
pwm = PWM(Pin(21), freq=1000)

while True:
    light = adc.read_u16()
    pwm.duty_u16(light)
    print(light)
    sleep(0.1)
    
def read_avg(adc, n=16):
    total = 0
    for _ in range(n):
        total += adc.read_u16()
    return total // n