String inputString = "";
bool isStringComplete = false;

void setup() {
  Serial.begin(19200);
  inputString.reserve(200);
  pinMode(LED_BUILTIN, OUTPUT);

  Serial.println("Ready! Enter LED ON, LED OFF, or FLASH <count> <period>");
}

void loop() {
  if (isStringComplete) {
    inputString.trim();

    if (inputString.equals("LED ON")) {
      digitalWrite(LED_BUILTIN, HIGH);
      Serial.println("The LED is now on!");

    } else if (inputString.equals("LED OFF")) {
      digitalWrite(LED_BUILTIN, LOW);
      Serial.println("The LED is now off!");

    } else if (inputString.startsWith("FLASH ")) {
      int firstSpace = inputString.indexOf(' ');
      int secondSpace = inputString.indexOf(' ', firstSpace + 1);

      if (firstSpace != -1 && secondSpace != -1) {
        int flashCount =
            inputString.substring(firstSpace + 1, secondSpace).toInt();
        int period =
            inputString.substring(secondSpace + 1).toInt();

        if (flashCount > 0 && period >= 2) {
          int halfPeriod = period / 2;

          Serial.print("Flashing ");
          Serial.print(flashCount);
          Serial.print(" times with a period of ");
          Serial.print(period);
          Serial.println(" ms.");

          for (int i = 0; i < flashCount; i++) {
            digitalWrite(LED_BUILTIN, HIGH);
            delay(halfPeriod);

            digitalWrite(LED_BUILTIN, LOW);
            delay(halfPeriod);
          }

          Serial.println("Flash complete!");

        } else {
          Serial.println(
              "Error: Flash count must be positive and period must be at least 2 ms.");
        }

      } else {
        Serial.println("Usage: FLASH <count> <period>");
      }

    } else {
      Serial.println("Unknown command. Try LED ON, LED OFF, or FLASH <count> <period>.");
    }

    // Reset input after processing the command
    inputString = "";
    isStringComplete = false;
  }
}

void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();

    if (inChar == '\n') {
      isStringComplete = true;
    } else if (inChar != '\r') {
      inputString += inChar;
    }
  }
}
