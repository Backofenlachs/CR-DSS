#!/usr/bin/env python3


def get_int():
    while True:
        try:
            return int(input("Enter an integer: "))
        except ValueError:
            print("That's not an integer. Please try again.")

def get_init(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("That's not an integer. Please try again.")  

def main():
    print("Welcome to   the integer input program!")
    num = get_int()
    print(f"You entered: {num}")

if __name__ == "__main__":
    main()