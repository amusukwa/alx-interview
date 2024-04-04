#!/usr/bin/python3
"""
UTF-8 Validation file
"""


def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    bytes_to_follow = 0
    
    for num in data:
        if bytes_to_follow == 0:
            # Count the number of bytes to follow based on the first few bits
            if num >> 7 == 0:  # 1 byte character
                bytes_to_follow = 0
            elif num >> 5 == 0b110:  # 2 bytes character
                bytes_to_follow = 1
            elif num >> 4 == 0b1110:  # 3 bytes character
                bytes_to_follow = 2
            elif num >> 3 == 0b11110:  # 4 bytes character
                bytes_to_follow = 3
            else:
                return False  # Invalid start byte for UTF-8 character
        else:
            if num >> 6 != 0b10:
                return False  # Subsequent bytes must start with '10'
            bytes_to_follow -= 1

    return bytes_to_follow == 0
