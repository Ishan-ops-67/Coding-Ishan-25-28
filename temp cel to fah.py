temp = input('would you like celsius or fahrenheit: ')
if (temp == 'celsius'):
    celsius = ('enter the temperature you wish to convert: ')
    fahrenheit = celsius * 9,5 + 32
    print('your temperature in fahrenheit is',fahrenheit)
elif (temp == 'fahrenheit'):
    fah = ('enter the temperature you wish to convert: ')
    cel = (fah - 32) * 5,9 
    print('your temperature in celsius is',cel)
    