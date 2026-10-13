negative = int(input('how many negatives did you get'))
if (negative == 1):
    for i in range(1,11):
        print('prompt')
elif (negative == 2):
    for i in range(1,51):
        print('reminder')
elif (negative == 3):
    for i in range(1,101):
        print('warning')
else:
    for i in range(1,501):
        print('removal')