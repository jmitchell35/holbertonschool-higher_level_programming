#!/usr/bin/python3

class CountedIterator:
    def __init__(self, data):
        self.counter = 0
        self.obj = iter(data)
    
    def get_count(self):
        return self.counter
    
    def __next__(self):
        self.counter += 1
        try:
            return next(self.obj)
        except StopIteration:
            self.counter -= 1
            raise