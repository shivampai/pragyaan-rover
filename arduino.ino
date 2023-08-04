#include <Servo.h>

Servo soilServo; // Create a servo object


int ledPin = 13;
char command;
int ledStatus = 0;
int msensorStatus = 0;
void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
  soilServo.attach(9); // Attach the servo to pin 9
}

void loop() {
  if (Serial.available() > 0) {
    command = Serial.read();
    if (command == 'h') {
      if (ledStatus == 0) {
        digitalWrite(ledPin, HIGH);
        ledStatus = 1;
        Serial.println("2001");
      } else {
        digitalWrite(ledPin, LOW);
        ledStatus = 0;
        Serial.println("2002");
      }
    } else if (command == 'm') {
      if (msensorStatus == 0) {
        soilServo.write(90);
        msensorStatus = 1;
        Serial.println("2001");
      } else {
        soilServo.write(0);
        msensorStatus = 0;
        Serial.println("2002");
      }
    }

  }
}
