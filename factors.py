import sys
from math import isqrt

def factorize(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return i, n // i
    return None

def process_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            n = int(line)
            factors = factorize(n)
            if factors:
                p, q = factors
                print(f"{n} = {p} * {q}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    file_path = sys.argv[1]
    process_file(file_path)

