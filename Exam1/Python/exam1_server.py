import flask
import arduino
import threading

app = flask.Flask(__name__, static_url_path="", static_folder="Public")

serial_lock = threading.Lock()
arduino = arduino.Arduino("/dev/ttyACM0") # TODO: set port if needed

@app.get("/")
def handle_naked_domain():
    return flask.redirect("/index.html")

@app.get("/api/led/<command>")
def handle_arduino_LED_commands(command):
    with serial_lock:
        response = arduino.send_LED_command(command)
    return response

@app.get("/api/flash/<number>/<delay>")
def handle_arduino_FLASH_commands(number, delay):
    with serial_lock:
        response = arduino.send_FLASH_command(number, delay)
    return response

if __name__ == "__main__":
    print("Running Flask")
    arduino.connect()
    try:
        app.run(host = '0.0.0.0', port = 8081, use_reloader=False)
    finally:
        print("Disconnecting Arduino")
        arduino.disconnect()