#!/usr/bin/python3
import sys


def factorize(num):
    """Generate 2 factors for a given number."""
    factor1 = 2
    while num % factor1:
        if factor1 * factor1 > num:
            return None, None
        factor1 += 1

    factor2 = num // factor1
    return factor1, factor2


def main():
    if len(sys.argv) != 2:
        sys.exit(f"Wrong usage: {sys.argv[0]} <file_path>")

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as file:
            for line in file:
                num = int(line.strip())
                factor1, factor2 = factorize(num)
                if factor1 is not None:
                    print(f"{num} = {factor1} * {factor2}")
                else:
                    print(f"{num} is a prime number")

    except FileNotFoundError:
        sys.exit(f"File not found: {filename}")
    except Exception as e:
        sys.exit(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
