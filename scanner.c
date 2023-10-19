#include <stdio.h>
// #include <wiringPi.h>

// #define IR_GPIO_PIN 2

// int main() {
//     if (wiringPiSetup() == -1) {
//         fprintf(stderr, "Failed to initialize WiringPi.\n");
//         return 1;
//     }

//     pinMode(IR_GPIO_PIN, INPUT);

//     printf("IR receiver initialized. Listening for IR messages...\n");

//     while (1) {
//         //if (digitalRead(IR_GPIO_PIN) == HIGH) {
//         int value = digitalRead(IR_GPIO_PIN);
//         printf("IR Value: %d\n", value);
//         delay(50); 
//         //}
//     }

//     return 0;
// }

#include <IRremote.h>

const int RECV_PIN = 13;
IRrecv irrecv(RECV_PIN);
decode_results results;

void setup(){
  Serial.begin(9600);
  irrecv.enableIRIn();
  irrecv.blink13(true);
}

void loop(){
  if (irrecv.decode(&results)){
        Serial.println(results.value, HEX);
        irrecv.resume();
  }
}
