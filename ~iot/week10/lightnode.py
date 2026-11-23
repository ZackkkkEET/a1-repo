from machine import ADC, Pin, PWM

class LightNode:
    def __init__(self, adc_pin=34, pwm_pin=25, dark=1580, bright=3104):
        self.adc = ADC(Pin(adc_pin))
        self.adc.atten(ADC.ATTN_11DB)
        self.pwm = PWM(Pin(pwm_pin), freq=1000)
        self.pwm.duty_u16(0)
        self.dark = dark
        self.bright = bright

    def read_raw(self):
        return self.adc.read()

    def read_avg(self, n=16):
        total = 0
        for _ in range(n):
            total += self.adc.read()
        return total / n

    def read_pct(self):
        raw = self.read_avg()
        pct = (raw - self.dark) / (self.bright - self.dark) * 100.0
        return max(0.0, min(100.0, pct))

    def set_brightness(self, percent):
        percent = max(0.0, min(100.0, percent))
        self.pwm.duty_u16(int(percent / 100 * 65535))