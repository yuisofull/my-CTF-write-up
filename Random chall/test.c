#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

unsigned long* encryption(unsigned long data[], unsigned long size)
{
    unsigned int eax, edx, ecx, byte_address;

    for (byte_address = 0; byte_address < size; byte_address++)
    {
        eax = data[byte_address];
        ecx = eax + 0x11;
        eax += 0xB;
        ecx = eax * ecx;
        edx = ecx;
        edx >>= 8;
        eax = edx;
        eax ^= ecx;
        eax >>= 0x10;
        eax ^= edx;
        eax ^= ecx;
        data[byte_address] = eax;
    }

    return data;
}

unsigned long* _encryption(void* data, unsigned long size)
{
    unsigned long* data_chunk = malloc(size * sizeof(unsigned long));
    unsigned long* result;
    int i;

    if (size & 1) size++;
    memset(data_chunk, 0, size * sizeof(unsigned long));
    for (i = 0; i < size / 2; i++)
        data_chunk[i] = ((unsigned short*)data)[i];

    result = encryption(data_chunk, size / 2);
    return result;
}

int main()
{
    const char* encrypted_str = "188d1f2f13cd5b601bd6047f4496ff74496ff74496ff7";
    const int encrypted_len = strlen(encrypted_str);
    const int max_key_length = 20; // Adjust as needed

    for (int key_length = 3; key_length <= max_key_length; key_length++)
    {
        for (int i = 0; i < pow(26, key_length); i++)
        {
            char key[max_key_length + 1];
            int j;
            for (j = key_length - 1; j >= 0; j--)
            {
                key[j] = 'a' + i % 26;
                i /= 26;
            }
            key[key_length] = '\0';

            unsigned long* encrypted_data = _encryption(encrypted_str, encrypted_len);
            char* decrypted_str = malloc(encrypted_len * sizeof(char) + 1);
            int decrypted_len = 0;

            for (int k = 0; k < encrypted_len / 2; k++)
            {
                unsigned short decrypted_word = (encrypted_data[k] ^ strtol(key, NULL, 16)) & 0xffff;
                decrypted_str[decrypted_len++] = decrypted_word >> 8;
                decrypted_str[decrypted_len++] = decrypted_word & 0xff;
            }

            decrypted_str[decrypted_len] = '\0';
            free(encrypted_data);

            if (strstr(decrypted_str, key) != NULL)
            {
                printf("Possible original text: %s\n", decrypted_str);
                printf("Possible key: %s\n", key);
                return 0;
            }

            free(decrypted_str);
        }
    }

    printf("No match found.\n");
    return 1;
}