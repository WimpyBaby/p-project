"""Module for error handling"""


def get_float_input(text):
    """function for getting float"""
    while True:
        try:
            value = float(input(text))
            if value <= 0:
                print("Please enter a number that is not zero or less than zero")
            else:
                return value
        except ValueError:
            print("Please enter a valid float")


def get_letters_input(text):
    """Function that takes a string as input and returns it if it only contains letters"""
    while True:
        try:
            user_input = input(text)
            # isalpha() hämtat från stackoverflow där isalpha() kollar om det är en bokstav
            if user_input.isalpha():
                return user_input
            else:
                print("\nInvalid input! Please enter only letters.")
        except ValueError:
            print("\nInvalid input! Please enter only letters.\n")


def get_number_input(text):
    """Function that takes a string as input and returns it if it only contains numbers"""
    while True:
        try:
            user_input = input(text)
            # isdigit() hämtat från stackoverflow där isdigit() kollar om det är en siffra
            if user_input.isdigit():
                return user_input
            else:
                print("\nInvalid input! Please enter only numbers.")
        except ValueError:
            print("\nInvalid input! Please enter only numbers.\n")
