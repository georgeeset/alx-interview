#!/usr/bin/python3
"""Module for validUtf8 method"""


def validUTF8(data):
    """Determines if given data represents valid UTF-8 encoding
    Args:
        data: list of integers
    Returns:
        True if valid UTF-8 encoding, otherwise False
    """

    # print(bin(43))
    n_bytes = 0

    sample1 = 1 << 7
    sample2 = 1 << 6
    for byte in data:

        # Get the number of set most significant bits in the byte if
        # this is the starting byte of an UTF-8 character.
        mask = 1 << 7
        if n_bytes == 0:
            while mask & byte:
                n_bytes += 1
                mask = mask >> 1

            # 1 byte characters
            if n_bytes == 0:
                continue

            # Invalid scenarios according to the rules of the problem.
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # If this byte is a part of an existing UTF-8 character, then we
            # simply have to look at the two most significant bits and we make
            # use of the masks we defined before.
            if not (byte & sample1 and not (byte & sample2)):
                return False
        n_bytes -= 1
    return n_bytes == 0
