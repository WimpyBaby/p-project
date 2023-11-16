"""Code for practicing periodic system numbers, weight and symbol."""

import random


class Element:
    """A class representing an element."""

    def __init__(self, symbol, weight):
        """Initialize an element with symbol and weight."""
        self.symbol = symbol
        self.weight = weight

    def __str__(self):
        """Return a string representation of an element."""
        return f"{self.symbol} {self.weight}"


def element_list():
    """Return a list of elements sorted in a dictionary and by their weight."""

    with open("element.txt", "r", encoding="utf-8") as file:
        element_data = {}

        # Read file line by line
        for line in file:
            # Split line into words
            data = line.strip().split()

            # Ensure that there are two words on the line
            if len(data) == 2:
                symbol = data[0]
                weight = float(data[1])

                element_data[symbol] = weight

        # sorted method derived from stackoverflow
        sorted_element_data = sorted(element_data.items(), key=lambda x: x[1])

        # Create instances of Element class and add them to a list
        elements = [Element(symbol, weight) for symbol, weight in sorted_element_data]

        return elements


element_list = element_list()
element_data = {element.symbol: element.weight for element in element_list}


def show_element():
    """function for showing elements in a dictionary"""
    for i in element_data:
        print(i, element_data[i])


def practice_element_number():
    """Practice periodic system numbers."""
    while True:
        # Generate a random symbol
        random_symbol = random.choice(list(element_data.keys()))

        # Ask user for input
        guess = input(f"Which atomic number does {random_symbol} have? ")

        # if guess ==


practice_element_number()
