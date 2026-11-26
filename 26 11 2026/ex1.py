def num_test(number):
    if number > 10:
        return 'greater than 10'
    if number < 10:
        return 'less than 10'
    if number == 10:
        return 'equal to 10'
number = int(input('ENTER A NUMBER:'))
print(num_test(number))