import motor
import time

class DriveSystem:
    def __init__(self):
        self.car = motor.OrdinaryCar()

    def scale_speed(self, speed):
        """ Returns a duty from 0 to 4095 based on given speed """
        return int(speed / 100 * 4095)

    def set_speeds(self, lf, lr, rf, rr):
        """ Pass in four speeds each -100 to 100 to set the wheel duty cycle """
        
        self.car.set_motor_model(self.scale_speed(lf),
                                 self.scale_speed(lr),
                                 self.scale_speed(rf),
                                 self.scale_speed(rr))

    def go(self, left_wheel_speed, right_wheel_speed):
        """ Speeds as integers from -100 to 100. """
        self.set_speeds(left_wheel_speed, left_wheel_speed, right_wheel_speed, right_wheel_speed)

    def stop(self):
        self.set_speeds(0, 0, 0, 0)

    def go_straight_for_seconds(self, seconds, speed):
        self.go(speed, speed)
        time.sleep(seconds)
        self.stop()

    def go_straight_for_inches(self, inches, speed):
        m = 0.5
        b = 0
        inches_per_sec = speed * m + b
        seconds = inches/inches_per_sec
        self.go_straight_for_seconds(seconds, speed)

    
