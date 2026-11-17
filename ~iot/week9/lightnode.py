# lightnode.py: read calibrated light percentage (GPIO34) and drive LED (GPIO25)
from machine import ADC, Pin, PWM

class LightNode:
    def __init__(self, adc_pin=34, pwm_pin=25, dark=300, bright=3400):
        self.adc = ADC(Pin(adc_pin))
        self.adc.atten(ADC.ATTN_11DB)      # full 0-3.3V range (0-4095)
        self.pwm = PWM(Pin(pwm_pin), freq=1000)
        self.pwm.duty(0)
        self.dark = dark
        self.bright = bright

    def read_raw(self):
        return self.adc.read()

    def read_pct(self):
        raw = self.read_raw()
        pct = (raw - self.dark) / (self.bright - self.dark) * 100.0
        return max(0.0, min(100.0, pct))