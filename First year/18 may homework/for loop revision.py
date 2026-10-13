number = int(input('enter a number: '))
print('you will now be asked for',number,'numbers')
number_1 = 0
for i in range(number):
    number_2 = float(input('enter a number:'))
    number_1 = number_1 + number_2
print('the total of the values enterd is:',number_1)