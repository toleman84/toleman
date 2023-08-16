#!/usr/bin/env python3
from bookstore_management import Book


class Fiction(Book):
    """doc"""
    def __init__(self, title, author, price, genre):
        """doc"""
        super().__init__(title, author, price)
        self.genre = genre

    def __str__(self):
        """doc"""
        return "{} by {} - ${} - Genre: {}".format(self.title, self.author, self.price, self.genre)

class NonFiction(Book):
    """doc"""
    def __init__(self, subject):
        """doc"""
        self.subject = subject

    def __str__(self):
        """doc"""
        return "{} by {} - ${}".format(self.title, self.author, self.price)

class Textbook(Book):
    """doc"""
    def __init__(self, course_name):
        """doc"""
        self.course_name = course_name

    def __str__(self):
        """doc"""
        return "{} by {} - ${}".format(self.title, self.author, self.price)
