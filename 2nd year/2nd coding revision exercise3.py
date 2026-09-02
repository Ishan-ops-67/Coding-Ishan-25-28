sent = input('enter a sentence: ')
x = 0
for b in sent:
    if b == 'a' or b == 'e' or b == 'o' or b == 'i'or b == 'u':
        x = x + 1
print(x)