from machine import Pin, PWM

class Motor:
    def __init__(self, a, b):
        self.a=PWM(Pin(a))
        self.b=PWM(Pin(b))
        self.a.freq(1000)
        self.b.freq(1000)
        self.a.duty(0)
        self.b.duty(0)

    def drive(self, speed):
        d = int(speed * 1023)
        if d>0:
            self.b.duty(0)
            self.a.duty(d)
        else:
            self.a.duty(0)
            self.b.duty(-d)

    def stop(self):
        self.a.duty(0)
        self.b.duty(0)


class Servo:
    def __init__(self,pin):
        self.p = PWM(Pin(pin),freq=50)
        self.p.duty(75)

    def set_pos(self, pos):
        if 0 <= pos <= 1:
            pos = int(50*pos)+50
            self.p.duty(pos)


