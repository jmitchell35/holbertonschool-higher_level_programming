#!/usr/bin/env python3
import pickle

class CustomObject:
    def __init__(self, name: str, age: int, is_student: bool):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        for key, value in self.__dict__.items():
            print(f"{key}: {value}")

    def serialize(self, filename):
        with open(filename, mode="wb") as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, mode="rb") as file:
                return pickle.load(file)
        except Exception as e:
            print(f"{e}")
            return None
