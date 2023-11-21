"""Code for practicing periodic system numbers, weight and symbol."""

import random
import sys
import tkinter as tk
from dataclasses import dataclass


@dataclass
class Element:
    """A class representing an element."""

    symbol: str
    weight: float
    number: int
    row: int
    column: int

    def __str__(self):
        """Return a string representation of an element."""
        return f"{self.symbol} {self.weight} {self.number} {self.row} {self.column}"


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


def element_list():
    """Return a list of elements sorted by their weight."""
    with open("element.txt", "r", encoding="utf-8") as file:
        element_dict = {}

        for line in file:
            data = line.strip().split()

            if len(data) == 5:
                symbol = data[0]
                weight = float(data[1])
                number = int(data[2])
                row = int(data[3])
                column = int(data[4])

                # Store symbol as key with a dictionary containing weight and number as value
                element_dict[symbol] = {
                    "symbol": symbol,
                    "weight": weight,
                    "number": number,
                    "row": row,
                    "column": column,
                }

        # Sort elements based on their weight
        sorted_elements_data = sorted(element_dict.values(), key=lambda x: x["weight"])

        # Create instances of Element class and add them to a list
        elements = [
            Element(
                data["symbol"],
                data["weight"],
                data["number"],
                data["row"],
                data["column"],
            )
            for data in sorted_elements_data
        ]

        return elements


element_list = element_list()
element_dict = {
    element.symbol: {
        "weight": element.weight,
        "number": element.number,
        "row": element.row,
        "column": element.column,
    }
    for element in element_list
}


def show_element():
    """function for showing elements in a dictionary"""
    print("\nSymbol         Weight          Number          Row             Column\n")
    for symbol, data in element_dict.items():
        print(
            f"{symbol:<15} {data['weight']:<15} {data['number']:<15} {data['row']:<15} {data['column']:<15}"
        )


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

        if int(guess) == random_element.number:
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


def practice_element_weight(element_dict):
    """Practice periodic system weight."""

    # Extracting a random element from element_list as the correct weight
    correct_weight = random.choice(element_list)
    print(f"\n{correct_weight.symbol} {correct_weight.weight} {correct_weight.number}")

    # Extracting random weights from element_dict as alternatives
    random_elements = random.sample(list(element_dict.keys()), 2)
    random_weights = [
        element_dict[element]["weight"]
        for element in random_elements + [correct_weight.symbol]
    ]

    # Shuffling the order of the weights
    random.shuffle(random_weights)

    # Printing the shuffled weights
    print(
        f"What is the correct weight for {correct_weight.symbol}?: \n{random_weights}\n"
    )

    # Asking the user to input their choice
    while True:
        user_choice = get_float_input(
            "Which weight do you think is correct? Enter the weight: "
        )

        if user_choice in random_weights:
            if user_choice == correct_weight.weight:
                print("\nCorrect!\n")
                break
            print(f"\nWrong! The correct answer is {correct_weight.weight}\n")
            break
        print("\nInvalid input! Please enter a valid alternative.\n")


def create_periodic_table(root, elements):
    """Create a periodic table."""

    wrong_buttons = []  # List to store wrong pressed buttons
    placed_elements = []  # List to store elements that have been placed

    random_element = random.choice(elements)
    print(
        f"\n{random_element.symbol} {random_element.weight} {random_element.number} {random_element.row} {random_element.column}"
    )

    def print_row_col(element_row, element_col):
        """Print row and column."""
        nonlocal random_element, wrong_buttons

        print(f"Row: {element_row}, Column: {element_col}")
        button = root.grid_slaves(row=element_row, column=element_col)[0]

        if element_row == random_element.row and element_col == random_element.column:
            print("Correct!")
            button.config(bg="green")

            # Reset color of wrong buttons
            for wrong_button in wrong_buttons:
                wrong_button.config(bg="SystemButtonFace")
            wrong_buttons = []  # Reset the list of wrong buttons

            # Generate a new random element that has not been placed
            random_element = random.choice(
                [e for e in elements if e not in placed_elements]
            )
            print(
                f"\n{random_element.symbol} {random_element.weight} {random_element.number} {random_element.row} {random_element.column}"
            )

            symbol_label = tk.Label(
                root, text=f"Find: {random_element.symbol}", font=("", 20)
            )
            symbol_label.grid(row=0, column=0, columnspan=18, pady=5, padx=5)
        else:
            print("Wrong!")
            button.config(bg="red")  # Change color of wrong button
            wrong_buttons.append(button)  # Add wrong button to the list

    symbol_label = tk.Label(root, text=f"Find: {random_element.symbol}", font=("", 20))
    symbol_label.grid(row=0, column=0, columnspan=18, pady=5, padx=5)

    for element in elements:  # Loop through all elements and create periodic table
        row = element.row
        col = element.column

        button = tk.Button(
            root, text=element.symbol, borderwidth=1, relief="solid", width=5, height=2
        )
        button.grid(row=row, column=col, padx=2, pady=2)

        button.config(command=lambda r=row, c=col: print_row_col(r, c))


def displaymenu():
    """Menu for periodic system."""
    print("\n---------------MENU---------------")
    print("Welcome to the periodic system!\n")
    print("1. Show elements")
    print("2. Practice element number")
    print("3. Practice element Symbol")
    print("4. Practice element weight")
    print("5. Practice periodic table")
    print("6. Exit")
    print("----------------------------------")
    user_input = get_number_input("Please enter your choice: ")

    if user_input == "1":
        show_element()
    elif user_input == "2":
        practice_element_number()
    elif user_input == "3":
        practice_element_symbol()
    elif user_input == "4":
        practice_element_weight(element_dict)
    elif user_input == "5":
        root = tk.Tk()
        root.title("Periodic Table")
        create_periodic_table(root, element_list)
        root.mainloop()
    elif user_input == "6":
        sys.exit()
    else:
        print("Invalid input! Please enter a number between 1-5.")


def main():
    """Main function."""
    while True:
        displaymenu()


if __name__ == "__main__":
    main()
