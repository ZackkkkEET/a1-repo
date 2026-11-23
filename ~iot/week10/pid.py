class PIDController:
    def __init__(self, kp, ki, kd, out_min=0.0, out_max=100.0):
        self.kp, self.ki, self.kd = kp, ki, kd
        self.out_min, self.out_max = out_min, out_max
        self.integral = 0.0
        self.prev_pv = None

    def update(self, sp, pv, dt):
        e = sp - pv
        cand = self.integral + e * dt
        if self.prev_pv is None:
            dpv = 0.0
        else:
            dpv = (pv - self.prev_pv) / dt
        self.prev_pv = pv

        u = self.kp * e + self.ki * cand - self.kd * dpv
        if u > self.out_max:
            u = self.out_max
        elif u < self.out_min:
            u = self.out_min
        else:
            self.integral = cand
        return u