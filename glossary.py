#!/usr/local/bin/python3.7

glossary = {
    'tuple': 'A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.',
    'dictionary': 'A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.',
    'list': 'A list is a collection which is ordered and changeable. In Python lists are written with square brackets.',
    'set': 'A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.',
    'variable': 'Variables are containers for storing data values.',
    }

for key in glossary:
    print(key + ":\n\t" + glossary[key] + "\n")
