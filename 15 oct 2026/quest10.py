people = int(input('how many people in your party: '))
if people < 10:
    for i in range(0,people):
        name = input('whats theyre name: ')
        print(name,'has been invited')
else:
    print('too many people please rerun and choose below 10 people')
