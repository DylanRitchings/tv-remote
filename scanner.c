#include <stdio.h>
#include <wiringPi.h>

// Define the GPIO pin where the IR receiver is connected
#define IR_GPIO_PIN 27 // Replace with the actual GPIO pin number

int main() {
    if (wiringPiSetup() == -1) {
        fprintf(stderr, "Failed to initialize WiringPi.\n");
        return 1;
    }

    // Set the GPIO pin to input mode
    pinMode(IR_GPIO_PIN, INPUT);

    printf("IR receiver initialized. Listening for IR messages...\n");

    while (1) {
        //if (digitalRead(IR_GPIO_PIN) == HIGH) {
            // IR signal detected
        int value = digitalRead(IR_GPIO_PIN);
        printf("Raw IR Value: %d\n", value);
        delay(100); // Adjust the delay as needed
        //}
    }

    // The cleanup code will not be reached in this example, as the loop is infinite

    return 0;
}
