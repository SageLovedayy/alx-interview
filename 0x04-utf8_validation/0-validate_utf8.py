#!/usr/bin/python3

"""
This function determines if a given data set represents a valid UTF-8 encoding
returns True if valid UTF_8 encoding, False otherwise.

Implementation
- Handle only the 8 LSBs of each integer (1111111 i.e 0xFF)
- Determine the number of bytes in the sequence using the first byte, return false if first byte is invalid
- Loop over coninuation bytes and check for enough bytes left in the list to
complete the character sequence
- Validate coninuation bytes (also check onlly the 8 LSBs) to be sure they
match the format 10xxxxxx
"""
def validUTF8(data):
    i = 0
    while i < len(data):
        # return the 8 least significant bits
        byte = data[i] & 0xFF
        # detemine no of bytes in sequence using the first character
        if byte >> 7 == 0:
            num_bytes = 1
        elif byte >> 5 == 0b110:
            num_bytes = 2
        elif byte >> 4 == 0b1110:
            num_bytes = 3
        elif byte >> 3 == 0b11110:
            num_bytes = 4
        else:
            return False

       # check continuation byte
        for j in range(1, num_bytes):
            if i + j >= len(data):
                return False # not enough bytes for current character

            # validate sequence in next byte using 8LSBs
            next_byte = data[i + j] & 0xFF
            if next_byte >> 6 != 0b10:
                return False

        i += num_bytes

    return True

    

    

