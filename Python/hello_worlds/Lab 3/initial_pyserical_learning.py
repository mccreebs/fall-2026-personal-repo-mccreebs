import serial

print("Learning Pyserial")

ser = serial.Serial("/dev/ttyACM0", 19200, timeout=10)

while not ser.is_open:
    print("Opening...")

# TODO: Use the serial object

ser.close()
