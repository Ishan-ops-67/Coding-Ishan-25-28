total = 0
for i in range(1,6):
    number = int(input('Enter a number:  '))
    add = input('Would you like this number added to the total?: ')
    if add == 'yes':
        total = total + number
print(f'the total is {total}')