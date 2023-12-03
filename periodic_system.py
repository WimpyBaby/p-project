"""Code for practicing periodic system numbers, weight and symbol."""

from dataclasses import dataclass
from enum import Enum
import random
import sys
import tkinter as tk
import error_handling as eh


# Dataclass for elements in the periodic table
@dataclass
class Element:
    """A class for elements in the periodic table."""

    symbol: str
    weight: float
    number: int
    row: int
    column: int

    def __str__(self):
        """Return a string representation of an element."""
        return f"{self.symbol} {self.weight} {self.number} {self.row} {self.column}"


class PeriodicTableReader:
    """A class for reading a periodic table file."""

    def __init__(self, file_path):
        self.file_path = file_path
        self.element_dict = self._create_element_dict()
        self.sorted_element_dict = self._sorted_element_dict()

    # create a dictionary of elements from the file
    def _create_element_dict(self):
        element_dict = {}
        with open(self.file_path, "r", encoding="utf-8") as file:
            for line in file:
                data = line.strip().split()

                # Instances of Element class are created and added to element_dict
                if len(data) == 5:
                    symbol, weight, number, row, column = data
                    element = Element(
                        symbol, float(weight), int(number), int(row), int(column)
                    )
                    element_dict[symbol] = element
        return element_dict

    def _sorted_element_dict(self):
        """Return a sorted element dictionary."""
        # Sort the element dictionary by weight
        return sorted(self.element_dict.values(), key=lambda elem: elem.weight)

    def show_element(self):
        """function for showing elements in a dictionary"""
        print(
            "\nSymbol         Weight          Number          Row             Column\n"
        )
        # Print the sorted element dictionary
        for element in self._sorted_element_dict():
            print(
                f"{element.symbol:<15} {element.weight:<15} {element.number:<15} {element.row:<15} {element.column:<15}"
            )


class PracticePeriodicTable:
    """A class for practicing periodic table."""

    # Max attempt for each practice type
    MAX_ATTEMPT = 3

    def __init__(self, element_dict):
        self.element_dict = element_dict
        self.total_attempt = 0

    def get_max_attempt(self):
        """Return max attempt."""
        # Return max attempt
        return self.MAX_ATTEMPT

    def get_total_attempt(self):
        """Return total attempt."""
        # Return total attempt
        return self.total_attempt

    def increment_total_attempt(self):
        """Increment total attempt by 1."""
        # Increment total attempt by 1 each time the user guesses wrong
        self.total_attempt += 1

    def generate_random_symbol(self):
        """Generate a random symbol."""
        # Return a random symbol from element_dict
        return random.choice(list(self.element_dict.keys()))

    def practice_element_number(self):
        """Practice periodic system numbers."""

        # Generate a random symbol and retrieve the number from element_dict
        generated_symbol = self.generate_random_symbol()
        generated_number = self.element_dict[generated_symbol].number

        # Debugging print statements
        print(
            f"\n{generated_symbol} {self.element_dict[generated_symbol].weight} {generated_number}"
        )

        # Asking the user to input their guess
        while True:
            # Ask user for input
            guess = eh.get_number_input(
                f"\nWhich atomic number does {generated_symbol} have? "
            )

            # Check if guess is equal to generated_number
            if int(guess) == self.element_dict[generated_symbol].number:
                print("Correct!")
                break

            # If guess is incorrect increment total_attempt by 1
            self.increment_total_attempt()

            print(
                f"Wrong! you have {self.get_max_attempt() - self.get_total_attempt()} attempts left"
            )

            # If total_attempt is equal to 3 print the correct answer and reset total_attempt to 0
            if self.get_total_attempt() == self.get_max_attempt():
                print(
                    f"\nThe correct answer is {self.element_dict[generated_symbol].number}"
                )
                self.total_attempt = 0
                break

    def practice_element_symbol(self):
        """Practice periodic system symbols."""

        # Generate a random symbol and element from element_dict
        generated_symbol = self.generate_random_symbol()
        generated_element = self.element_dict[generated_symbol]

        # Debugging print statements
        print(
            f"\n{generated_symbol} {generated_element.weight} {generated_element.number}"
        )

        while True:
            # Ask user for input
            guess = eh.get_letters_input(
                f"\nWhich symbol does the atomic number {generated_element.number} have? "
            )
            # Check if guess is equal to generated_symbol
            if guess.casefold() == generated_symbol.casefold():
                print("Correct!")
                break

            # If guess is not equal to generated_symbol
            self.increment_total_attempt()
            print(
                f"Wrong! You have {self.get_max_attempt() - self.get_total_attempt()} attempts left"
            )

            # If total_attempt is equal to 3
            if self.get_total_attempt() == self.get_max_attempt():
                print(f"\nSorry, the correct answer is {generated_symbol}")
                self.total_attempt = 0
                break

    def practice_element_weight(self):
        """Practice periodic system weights."""

        # Generate a random symbol and weight from element_dict
        generated_symbol = self.generate_random_symbol()
        generated_weight = self.element_dict[generated_symbol].weight

        # Extracting random elements from element_dict as alternatives
        random_symbols = random.sample(list(self.element_dict.keys()), 2)
        random_weights = [
            self.element_dict[symbol].weight for symbol in random_symbols
        ] + [generated_weight]

        # Shuffle the list of random_weights
        random.shuffle(random_weights)

        # Debugging print statements
        print(
            f"Generated symbol: {generated_symbol} {self.element_dict[generated_symbol].weight}\n"
        )

        # Printing the shuffled weights
        print(
            f"What is the correct weight for the element {generated_symbol}?: \n{random_weights}\n"
        )

        # Asking the user to input their choice
        while True:
            user_choice = eh.get_float_input(
                ("Which weight do you think is correct? Enter the weight: ")
            )

            # Check if choice is in weights list
            if user_choice in random_weights:
                # Check if choice is equal to weights and print correct or wrong
                if user_choice == generated_weight:
                    print("\nCorrect!\n")
                    break
                print(f"\nWrong! The correct answer is {generated_weight}\n")
                break
            print("\nInvalid input! Please enter a valid alternative.\n")


def create_periodic_table(root, element_dict):
    """Create a periodic table using tkinter."""

    # list for storing wrong buttons and placed symbols
    wrong_buttons = []
    placed_symbols = []

    # Create a label for the symbol to find and choose a random symbol
    symbol_label = tk.Label(root, font=("", 20))
    symbol_label.grid(row=0, column=0, columnspan=18, pady=5, padx=5)
    generated_symbol = random.choice(list(element_dict.keys()))

    def print_row_col(element_row, element_col):
        nonlocal generated_symbol, wrong_buttons

        # retrieve column and row the button that was clicked
        button = root.grid_slaves(row=element_row, column=element_col)[0]

        # retrieve column and row of the generated symbol
        element_row_col = (
            element_dict[generated_symbol]["row"],
            element_dict[generated_symbol]["column"],
        )

        # if the button that was clicked has same row and column as the generated symbol
        if (element_row, element_col) == element_row_col:
            button.config(bg="green")

            # wrong buttons are set to default color and the list is cleared after correct answer
            for wrong_button in wrong_buttons:
                wrong_button.config(bg="SystemButtonFace")
            wrong_buttons = []

            # remaining symbols are symbols that are not placed
            remaining_symbols = [
                symbol for symbol in element_dict.keys() if symbol != placed_symbols
            ]

            # if remaining symbols, a new symbol is chosen
            if remaining_symbols:
                generated_symbol = random.choice(remaining_symbols)

            # new generated symbol is used as label
            symbol_label.config(text=f"Find: {generated_symbol}")

            # if all symbols are placed, the user is congratulated and the program is exited
            if len(placed_symbols) == len(element_dict):
                print("Congratulations! You have placed all symbols!")
                sys.exit()

        # wrong buttons are set to red and the button that was clicked is added to wrong buttons
        else:
            button.config(bg="red")
            wrong_buttons.append(button)

    # loop through element_dict and create buttons for each element
    for symbol, data in element_dict.items():
        # placed symbols are added to placed_symbols
        row, col = data.row, data.column

        # if the symbol is placed, the button is disabled
        button = tk.Button(
            root, text=data.number, borderwidth=1, relief="solid", width=5, height=2
        )

        # Create a button for each element in the shape of the periodic table
        button.grid(row=row, column=col, padx=2, pady=2)
        button.config(command=lambda r=row, c=col: print_row_col(r, c))

    # new generated symbol is used as label
    symbol_label.config(text=f"Find: {generated_symbol}")


class MenuOption(Enum):
    """Enum for practice type."""

    # Enum for menu options
    SHOW_ELEMENTS = 1
    PRACTICE_ELEMENT_NUMBER = 2
    PRACTICE_ELEMENT_SYMBOL = 3
    PRACTICE_ELEMENT_WEIGHT = 4
    PRACTICE_PERIODIC_TABLE = 5
    EXIT = 6


def displaymenu(reader, practice_table_instance):
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

    # Asking the user to input their choice
    while True:
        user_input = eh.get_number_input("Please enter your choice: ")

        # Check if user_input is a valid menu option and break the loop if it is
        try:
            menu_option = MenuOption(int(user_input))
            break
        except ValueError:
            print("Invalid input! Please enter a valid choice.")

    # Check which menu option the user chose and call the corresponding function
    if menu_option == MenuOption.SHOW_ELEMENTS:
        reader.show_element()
    elif menu_option == MenuOption.PRACTICE_ELEMENT_NUMBER:
        practice_table_instance.practice_element_number()
    elif menu_option == MenuOption.PRACTICE_ELEMENT_SYMBOL:
        practice_table_instance.practice_element_symbol()
    elif menu_option == MenuOption.PRACTICE_ELEMENT_WEIGHT:
        practice_table_instance.practice_element_weight()
    elif menu_option == MenuOption.PRACTICE_PERIODIC_TABLE:
        root = tk.Tk()
        root.title("Periodic Table")
        create_periodic_table(root, reader.element_dict)
        root.mainloop()
    elif menu_option == MenuOption.EXIT:
        sys.exit()


def main():
    """Main function to run the periodic system."""

    # Create an instance of PeriodicTableReader and PracticePeriodicTable classes
    elements_data = "element.txt"
    reader = PeriodicTableReader(elements_data)
    practice_table_instance = PracticePeriodicTable(reader.element_dict)

    while True:
        displaymenu(reader, practice_table_instance)


# Main program starts here with instance of PeriodicTableReader
if __name__ == "__main__":
    main()
