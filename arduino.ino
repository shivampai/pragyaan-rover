#include <Servo.h>
#include <DHT.h>

#define DHTPIN 2   // Replace with the pin number where your DHT11 data pin is connected
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);


Servo soilServo; // Create a servo object

Servo flagServo; // Create a servo object


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

    if (command == 't') {
      float temperature = dht.readTemperature();
      float humidity = dht.readHumidity();
      Serial.print(temperature);
      Serial.print(",");
      Serial.print(humidity);
      Serial.print("\n");
    }
    else if (command == "ter") {
    }
    else if (command == 't') {
      float temperature = dht.readTemperature();
      float humidity = dht.readHumidity();
      Serial.print(temperature);
      Serial.print(",");
      Serial.print(humidity);
      Serial.print("\n");
    }
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
    else if (command == "fa") {
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
