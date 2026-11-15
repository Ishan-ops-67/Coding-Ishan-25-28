name = input('Enter your name: ')
number = input('Enter a number: ')
number = int(number)
if number < 10:
    for i in range(number):
        print(name)
else:
    print('too high')