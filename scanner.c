#include <stdio.h>
#include <wiringPi.h>

#define IR_GPIO_PIN 27 

int main() {
    if (wiringPiSetup() == -1) {
        fprintf(stderr, "Failed to initialize WiringPi.\n");
        return 1;
    }

    pinMode(IR_GPIO_PIN, INPUT);

    printf("IR receiver initialized. Listening for IR messages...\n");

    while (1) {
        //if (digitalRead(IR_GPIO_PIN) == HIGH) {
        int value = digitalRead(IR_GPIO_PIN);
        printf("IR Value: %d\n", value);
        delay(50); 
        //}
    }

    return 0;
}
