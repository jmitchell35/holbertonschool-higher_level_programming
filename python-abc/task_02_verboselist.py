#!/usr/bin/env python3

class VerboseList(list):
    def append(self, value):
        super().append(value)
        print(f"Added [{value}] to the list.")
        
    def extend(self, iterable):
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")
    
    def remove(self, value):
        print(f"Removed [{value}] from the list.")
        super().remove(value)
    
    def pop(self, index=None):
        if index == None:
            index = len(self) - 1
        print(f"Popped [{self[index]}] from the list.")
        super().pop(index)