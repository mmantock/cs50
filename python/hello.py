#!/usr/bin/env python3
"""A tiny test program — prints a greeting and does a small calculation."""


def main():
    name = "Michael"
    total = sum(range(1, 11))  # 1 + 2 + ... + 10
    print(f"Hello, {name}! The sum of 1 to 10 is {total}.")


if __name__ == "__main__":
    main()
