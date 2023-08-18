#!/usr/bin/python3
"""
Script that read stdin line by line
and computes metrics
Input format: <IP Address> -
[<date>] "GET /projects/260 HTTP/1.1" <status code>
 <file size> (if the format is not this one, the line must be skipped)
"""
import sys


def print_statistics(total_size, status_codes):
    """
    prints stdin
    """
    print(f"Total file size: File size: {total_size}")
    for code, count in sorted(status_codes.items()):
        print(f"{code}: {count}")


def main():
    total_size = 0
    status_codes = {}

    try:
        line_count = 0
        for line in sys.stdin:
            line = line.strip()
            parts = line.split()

            if len(parts) >= 9:
                try:
                    file_size = int(parts[-1])
                    status_code = int(parts[-2])
                except ValueError:
                    continue

                total_size += file_size

                if status_code in status_codes:
                    status_codes[status_code] += 1
                else:
                    status_codes[status_code] = 1

                line_count += 1

                if line_count % 10 == 0:
                    print_statistics(total_size, status_codes)

    except KeyboardInterrupt:
        pass

    print_statistics(total_size, status_codes)


if __name__ == "__main__":
    main()
