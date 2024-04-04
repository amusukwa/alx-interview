#!/usr/bin/python3
"""
UTF-8 Validation file
"""


def validUTF8(data):
    # Variable to keep track of the number of bytes in the current character
    num_bytes = 0

    # Iterate through each integer in the data list
    for num in data:
        # If num_bytes is 0, it means we are at the start of a new character
        if num_bytes == 0:
            # Calculate the number of bytes in the current character based on the first few bits
            if num >> 7 == 0b0:
                num_bytes = 1
            elif num >> 5 == 0b110:
                num_bytes = 2
            elif num >> 4 == 0b1110:
                num_bytes = 3
            elif num >> 3 == 0b11110:
                num_bytes = 4
            else:
                return False

            if num_bytes == 1:
                continue

            num_bytes -= 1

        else:
            if not (num >> 6 == 0b10):
                return False

            # Decrement the number of bytes to process in the sequence
            num_bytes -= 1

    # If all bytes are processed and num_bytes is 0, it's a valid UTF-8 encoding
    return num_bytes == 0

