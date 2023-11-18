"""Code for practicing periodic system numbers, weight and symbol."""

import random
import sys


class Element:
    """A class representing an element."""

    def __init__(self, symbol, weight, number):
        """Initialize an element with symbol and weight."""
        self.symbol = symbol
        self.weight = weight
        self.number = number

    def __str__(self):
        """Return a string representation of an element."""
        return f"{self.symbol} {self.weight} {self.number}"


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


def element_list():
    """Return a list of elements sorted by their weight."""
    with open("element.txt", "r", encoding="utf-8") as file:
        element_dict = {}

        for line in file:
            data = line.strip().split()

            if len(data) == 3:
                symbol = data[0]
                weight = float(data[1])
                number = int(data[2])

                # Store symbol as key with a dictionary containing weight and number as value
                element_dict[symbol] = {
                    "symbol": symbol,
                    "weight": weight,
                    "number": number,
                }

        # Sort elements based on their weight
        sorted_elements_data = sorted(element_dict.values(), key=lambda x: x["weight"])

        # Create instances of Element class and add them to a list
        elements = [
            Element(data["symbol"], data["weight"], data["number"])
            for data in sorted_elements_data
        ]

        return elements


element_list = element_list()
element_dict = {
    element.symbol: {"weight": element.weight, "number": element.number}
    for element in element_list
}


def show_element():
    """function for showing elements in a dictionary"""
    for symbol, data in element_dict.items():
        print(f"{symbol:<15} {data['weight']:<15} {data['number']:<15}")


def practice_element_number():
    """Practice periodic system numbers."""

    attempt = 3
    total_attempt = 0

    # Generate a random symbol
    random_element = random.choice(element_list)
    print(f"\n{random_element.symbol} {random_element.weight} {random_element.number}")

    while True:
        # Generate a random symbol

        # Ask user for input
        guess = get_number_input(
            f"\nWhich atomic number does {random_element.symbol} have? "
        )

        if guess == random_element.number:
            print("Correct!")
            break

        total_attempt += 1
        print(f"Wrong! you have {attempt - total_attempt} attempts left")

        if total_attempt == 3:
            print(
                f"\nSorry, the correct answer is {element_dict[random_element.symbol]['number']}"
            )
            break


def practice_element_symbol():
    """Practice periodic system symbols."""

    attempt = 3
    total_attempt = 0

    # Generate a random element
    random_element = random.choice(element_list)
    print(f"\n{random_element.symbol} {random_element.weight} {random_element.number}")

    while True:
        # Ask user for input
        guess = get_letters_input(f"\nWhich symbol does {random_element.number} have? ")

        if guess.casefold() == random_element.symbol.casefold():
            print("Correct!")
            break

        total_attempt += 1
        print(f"Wrong! You have {attempt - total_attempt} attempts left")

        if total_attempt == 3:
            print(f"\nSorry, the correct answer is {random_element.symbol}")
            break


def displaymenu():
    """Menu for periodic system."""
    print("\n---------------MENU---------------")
    print("Welcome to the periodic system!\n")
    print("1. Show elements")
    print("2. Practice element number")
    print("3. Practice Symbol")
    print("4. Exit")
    print("----------------------------------")
    user_input = get_number_input("Please enter your choice: ")

    if user_input == "1":
        show_element()
    elif user_input == "2":
        practice_element_number()
    elif user_input == "3":
        practice_element_symbol()
    elif user_input == "4":
        sys.exit()
    else:
        print("Invalid input! Please enter a number between 1-4.")


def main():
    """Main function."""
    while True:
        displaymenu()


if __name__ == "__main__":
    main()
