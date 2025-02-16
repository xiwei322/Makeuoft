#include <LiquidCrystal.h>
#include <Servo.h>

// Define servo motor objects
Servo servo1;
Servo servo2;
// Initialize the LCD with the 4-bit mode pins: RS, EN, D4, D5, D6
//LiquidCrystal lcd_1(7, 6, 5, 4, 3, 2);

// Arduino Code to dynamically receive data from Serial

String incomingData = "";  // Variable to store incoming data

void setup() {

  servo1.attach(13);  // Servo 1 connected to pin 12 a

  servo1.write(0);



  Serial.begin(9600);  // Initialize serial communication at 9600 baud rate

  pinMode(8, OUTPUT);  // Pin 8 as output
  pinMode(9, OUTPUT);  // Pin 9 as output

  
  // Set the voltage of each pin to HIGH (1)
  digitalWrite(8, LOW);   // Pin 8 HIGH
    digitalWrite(8, HIGH);   // Pin 8 HIGH
    servo1.write(2);
    delay(5000);
   digitalWrite(8, LOW);   // Pin 8 HIGH
    servo1.write(90);
  digitalWrite(9, LOW);   // Pin 9 HIGH


}

void loop() {
 if (Serial.available() > 0) {  // Check if data is available to read
        incomingData = Serial.readString();  // Read the incoming data
        Serial.println("Received: " + incomingData);  // Print the received data to the Serial Monitor

        // Check if data received is "Trash" or "Recycle"
        if (incomingData == "Trash") {
            digitalWrite(8, HIGH);  // Pin 8 HIGH
              servo1.write(0);
            delay(2000);             // Wait for 5 seconds
              servo1.write(90);
            digitalWrite(8, LOW);    // Pin 8 LOW
        }
        if (incomingData == "Recycle") {
            digitalWrite(9, HIGH);  // Pin 9 HIGH
              servo1.write(180);
            delay(2000);             // Wait for 3 seconds
              servo1.write(90);
            digitalWrite(9, LOW);    // Pin 9 LOW
        }

        // Clear incomingData for the next cycle
        incomingData = "";  
    }
}





 /*  if (Serial.available() > 0) {  // Check if data is available to read
    String data = Serial.readString();  // Read the incoming data
    Serial.println(data);  // Print the received data to the Serial Monitor

    if(data == "Trash"){
      digitalWrite(8, HIGH);
      delay(5000);
      digitalWrite(8,LOW);
      }
      if(data == "Recycle"){
      digitalWrite(9, HIGH);
      delay(3000);
      digitalWrite(9,LOW);
      }
  }


  // Check if data is available to read
  if (Serial.available() > 0) {
    // Read the incoming byte and append it to the string
    char incomingByte = Serial.read();
    
    // If the byte is a newline or carriage return, we have a complete message
    if (incomingByte == '\n' || incomingByte == '\r') {
      // Print the received data to the Serial Monitor
      Serial.print("Received: ");
      Serial.println(incomingData);
      if(incomingData == "Trash"){
      digitalWrite(8, HIGH);
      delay(5000);
      digitalWrite(8,LOW);
      }
      if(incomingData == "Recycle"){
      digitalWrite(9, HIGH);
      delay(3000);
      digitalWrite(9,LOW);
      }

      // Clear the incomingData string to start receiving the next data
      incomingData = "";
    } else {
      // If it's not a newline, keep adding it to the incoming data string
      incomingData += incomingByte;
    }
  }*/

