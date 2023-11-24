"""Code for practicing periodic system numbers, weight and symbol."""

from dataclasses import dataclass
import random
import sys
import tkinter as tk
import error_handling as eh


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


class PeriodicTableReader:
    """A class for reading a periodic table file."""

    def __init__(self, file_path):
        self.file_path = file_path
        self.element_dict = self._create_element_dict()

    def __str__(self):
        """Return a string representation of the PeriodicTableReader."""
        return f"{self.file_path} {self.element_dict}"

    def _create_element_dict(self):
        element_dict = {}
        with open(self.file_path, "r", encoding="utf-8") as file:
            for line in file:
                data = line.strip().split()

                if len(data) == 5:
                    symbol, weight, number, row, column = data
                    element_dict[symbol] = {
                        "weight": float(weight),
                        "number": int(number),
                        "row": int(row),
                        "column": int(column),
                    }
        return element_dict

    def show_element(self):
        """function for showing elements in a dictionary"""
        print(
            "\nSymbol         Weight          Number          Row             Column\n"
        )
        for symbol, data in self.element_dict.items():
            print(
                f"{symbol:<15} {data['weight']:<15} {data['number']:<15} {data['row']:<15} {data['column']:<15}"
            )


class PracticePeriodicTable:
    """A class for practicing periodic table."""

    def __init__(self, element_dict):
        self.element_dict = element_dict

    def practice_element_number(self):
        """Practice periodic system numbers."""

        attempt = 3
        total_attempt = 0

        # Generate a random symbol
        generated_symbol = random.choice(list(self.element_dict.keys()))
        generated_number = self.element_dict[generated_symbol]["number"]

        # Debugging print statements
        print(
            f"\n{generated_symbol} {self.element_dict[generated_symbol]['weight']} {generated_number}"
        )

        while True:
            # Ask user for input
            guess = eh.get_number_input(
                f"\nWhich atomic number does {generated_symbol} have? "
            )

            # Check if guess is equal to generated_number
            if int(guess) == self.element_dict[generated_symbol]["number"]:
                print("Correct!")
                break

            total_attempt += 1
            print(f"Wrong! you have {attempt - total_attempt} attempts left")

            if total_attempt == 3:
                print(
                    f"\nSorry, the correct answer is {self.element_dict[generated_symbol]['number']}"
                )
                break

    def practice_element_symbol(self):
        """Practice periodic system symbols."""

        # Set attempt and total_attempt to 0
        attempt = 3
        total_attempt = 0

        # Generate a random symbol and element from element_dict
        generated_symbol = random.choice(list(self.element_dict.keys()))
        generated_element = self.element_dict[generated_symbol]

        # Debugging print statements
        print(
            f"\n{generated_symbol} {generated_element['weight']} {generated_element['number']}"
        )

        while True:
            # Ask user for input
            guess = eh.get_letters_input(
                f"\nWhich symbol does {generated_element['number']} have? "
            )
            # Check if guess is equal to generated_symbol
            if guess.casefold() == generated_symbol.casefold():
                print("Correct!")
                break

            # If guess is not equal to generated_symbol
            total_attempt += 1
            print(f"Wrong! You have {attempt - total_attempt} attempts left")

            # If total_attempt is equal to 3
            if total_attempt == 3:
                print(f"\nSorry, the correct answer is {generated_symbol}")
                break

    def practice_element_weight(self):
        """Practice periodic system weights."""
        # Extracting a random element from element_dict as the correct weight
        generated_symbol = random.choice(list(self.element_dict.keys()))
        generated_weight = self.element_dict[generated_symbol]["weight"]

        # Extracting random elements from element_dict as alternatives
        random_symbols = random.sample(list(self.element_dict.keys()), 2)
        random_weights = [
            self.element_dict[symbol]["weight"] for symbol in random_symbols
        ] + [generated_weight]

        # Shuffling the order of the weights
        random.shuffle(random_weights)

        # Debugging print statements
        print(
            f"Generated symbol: {generated_symbol} {self.element_dict[generated_symbol]['weight']}\n"
        )

        # Printing the shuffled weights
        print(
            f"What is the correct weight for {generated_symbol}?: \n{random_weights}\n"
        )

        # Asking the user to input their choice
        while True:
            user_choice = eh.get_float_input(
                ("Which weight do you think is correct? Enter the weight: ")
            )

            if user_choice in random_weights:
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

    for symbol, data in element_dict.items():
        row, col = data["row"], data["column"]

        button = tk.Button(
            root, text=data["number"], borderwidth=1, relief="solid", width=5, height=2
        )
        button.grid(row=row, column=col, padx=2, pady=2)
        button.config(command=lambda r=row, c=col: print_row_col(r, c))

    symbol_label.config(text=f"Find: {generated_symbol}")


ELEMENTS_DATA = "element.txt"
reader = PeriodicTableReader(ELEMENTS_DATA)

practice_table_instance = PracticePeriodicTable(reader.element_dict)


def displaymenu(element_dict):
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
    user_input = eh.get_number_input("Please enter your choice: ")

    if user_input == "1":
        reader.show_element()
    elif user_input == "2":
        practice_table_instance.practice_element_number()
    elif user_input == "3":
        practice_table_instance.practice_element_symbol()
    elif user_input == "4":
        practice_table_instance.practice_element_weight()
    elif user_input == "5":
        root = tk.Tk()
        root.title("Periodic Table")
        create_periodic_table(root, element_dict)
        root.mainloop()
    elif user_input == "6":
        sys.exit()
    else:
        print("Invalid input! Please enter a number between 1-5.")


def main(element_dict):
    """Main function to run the periodic system."""

    while True:
        displaymenu(element_dict)


# Main program starts here with instance of PeriodicTableReader
if __name__ == "__main__":
    main(reader.element_dict)
