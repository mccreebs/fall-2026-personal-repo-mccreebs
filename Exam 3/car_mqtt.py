import mqtt_helper as mh
import signal
import time
from rosebot import Rosebot
class App:

    def __init__(self):
        self.robot = Rosebot()

        self.mqtt_client = mh.MqttClient()
        self.mqtt_client.connect(subscription_topic_name="me435/mccreebs/#",
                                 publish_topic_name="me435/mccreebs/to_computer")
        self.mqtt_client.callback = self.mqtt_callback



    def mqtt_callback(self, message_type, message_payload):
        print("Received type: ", message_type)
        print("Received payload: ", message_payload)

        if message_type == "left":
            if message_payload[0] == 1:
                self.robot.drive_system.set_speeds(message_payload[2], message_payload[2], 0, 0)
            elif message_payload[0] == 0:
                self.robot.drive_system.set_speeds(-message_payload[2], -message_payload[2], 0, 0) 
            time.sleep(message_payload[1])     

        if message_type == "right":
            if message_payload[0] == 1:
                self.robot.drive_system.set_speeds(0, 0, message_payload[2], message_payload[2])
            elif message_payload[0] == 0:
                self.robot.drive_system.set_speeds(0, 0, -message_payload[2], -message_payload[2]) 
            time.sleep(message_payload[1])  

        if message_type == "both":
            if message_payload[0] == 1:
                self.robot.drive_system.set_speeds(message_payload[2], message_payload[2], message_payload[3], message_payload[3])
            elif message_payload[0] == 0:
                self.robot.drive_system.set_speeds(-message_payload[2], -message_payload[2], -message_payload[3], -message_payload[3]) 
            time.sleep(message_payload[1]) 

def main():
    print("Car MQTT")
    app = App()

    try:
        # while True:
            # app.mqtt_client.send_message("beep", [40, 40, 40, 40])
            # time.sleep(2)
        #     app.mqtt_client.send_message("stop", [0, 0, 0, 0])
        #     time.sleep(1)

        signal.pause() # Keep the program alive but does nothing.
    except KeyboardInterrupt:
        print("Goodbye")
        app.robot.drive_system.stop()
        app.mqtt_client.close()



main()