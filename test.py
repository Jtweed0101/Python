
'''print("We have {0} small boxes, {1} large boxes, {2} medium boxes".format(10,12,12))
'''
###########################################################################
'''
chars = "[[]]"
word = "Cool"

result = chars[0:2] + word + chars[2:]
if result == "[[Cool]]":
    print(result, '\nGreat job!')
else:
    print("Better luck next time")
'''

################################################################################

'''
word1 = "Computer"
word2 = "Truck"

print(word1[1:] + word2[0] + word2[2:])
'''

################################################################################

'''
chars = "<<[]]]" # this could be a very long string with an even length.
word = "Cool"
size = len(chars)
half_of_size = int(size/2)

print(chars[:half_of_size] + word + chars[half_of_size:])
'''

################################################################################

'''my_list = ['b', 'd', 'a', 'z', 'x']
another_list = [1, 2, 3, 4, 5]
my_list.sort(reverse=True)
another_list.sort(reverse=True)
new_list = my_list[2:] + another_list[2:]
print(new_list)'''

################################################################################


'''
my_list = ['a', 'b', 'c', 1, 2, 3, ['apple', 'orange', ['john', 'robert'], 'banana'], 'd']
print(my_list[6][2][1])
'''

################################################################################

'''my_list = ['a', 'b', 'c', 1, 2, 3, ['apple', 'orange', ['john', 'robert'], 'banana'], 'd']
my_list[6][2][1] = 'joe'
print(my_list)'''


################################################################################

'''var = 0
print(var == 0)
var = 1
print(var == 0)'''

################################################################################

'''n = int(input('Enter a number: '))
print(n >= 100)
'''

################################################################################

'''weather = input('How is the weather: good or bad? ')
if weather == 'good':
    print('Go for a walk')
else:
    print('Stay inside')
print('Then have lunch')'''

################################################################################

'''number_1 = int(input("Enter a number: "))
number_2 = int(input("Enter another number: "))

if number_1 > number_2:
    print(number_1, "is larger")
elif number_2 > number_1:
    print(number_2, "is larger")
else:
    print("The numbers are equal")
'''

################################################################################

dict = {'K1': 12, 'K2': 13, 'items': ['potion', {'P1': 'health', 'P2': 'stamina'}]}

print(dict['items'][1]['P2'])





































