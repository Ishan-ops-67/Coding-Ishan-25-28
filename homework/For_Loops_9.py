direction = input('Do you want to count up or down: ')
if direction == 'up':
    number = int(input('whats the top number then: '))
    for i in range(1,number):
        print(i)
elif direction == 'down':
    number = int(input('enter a number belwo 20 then:'))
    for i in range(number,0,-1):
        print(i)
else:
    print('i dont understand')