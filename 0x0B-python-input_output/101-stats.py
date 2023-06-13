#!/usr/bin/python3
"""Reads stdin line by line and computes metrics"""


import sys
from collections import defaultdict


def print_statistics(file_sizes, status_codes):
    """Prints the statistics on stdout"""
    total_size = sum(file_sizes)
    print(f"File size: {total_size}")

    sorted_status_codes = sorted(status_codes.keys())
    for code in sorted_status_codes:
        count = status_codes[code]
        print(f"{code}: {count}")


def process_input():
    """Processes the user input"""
    file_sizes = []
    status_codes = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            if line:
                # Parse the line and extract relevant information
                parts = line.split()
                file_size = int(parts[-1])
                status_code = parts[-2]
                file_sizes.append(file_size)
                status_codes[status_code] += 1

                line_count += 1

                # Print statistics every 10 lines
                if line_count % 10 == 0:
                    print_statistics(file_sizes, status_codes)

    except KeyboardInterrupt:
        print_statistics(file_sizes, status_codes)


process_input()
