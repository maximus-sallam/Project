from collections import OrderedDict

glossary = OrderedDict()

glossary['tuple'] = 'A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.'
glossary['dictionary'] = 'A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.'
glossary['list'] = 'A list is a collection which is ordered and changeable. In Python lists are written with square brackets.'
glossary['set'] = 'A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.'
glossary['variable'] = 'Variables are containers for storing data values.'
glossary['indentation'] = 'Where in other programming languages the indentation in code is for readability only, in Python the indentation is very important.'
glossary['comment'] = 'Python has commenting capability for the purpose of in-code documentation.'
glossary['operators'] = 'Operators are used to perform operations on variables and values.'
glossary['while loop'] = 'With the while loop we can execute a set of statements as long as a condition is true.'
glossary['for loop'] = 'A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).'

print("\n")
for key, value in glossary.items():
    print(key.title() + ": " + value)
