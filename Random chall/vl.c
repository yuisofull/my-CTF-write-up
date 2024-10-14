#include <stdio.h>
#include <stdlib.h>
#include <string.h>

unsigned long *encryption(unsigned long data[], unsigned long size)
{
    unsigned int eax;
    unsigned int edx;
    unsigned int ecx;
    unsigned int byte_address;

    for (byte_address = 0; byte_address < size; byte_address++)
    {
        eax = data[byte_address];
        ecx = eax + 0x11;
        eax = eax + 0xB;
        ecx = eax * ecx;
        edx = ecx;
        edx = edx >> 8;
        eax = edx;
        eax = eax ^ ecx;
        eax = eax >> 0x10;
        eax = eax ^ edx;
        eax = eax ^ ecx;
        data[byte_address] = eax;
    }
    return data;
}

unsigned long *_encryption(void *data, unsigned long size)
{
    unsigned long *data_chunk = NULL;
    unsigned long *result;
    int i;

    if (size & 1)
        size++;
    data_chunk = (unsigned long *)malloc(size * sizeof(unsigned long));
    if (!data_chunk)
        return NULL;
    memset(data_chunk, 0, size * sizeof(unsigned long)); // Ensure memory is initialized to zero
    for (i = 0; i < size / 2; i++)
        data_chunk[i] = ((unsigned short *)data)[i];

    result = encryption(data_chunk, size / 2); // Adjusted the size passed to encryption
    return result;
}

void brute_force()
{
    const char *target = "188d1f2f13cd5b601bd6047f4496ff74496ff74496ff7";
    int pos = 0;
    int length = strlen(target);

    // Brute force all possible 2-character strings
    // Outer loop for the first character
    while (pos < length)
    {
        int found = 0;
        char *substring = (char *)malloc(9); // Allocate memory for the substring
        strncpy(substring, target + pos, 8);
        for (int i = 0; i < 256; i++)
        {
            if (found == 1)
            {
                break;
            }

            // Inner loop for the second character
            for (int j = 0; j < 256; j++)
            {
                if (pos >= length)
                {
                    break;
                }
                char *input = malloc(3 * 8); // Allocate memory for the input string
                input[0] = (char)i;
                input[1] = (char)j;
                // printf("Current input: %s\n", input);
                unsigned long size = strlen(input);
                unsigned long *encrypted_data = _encryption((void *)input, size);
                char *encrypted_string = malloc((size + 1) / 2 * 16 + 1);
                sprintf(encrypted_string, "%lx", encrypted_data[0]);
                if (strcmp(substring, encrypted_string) == 0)
                {
                    printf("Found: %s\n", input);
                    found = 1;
                }
                free(encrypted_string);
                free(input);
                free(encrypted_data);
                if (found == 1)
                {
                    break;
                }
            }
        }
        pos += 8;
        free(substring);
    }
}

int main(int argc, char *argv[])
{
    const char *input = "te";

    brute_force();
    printf("Input: %s\n", input);
    const char *target = "188d1f2f13cd5b601bd6047f4496ff74496ff74496ff7";
    // const char *input = "te"; //2817c239
    unsigned long size = strlen(input); // Use the length of the input argument
    // Ensure the input is treated correctly based on how _encryption function is expected to work
    unsigned long *encrypted_data = _encryption((void *)input, size);

    // Print each encrypted unsigned long in hexadecimal format
    printf("Encrypted data in hexadecimal format: ");

    // Allocate a string that's large enough to hold the hexadecimal representation
    // Each unsigned long will be up to 16 hexadecimal digits
    char *encrypted_string = malloc((size + 1) / 2 * 16 + 1);

    char *encrypted_test = malloc((size + 1) / 2 * 16 + 1);
    sprintf(encrypted_test, "%s", "2817c239");

    if (encrypted_string == NULL)
    {
        printf("Memory allocation failed\n");
    }

    // Initialize the string to empty
    encrypted_string[0] = '\0';

    // Convert each number to hexadecimal and append it to the string
    for (unsigned long i = 0; i < (size + 1) / 2; i++)
    {
        sprintf(encrypted_string + i * 16, "%16lx", encrypted_data[i]);
        // if (strcmp(encrypted_string, encrypted_test) == 0)
        // {
        //     printf("Found: %s\n", encrypted_string);
        //     break;
        // }
    }

    // Print the final string
    printf("%s\n", encrypted_string);

    for (unsigned long i = 0; i < (size + 1) / 2; i++)
    { // Adjusted loop condition based on encryption function logic
        printf("%lx", encrypted_data[i]);
    }
    printf("\n");

    free(encrypted_data); // Remember to free the allocated memory

    return 0;
}
