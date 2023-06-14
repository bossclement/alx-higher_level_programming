#!/usr/bin/python3
"""Reads stdin line by line and computes metrics"""


import sys


total_size = 0
status_counts = {}

try:
    for i, line in enumerate(sys.stdin, start=1):
        fields = line.split()

        file_size = int(fields[-1])
        status_code = int(fields[-2])

        total_size += file_size

        if status_code in status_counts:
            status_counts[status_code] += 1
        else:
            status_counts[status_code] = 1

        if i % 10 == 0:
            print("File size: {}".format(total_size))
            for code in sorted(status_counts.keys()):
                print("{}: {}".format(code, status_counts[code]))

except KeyboardInterrupt:
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        print("{}: {}".format(code, status_counts[code]))
