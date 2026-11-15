invitees = int(input('enter the amount of people you have invited to your party: '))
if invitees < 10:
    for i in range(1,invitees + 1):
        name = input('enter this persons name: ')
        print(f'{name} has been invited')
else:
    print('too many people')