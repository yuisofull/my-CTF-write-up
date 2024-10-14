#include <stdio.h>
#include <stdlib.h>
#include <string.h>

unsigned long* encryption(unsigned long data[], unsigned long size)
{
    unsigned int eax;
    unsigned int edx;
    unsigned int ecx;
    unsigned int byte_address;

    for (byte_address = 0; byte_address < size; byte_address++)
    {
        eax = data[byte_address]; // a = x
        ecx = eax + 0x11; // c = a + 0x11
        eax = eax + 0xB;  // a = a + 0xB
        ecx = eax * ecx;  // c = a * c = (a + 0xB) * (a + 0x11)
        edx = ecx;        // d = c = (a + 0xB) * (a + 0x11)
        edx = edx >> 8;   // d = d >> 8 = (a + 0xB) * (a + 0x11) / 2^8
        eax = edx;        // a = d = (a + 0xB) * (a + 0x11) / 2^8
        eax = eax ^ ecx;  // a = a ^ c = (a + 0xB) * (a + 0x11) / 2^8 ^ (a + 0xB) * (a + 0x11)
        eax = eax >> 0x10;// a = a >> 0x10 = ((a + 0xB) * (a + 0x11) / 2^8 ^ (a + 0xB) * (a + 0x11)) / 2^16
        eax = eax ^ edx;  // a = a ^ d = ((a + 0xB) * (a + 0x11) / 2^8 ^ (a + 0xB) * (a + 0x11)) / 2^16 ^ (a + 0xB) * (a + 0x11) / 2^8
        eax = eax ^ ecx;  // a = a ^ c = ((a + 0xB) * (a + 0x11) / 2^8 ^ (a + 0xB) * (a + 0x11)) / 2^16 ^ (a + 0xB) * (a + 0x11) / 2^8 ^ (a + 0xB) * (a + 0x11)
        data[byte_address] = eax; // Store the result back to the array
    }
    return data;
}
// find c
// a = d = c >> 8
// a = a ^ c = c ^ (c >> 8) 
// a = a >> 0x10 = (c ^ (c >> 8)) >> 16
// a = a ^ d = [(c ^ (c >> 8)) >> 16] ^ (c >> 8)
// a = a ^ c = [(c ^ (c >> 8)) >> 16] ^ (c >> 8) ^ c    

// reverse c




unsigned long* _encryption(void* data, unsigned long size)
{
    unsigned long* data_chunk = NULL;
    unsigned long* result;
    int i;

    if (size & 1) size++;
    data_chunk = (unsigned long*)malloc(size * sizeof(unsigned long));
    if (!data_chunk) return NULL;
    memset(data_chunk, 0, size * sizeof(unsigned long)); // Ensure memory is initialized to zero
    for (i = 0; i < size / 2; i++) data_chunk[i] = ((unsigned short*)data)[i];

    result = encryption(data_chunk, size / 2); // Adjusted the size passed to encryption
    return result;
}

int main(int argc, char *argv[])
{
    if (argc < 2) {
        printf("Usage: %s <text to encrypt>\n", argv[0]);
        return 1; // Exit if no argument is provided
    }

    const char* input = argv[1];
    unsigned long size = strlen(input); // Use the length of the input argument
    // Ensure the input is treated correctly based on how _encryption function is expected to work
    unsigned long* encrypted_data = _encryption((void*)input, size);

    // Print each encrypted unsigned long in hexadecimal format
    printf("Encrypted data in hexadecimal format: ");
    for (unsigned long i = 0; i < (size + 1) / 2; i++) { // Adjusted loop condition based on encryption function logic
        printf("%lx", encrypted_data[i]);
    }
    printf("\n");

    free(encrypted_data); // Remember to free the allocated memory

    return 0;
}