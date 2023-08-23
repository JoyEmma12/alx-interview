#!/usr/bin/python3
"""
Method that determines if a given set
represent valid UTF-8 encoding
"""


def validUTF8(data):

    """
    True if data is a valid UTF-8 encoding, else return False
    """

    num_bytes_to_follow = 0

    for byte in data:
        byte = byte & 0xFF  # Keep only the least significant 8 bits

        if num_bytes_to_follow > 0:
            if byte >> 6 == 0b10:
                num_bytes_to_follow -= 1
            else:
                return False  # Invalid continuation byte
        else:
            if byte >> 7 == 0:  # 1-byte character
                num_bytes_to_follow = 0
            elif byte >> 5 == 0b110:  # 2-byte character
                num_bytes_to_follow = 1
            elif byte >> 4 == 0b1110:  # 3-byte character
                num_bytes_to_follow = 2
            elif byte >> 3 == 0b11110:  # 4-byte character
                num_bytes_to_follow = 3
            else:
                return False  # Invalid starting byte

    return num_bytes_to_follow == 0
