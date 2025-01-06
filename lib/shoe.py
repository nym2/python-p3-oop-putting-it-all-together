#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        # Initialize brand and size
        self.brand = brand
        self._size = None
        self.size = size  # This will trigger the setter

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        # Check if the size is an integer
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    def cobble(self):
        # Repair the shoe and set the condition to 'New'
        self.condition = "New"
        print("Your shoe is as good as new!")
