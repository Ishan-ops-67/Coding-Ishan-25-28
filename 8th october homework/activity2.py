number1 = float(input('enter a number: '))
number2 = float(input('enter a number: '))
number3 = float(input('enter a number: '))
if number3 > number1:
    if number3 > number2:
        print('the largest number is',number3)
elif number2 > number3:
    if number2 > number1:
        print('the largest number is',number2)
elif number1 > number2:
    if number1 > number3:
        print('the largest number is',number1)
