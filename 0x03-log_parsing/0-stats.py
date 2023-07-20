#!/usr/bin/env python3
"""display stat"""

import sys


def print_stat(status, file_size):
    """print stat"""
    print("File size: {}".format(file_size))
    for key in sorted(status.keys()):
        if status[key] != 0:
            print("{}: {}".format(key, status[key]))


if __name__ == "__main__":
    status = {"200": 0, "301": 0, "400": 0, "401": 0,
              "403": 0, "404": 0, "405": 0, "500": 0}
    file_size = 0
    counter = 0
    try:
        for line in sys.stdin:
            if counter != 0 and counter % 10 == 0:
                print_stat(status, file_size)
            counter += 1
            data = line.split()
            try:
                file_size += int(data[-1])
            except:
                pass
            try:
                status[data[-2]] += 1
            except:
                pass
        print_stat(status, file_size)
    except KeyboardInterrupt:
        print_stat(status, file_size)
        raise
