from rosebot import Rosebot
import time

def main():
    print("Lab 5b Line Following")
    robot = Rosebot()

    try:
        while True:
            if robot.ultrasonic.get_cm() < 20:
                robot.drive_system.stop()
            else:
                if robot.line_sensors.get_line_word() == "WBW":
                    robot.drive_system.set_speeds(20, 20, 20, 20)
                elif robot.line_sensors.get_line_word() == "BWW" or robot.line_sensors.get_line_word() == "BBW":
                    robot.drive_system.set_speeds(0, 0, 20, 20)
                elif robot.line_sensors.get_line_word() == "WWB" or robot.line_sensors.get_line_word() == "WBB":
                    robot.drive_system.set_speeds(20, 20, 0, 0)
                else:
                    robot.drive_system.set_speeds(0, 0, 0, 0)

            time.sleep(0.1)

    except KeyboardInterrupt:
        # Handle ctrl c to exit program cleanly.
        robot.drive_system.stop()
        print("Goodbye!")

# def follow_line(self, robot):
#     if robot.line_sensors.get_line_word() == "WBW":
#         robot.drive_system.set_speeds(30, 30, 30, 30)
#     elif robot.line_sensors.get_line_word() == "BWW":
#          robot.drive_system.set_speeds(0, 0, 30, 30)
#     elif robot.line_sensors.get_line_word() == "WWB":
#         robot.drive_system.set_speeds(30, 30, 0, 0)
#     else:
#         robot.drive_system.set_speeds(20, 20, 20, 20)


main()