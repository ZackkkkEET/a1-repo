ESP32, LDR on GPIO 34 (calibrated dark=1580, bright=3104), LED on GPIO 25.
Setpoint 50%, loop period 100 ms (10 Hz)



| # | kp | ki | kd | Observation | Change and why |
| 1 | 0.5 | 0 | 0 | LED blinked rapidly; pv alternated between about 9 and 59 every cycle. Loop gain too high for the strong LED, lowered kp
| 2 | 0.3 | 0 | 0 | LED Stable
| 3 | 0.15 | 0 | 0 | Steady, but pv was wrong
| 4 | 0.15 | 1.0 | 0 | wobble and unstable data
| 5 | 0.15 | 3.0 | 0 | pv flipped between about 14 and 45 before the step (oscillation). Gains too high at low LED levels, lowered both
| 6 | 0.05 | 0.5 | 0 | Calm hold at 30, rise about 1.4 s, overshoot about 3%, settling about 2.7 s. Rise too slow, raised ki
| 7 | 0.05 | 0.8 | 0 | Calm hold rise about 0.85 s, overshoot about 5%, settling about 1.4 s. Meets targets and kept as final 
| 8 | 0.05 | 0.8 | 0 | Windup test else removed & Restored the else

## Final gains
- kp = 0.05: higher values made the strong LED flip-flop between two levels.
- ki = 0.8: fastest value that kept the hold at the setpoint calm (0.5 was slower, 3.0 oscillated).
- kd = 0: the sensor is noisy and the loop already meets every target without it.

## Verification tests
| Test | Result | Grade |
| Step up 30 to 60 | rise about 0.85 s, overshoot about 5%, settled in about 1.4 s
| Step down 60 to 30 | fall about 0.85 s, no real undershoot, settled in about 0.9 s
| Disturbance (attempt 1): flashlight | Flashlight was too bright: pv hit 100 and u dropped to 0, then recovered in about 1.2 s once removed | pass (light exceeded what the LED can offset) 
| Disturbance (repeat): flashlight, then hand shade | Dimmer flashlight and hand shade both tested; the loop compensated and returned to the setpoint band, as expected.
| Saturation | SP held at 100 for 5 s (LED pinned), then dropped to 40; the output came off its limit and pv returned to 40 as expected, with no long overshoot tail.  

## Notes
- Anti-windup evidence: while the flashlight pinned u at 0 for about 4 s, the integral stayed frozen, and u resumed at about its old level (8.4% vs 7.5%) as soon as the light was removed.