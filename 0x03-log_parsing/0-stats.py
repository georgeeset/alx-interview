#!/usr/bin/python3
"""Log Parser"""
import sys
file_count: list = [0]


def print_stats() -> None:
    """
    Print statistics of status_codes
    """
    print('File size: {}'.format(file_count[0]))
    for key in sorted(status_codes.keys()):
        if status_codes[key]:
            print('{}: {}'.format(key, status_codes[key]))


def scan_input_line(line: list) -> None:
    """
    Checks the line for matches
    scan through the string lines
    """
    try:
        my_line = line[:-1]
        line_item = my_line.split(' ')
        file_count[0] += int(line_item[-1])
        status_code = int(line_item[-2])
        if status_code in status_codes:
            status_codes[status_code] += 1
    except BaseException:
        pass


if __name__ == '__main__':
    status_codes: map = {
        200: 0, 301: 0, 400: 0, 401: 0,
        403: 0, 404: 0, 405: 0, 500: 0
        }
    line_count: int = 0

    try:
        for line in sys.stdin:
            scan_input_line(line)
            """ print after every 10 lines """
            if line_count > 0 and line_count % 10 == 0:
                print_stats()
            line_count += 1
    except KeyboardInterrupt:
        print_stats()
        raise
    except Exception as e:
        pass
