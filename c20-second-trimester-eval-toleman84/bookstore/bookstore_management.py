#!/usr/bin/env python3
from abc import ABC, abstractmethod
import json


class Book(ABC):
    """abstract class"""
    def __init__(self, title, author, price):
        """doc"""
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        """doc"""
        return "{} by {} - ${}".format(self.title, self.author, self.price)

    @abstractmethod
    def to_dict(self) -> dict:
        """doc"""
        return {
            "title": self.title,
            "author": self.author,
            "price": self.price
        }

    def save_book_data(book_obj: Book) -> None:
        """doc"""
        book_dict = book_obj.to_dict()

        with open(f"{book_obj.title}_{book_obj.author}.json", "w") as f:
            return json.dump(book_dict, f)

    def load_book_data(title: str, author: str) -> Book:
        """doc"""
        with open(f"{title}_{author}.json", "r") as f:
            return json.load(f)
