#!/usr/bin/env python3
from abc import ABC, abstractmethod

class Book(ABC):
    """abstract class"""
    # @abstractmethod
    
    def __init__(self, title, author, price):
        """doc"""
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        """doc"""
        return "{} by {} - ${}".format(self.title, self.author, self.price)
