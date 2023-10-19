#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <unistd.h>

#define GPIO_BASE 0xFE200000  // Use the appropriate base address for your Raspberry Pi model

// Define offsets for GPIO registers
#define GPFSEL0  (0x00 / 4)
#define GPLEV0   (0x34 / 4)

int main() {
    int fd;
    void *gpio_map;
    volatile unsigned int *gpio;

    fd = open("/dev/mem", O_RDWR | O_SYNC);
    if (fd < 0) {
        perror("Unable to open /dev/mem");
        return -1;
    }

    gpio_map = mmap(NULL, 4096, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO_BASE);
    if (gpio_map == MAP_FAILED) {
        perror("mmap failed");
        close(fd);  // Close the file descriptor
        return -1;
    }

    gpio = (volatile unsigned int *)gpio_map;

    // Read the value of GPIO 17
    int pin_value = (gpio[GPLEV0] >> 17) & 1;
    
    if (pin_value)
        printf("GPIO 17 is high\n");
    else
        printf("GPIO 17 is low\n");

    // Unmap the memory and close the file descriptor
    munmap(gpio_map, 4096);
    close(fd);

    return 0;
}
