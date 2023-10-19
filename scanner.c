#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <unistd.h>

#define GPIO_BASE 0x3F000000  // The base address for GPIO memory mapping on a Raspberry Pi

int main() {
    int fd;  // File descriptor for /dev/mem
    void *gpio_map;  // Pointer to the mapped memory
    unsigned int *gpio;  // Pointer to the GPIO control registers

    // Open /dev/mem to access physical memory
    fd = open("/dev/mem", O_RDWR | O_SYNC);
    if (fd < 0) {
        perror("Unable to open /dev/mem");
        return -1;
    }

    // Map the GPIO registers into the process's address space
    gpio_map = mmap(NULL, 4096, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO_BASE);
    if (gpio_map == MAP_FAILED) {
        perror("mmap failed");
        return -1;
    }

    // Get a pointer to the GPIO control registers
    gpio = (volatile unsigned int *)(uintptr_t)gpio_map;

    // Read the value of GPIO 7
    if (gpio[0] & (1 << 7))
        printf("Pin 7 is high\n");
    else
        printf("Pin 7 is low\n");

    // Unmap the memory and close /dev/mem
    munmap(gpio_map, 4096);
    close(fd);

    return 0;
}


// if (gpio_lev & (1<<7))
//   printf("1")
// else
//   printf("2)


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
