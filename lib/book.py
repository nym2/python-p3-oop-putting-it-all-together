#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        # Initialize title and page_count
        self.title = title
        self._page_count = None
        self.page_count = page_count  # This will trigger the setter

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        # Check if the page_count is an integer
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        # Simulate turning the page and print a message
        print("Flipping the page...wow, you read fast!")

    
        