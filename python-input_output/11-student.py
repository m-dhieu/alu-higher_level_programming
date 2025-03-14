#!/usr/bin/python3


"""Class Student that defines a student by first_name, last_name, and age."""


class Student:
    """Class to represent a student."""
    
    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student instance."""
        if attrs is None:
            return {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
            }
        else:
            return {
                    attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)
                    }

    def reload_from_json(self, json):
        """Replace all attributes of Student instance with dictionary values.
        """
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
