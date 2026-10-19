import gpiozero as gz
import time
import signal

def basic_on_off():
    print("Basic On/Off")
    green_led = gz.DigitalOutputDevice(18)
    green_led.on()
    time.sleep(3)
    green_led.off()

def fancy_leds():
    print("Fancy Leds")
    red_led = gz.LED(14)
    yellow_led = gz.LED(15)
    green_led = gz.LED(18)

    # green_led.on()
    # time.sleep(3)
    # green_led.off()

    red_led.blink(on_time=2, off_time=0.1, )
    time.sleep(0.1)
    yellow_led.blink(on_time=2, off_time=0.1)
    time.sleep(0.1)
    green_led.blink(on_time=2, off_time=0.1)
    signal.pause()

def led_board():
    print("LED Board")

    leds = gz.LEDBoard(14, 15, 18, pwm=True)

    for i in range(5):
        leds.on()
        time.sleep(1)
        leds.off()
        time.sleep(1)

    leds.value = (0, 0.5, 0)
    time.sleep(1)
    leds.off()
    
    

def main():
    # basic_on_off()
    # fancy_leds()
    led_board()

main()

