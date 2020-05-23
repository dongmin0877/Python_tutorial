for fruit in ['apple', 'banana','orange']:
    print(fruit)
else:
    print('I ate all!')

print('-------------------')
for fruits in ['apple', 'banana' , 'orange']:
    if fruits == 'banana':
        print('stop eating')
        break
    print(fruits)
else:
    print('I ate all!')