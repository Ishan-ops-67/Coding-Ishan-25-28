number = input('Please enter a number between 1 to 12 you wish to see a times table for: ')
number = int(number)
for i in range(1,13):
    result = number * i
    print(f'{number} x {i} = {result}')