string = input('enter a string:')
len_of_string = len(string)
print('the length of this string is: ',len_of_string)
count = 0
for a in string:
    if a == 'a':
        count = count + 1
    elif a == 'e':
        count = count + 1
    elif a == 'i':
        count = count + 1
    elif a == 'o':
        count = count + 1
    elif a == 'u':
        count = count + 1
print('the number of lowercase volwels is: ',count)