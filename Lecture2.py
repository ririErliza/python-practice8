''' Branching Loops and Functions'''

a_number = 34

if a_number  % 2 == 0:
    print("We're inside an if block")
    print("The given number {} is even." .format(a_number))
else:
    print("The given number {} is odd" .format(a_number))



the_3_musketeers = ('Athos', 'Porthos', 'Aramis')

print('--------------------------')

a_candidate = 'Artagnan'

if a_candidate in the_3_musketeers:
    print("{} is a musketeer".format(a_candidate))
else:
    print("{} is NOT a musketeer". format(a_candidate))

print('--------------------------')

today = 'Wednesday'

if today == 'Sunday':
    print('Today is the day of the sun.')
elif today == 'Monday':
    print('Today is the day of the moon')
elif today == 'Tuesday':
    print('Today is the day of Tyr, the god of war')
elif today == 'Wednesday':
    print('Today is the day of Odin, the supreme deity')
elif today == 'Thursday':
    print('Today is the day of Thor')
elif today == 'Friday':
    print('Today is the day of Frigga')
elif today == 'Saturday':
    print('Today is the day of Saturn')
