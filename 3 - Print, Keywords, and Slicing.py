
#More about Print w/ Keywords
#\n will print a new line
'''
print('This is some Python')
print('This is some\n Python')
print('This is some\nPython')
'''

#Double quote vs. Single quote vs. \
#\ is called an escape and anything directly to the right of it will be ignored
'''
print('I am a coder')
print("I'm a coder")
print('I\'m a coder')
'''

#Slicing and Indexing
#From left to right, always starts with 0, from right to left starts with -1
'''
variable = 'this is a string'
print(variable)
print(variable[:])
print(variable[0])
print(variable[1])
print(variable[-1])
'''
#Print a range of values
'''
variable = 'this is a string'
print(variable[0:4])
print(variable[::2]
'''
#Print every 2 value
'''
variable = 'this is a string'
print(variable[::2])
'''
#Keywords
#End keyword will negate the new line and put whatever value you specify
'''
variable = 'this is a string'
print(variable, end='.')
variable = 'this is a string'
print(variable, end='!')
'''
#Sep keyword will separate values (in this case variables) with whatever value you specify
'''
variable = 'this is a string'
variable2 = 99
print(variable, variable2, sep='-', end='!')
'''
#Basic Methods
'''
variable = 'this is a string'
print(variable.upper())
'''