#include <stdio.h>
#include <ir_scanner_library.h>

int main() {
    // Initialize the IR scanner
    if (ir_scanner_init() != 0) {
        fprintf(stderr, "Failed to initialize the IR scanner.\n");
        return 1;
    }

    // Attempt to perform a scan
    int scan_result = ir_scanner_scan();
    
    if (scan_result != 0) {
        fprintf(stderr, "Failed to scan data. Error code: %d\n", scan_result);
    } else {
        printf("Scan successful. Now you can process the data.\n");
        // Process the scanned data here
    }

    // Clean up and release resources
    ir_scanner_cleanup();

    return 0;
}
