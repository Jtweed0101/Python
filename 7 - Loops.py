#While loops are useful when you want to continue something for a unknown period of time
#while condition:
#   do_something(1)
#   do_something(2)

'''
counter = 1
while counter < 11:
    print(counter)
    counter = counter+1
    #Can also use couter += 1
print('Finished!')
'''

'''
secret_number = 777
guessed_number = int(input('Enter number: '))
while True:
    if guessed_number != secret_number:
        print('Ha ha! You\'re stuck in my loop!')
        guessed_number = int(input('Enter number: '))
    else:
        break
print('You are free now.')
'''

#For loops are useful when you want to do something for a fixed/set number of times
'''
ip_addresses = ['192.168.1.2', '192.168.1.3', '192.168.1.4']

for i in ip_addresses:
print(i)
'''

'''
for i in range(3):
    print('Yikes!')
'''

