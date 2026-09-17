String inputString = "";      // a String to hold incoming data
bool isStringComplete = false;  // whether the string is complete

void setup() {
  Serial.begin(19200);
  inputString.reserve(200);
  pinMode(13, OUTPUT);
}

void loop() {
  // print the string when a newline arrives:
  if (isStringComplete) {
    if (inputString.equals("LED ON")) {
      digitalWrite(13, HIGH);
      Serial.println("The LED is now on!");
    } else if (inputString.equals("LED OFF")) {
      digitalWrite(13, LOW);
      Serial.println("The LED is now off!");
    } else {
      Serial.print("Unknown command --> ");
      Serial.println(inputString);
    }

    inputString = "";
    isStringComplete = false;
  }
}


void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    if (inChar == '\n') {
      isStringComplete = true;
    } else {
      inputString += inChar;
    }
  }
}
