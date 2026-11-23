from time import ticks_ms, ticks_diff, sleep_ms
from pid import PIDController
from lightnode import LightNode

MODE = "saturation"        # change to "saturation" for the second run
PERIOD_MS = 100

node = LightNode(adc_pin=34, pwm_pin=25, dark=1580, bright=3104)
pid = PIDController(kp=0.05, ki=0.8, kd=0.0)

def setpoint(t):
    if MODE == "saturation":
        return 100.0 if t < 5 else 40.0
    return 50.0

prev = ticks_ms()
t0 = prev
print("t,sp,pv,u")

while True:
    now = ticks_ms()
    t = ticks_diff(now, t0) / 1000
    if t > 15:
        break
    dt = ticks_diff(now, prev) / 1000
    prev = now

    sp = setpoint(t)
    pv = node.read_pct()
    u = pid.update(sp, pv, dt)
    node.set_brightness(u)

    print(t, sp, pv, u, sep=",")
    sleep_ms(max(0, PERIOD_MS - ticks_diff(ticks_ms(), now)))

node.set_brightness(0)
print("done")