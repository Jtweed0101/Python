#Lists
'''
cities = ['St. Louis', 'Chicago', 'Austin', 'New York City']
print(cities)
'''

#Print lists alphabetically (ascending) - does not change the index values
'''
cities = ['St. Louis', 'Chicago', 'Austin', 'New York City']
print(sorted(cities))
'''

#Print lists alphabetically (decending) - does not change the index values
'''
cities = ['St. Louis', 'Chicago', 'Austin', 'New York City']
print(sorted(cities, reverse=True))
'''

#Indexing
'''
cities = ['St. Louis', 'Chicago', 'Austin', 'New York City']
print(cities[0])
print(cities[3])
print(cities[-1])
print(cities[-4])
'''

#Slicing
'''
cities = ['St. Louis', 'Chicago', 'Austin', 'New York City']
print(cities[0:3])
'''

#Delete from list using del
'''
cities = ['St. Louis', 'Chicago', 'Austin', 'New York City']
del cities[2]
print(cities)
del cities[1:3]
print(cities)
'''

#Delete from list using pop
#By default pop removes the last value in a list

'''
cities = ['St. Louis', 'Chicago', 'Austin', 'New York City']
cities.pop()
print(cities)
cities.pop(1)
print(cities)
'''

#Add to list
'''
cities.append('New York City')
print(cities)
cities.insert(1,'Austin')
print(cities)
cities.insert(2,'Chicago')
print(cities)
'''

#Change value position in a list - Swap Austin and Chicago
'''
cities = ['St. Louis', 'Chicago', 'Austin', 'New York City']
cities[1], cities[2] = cities[2], cities[1]
print(cities)
'''

#Change list values (ascending)
'''
cities = ['St. Louis', 'Chicago', 'Austin', 'New York City']
cities.sort()
print(cities)
'''

#Change list values (decending)
'''
cities = ['St. Louis', 'Chicago', 'Austin', 'New York City']
cities.sort(reverse=True)
print(cities)
'''

#Check a value in a list
'''
cities = ['St. Louis', 'Chicago', 'Austin', 'New York City']
your_city=input("Enter the city name: ")
if your_city in cities:
    print('included!')
else:
    print('not included')
'''

#Using loops to add values into a list
'''
numbers = []
for i in range(1,10):
    numbers.append(i)
print(numbers)
'''

'''
This also works...
numbers = [i for i in range(1,10):]
print(numbers)
'''

#Nested lists
'''
cities_and_states = [['St. Louis', 'Chicago', 'Austin', 'New York City'], ['Missouri', 'Illinois', 'Texas', 'New York']]
print(cities_and_states)
print(cities_and_states[0][1])
print(cities_and_states[1][1])
'''
#Print 'banana'
'''
my_list = ['a', 'b', 'c', 1, 2, 3, ['apple', 'orange', 'banana'], 'd']
print(my_list[6][2])
'''

#Change individual value in a list
'''
my_list = ['a', 'b', 'c', 1, 2, 3, ['apple', 'orange', ['john', 'robert'], 'banana'], 'd']
my_list[6][2][1] = 'joe'
print(my_list)
'''

