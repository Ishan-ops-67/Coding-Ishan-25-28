direct = input('wanna go up or down?')
if direct == 'up':
    number = int(input('enter the top number then: '))
    for i in range(0,number):
        print(i)
elif direct == 'down':
    number = int(input('enter a number below 20 then: '))
    if number < 20:
        for i in range(0,number):
            print(i)
    else:
        print('i dont understand')
        