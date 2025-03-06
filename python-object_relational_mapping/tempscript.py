#!/usr/bin/python3
'''Script to debug failed execution'''
import sys
import importlib.util

print("Python executable:", sys.executable)
print("\nPython path:")
for path in sys.path:
    print(path)

print("\nTrying to locate MySQLdb:")
spec = importlib.util.find_spec('MySQLdb')
print("MySQLdb spec:", spec)