#include <Servo.h>
#include <DHT.h>
#include <NewPing.h>

#define TRIGGER_PIN 16

#define ECHO_PIN 17

#define MAX_DISTANCE 500// Maximum distance we want to ping for (in centimeters). Maximum sensor distance is rated at 400-500cm.

#define DHTPIN 2   // Replace with the pin number where your DHT11 data pin is connected
#define DHTTYPE DHT11

NewPing sonar1(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE);

DHT dht(DHTPIN, DHTTYPE);


Servo soilServo; // Create a servo object

Servo flagServo; // Create a servo object

//Leftir - D4
//Right ir - D7
//mSensor - A0
//headlight - D13
//soilServo - D9
//flagServo - D10
//Ultrasonic - Trig - A2 , Echo - A3
//DHT - D2
int ledPin = 13;
char command;
int ledStatus = 0;
int msensorStatus = 0;
int faStatus = 0;
int obFLPin = 4;
int obFRPin = 7;

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
  flagServo.attach(10);
  soilServo.attach(9); // Attach the servo to pin 9
  dht.begin();
}

void loop() {
  if (Serial.available() > 0) {
    command = Serial.read();
    if (command == "z") {
      float temperature = dht.readTemperature();
      float humidity = dht.readHumidity();
      int ter = sonar1.ping_cm();
      int sensorValue = analogRead(A0);
      int soilMoisture = map(sensorValue, 0, 1023, 0, 100);
      Serial.println("\nall,");
      Serial.print(ter, ",");
      Serial.print(temperature, ",");
      Serial.print(soilMoisture, ",");
      Serial.print(humidity, ",Healthy,");
      Serial.print(msensorStatus, ",");
      Serial.print(faStatus, ",");
      Serial.print(digitalRead(obFLPin), ",");
      Serial.print(digitalRead(obFRPin), ",Error");
    }
    else  if (command == 'a') {
      float temperature = dht.readTemperature();
      float humidity = dht.readHumidity();
      int ter = sonar1.ping_cm();
      int sensorValue = analogRead(A0);
      int soilMoisture = map(sensorValue, 0, 1023, 0, 100);
      Serial.print("\nall,");
      Serial.print(ter);
      Serial.print(",");
      Serial.print(temperature);
      Serial.print(",");
      Serial.print(100-soilMoisture);
      Serial.print(",");
      Serial.print(humidity);
      Serial.print(",Healthy,");
      Serial.print(msensorStatus);
      Serial.print(",");
      Serial.print(faStatus);
      Serial.print(",");
      Serial.print(digitalRead(obFLPin));
      Serial.print(",");
      Serial.print(digitalRead(obFRPin));
      Serial.print(",Error");

    }
//    else  if (command == 'a') {
//      float temperature = dht.readTemperature();
//      float humidity = dht.readHumidity();
//      Serial.pr
//    }
    else if (command == "ob") {
      Serial.println("\nob,");
      Serial.print(digitalRead(obFLPin));
      Serial.print(",");
      Serial.print(digitalRead(obFRPin));
    }
    else if (command == 'h') {
      if (ledStatus == 0) {
        digitalWrite(ledPin, HIGH);
        ledStatus = 1;
        Serial.println("2001");
      } else {
        digitalWrite(ledPin, LOW);
        ledStatus = 0;
        Serial.println("2002");
      }
    }
    else if (command == "f") {
      if (faStatus == 0) {
        flagServo.write(90);
        faStatus = 1;
        Serial.println("2001");
      } else {
        flagServo.write(0);
        faStatus = 0;
        Serial.println("2002");
      }
    }
    else if (command == 'm') {
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
