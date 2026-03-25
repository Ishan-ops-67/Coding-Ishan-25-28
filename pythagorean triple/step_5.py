a = int(input('enter an integer'))
b = int(input('enter an integer'))
c = int(input('enter an integer'))
for a in range(1,21):
    for b in range(1,21):
        for c in range(1,21):
            a_squared = a * a
            b_squared = b * b
            c_squared = c * c
            if (a_squared + b_squared == c_squared):
                print('you entered a pythagorean triple')