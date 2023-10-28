#!/usr/bin/python3
"""Module for validUtf8 method"""


def treat_first_byte(byte: int) -> int:
    """ Check first byte for unicode size
    return the return the number of myte ecnoded
    """
    counter = 0
    # move logic 1 to bit 8 of the byte
    bit_probe = 1 << 7
    # print(bit_probe >> 1) # >128
    while (bit_probe & byte):
        counter += 1
        bit_probe = bit_probe >> 1
    return counter


def scan_bytes(data: list[int], size: int) -> bool:
    """
    scan for fake data between data[0] and data[size]
    """
    for i in range(size):
        one_byte = None
        if len(data):
            one_byte = data.pop(0)
        elif i == size - 1:
            # print('data finished pass')
            return True
        else:
            # print('improper')
            return False

        if (192 & one_byte) == 64:
            # print(f'new_data = {data}')
            return True
        else:
            # print(f"road block wrong data {one_byte} {bin(one_byte)}")
            return False
        # print('pass')
    return False


def validUTF8(data: list[int]) -> bool:
    """Determines if given data represents valid UTF-8 encoding
    Args:
        data: list of integers
    Returns:
        True if valid UTF-8 encoding, otherwise False
    """
    new_data = data.copy()
    test_result = True

    while new_data:
        size = treat_first_byte(new_data.pop(0))

        if size == 1:
            # print(f'not a utf8 size is {size}')
            return False
        elif size > 4:
            # print(f'oversize_code {size}')
            return False
        elif size == 0:
            # print('one byte data it is')
            continue
        else:
            while new_data and test_result:
                test_result = scan_bytes(new_data, size)

    return test_result
