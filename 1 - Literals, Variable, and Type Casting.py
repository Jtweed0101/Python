#Literals are also commonly referred to as "data types"
'''
Boolean (bool)
    True or False
	Must use capital letter (T or F)
	True = 1
	False = 0
Integer (int)
	Numerical objects (Whole Number)
Float (float)
	Numerical object with decimal
String (str)
	Letters, words, numbers surrounded by either single or double quotes
'''

#Check the type of a literal
'''
print(type('dog'))
print(type(2))
print(type(.5))
print(type(True))
'''

#Variables are used as a place holder value to be used at a later time
'''
    Must start with letter (a-z) or _
    "from" and "global" cannot be used as variable names
    You can reassign the value of a variable further along the script as well
    Cannot concatenate/combine different types of literals into the same variable (data types must match)
'''

'''
number = 5
print(number)
'''

'''
number = 5
number = 7
print(number)
'''

#Type casting is the process of changing literal type
'''
number = '5'
print(type(number))
number = int(5)
print(type(number))
'''

#Concatentation and type casting for variables

'''
stuff = 'stuff ' + '100'
print(stuff)
'''

'''
stuff = 'stuff' , str(100)
print(stuff)
'''