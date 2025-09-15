#Basic if statement
'''
if condition_a_met:
    do_scenario_a()
else:
    do_scenario_d()
'''

#if statement with elif
'''
if condition_a_met:
    do_scenario_a()
elif condition_b_met:
    do_scenario_b()
elif condition_c_met:
    do_scenario_c()
else:
    do_scenario_d()
'''

#nested if statements
'''
a = input('y/n ')
if a == 'y':
    b = input('yes/no')
    if b == 'yes':
        print('Very Good!')
    else:
        print('Very Bad!')
else:
    print('Extremely bad!')
'''