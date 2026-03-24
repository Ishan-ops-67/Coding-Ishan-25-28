ab = int(input('lenght from a to b'))
bc = int(input('lenght from b to c'))
cd = int(input('lenght from c to d'))
da = int(input('lenght from d to a'))
i = int(input('enter iunternal angle'))
if ab == bc:
    if ab == cd:
        if i == 90:
            print('its a square')
        else:
            print('its a rhombus')
    else:
        print('its a irrgular quad')
else:
    print('its a irrgular quad')
else:
    if ab == cd:
    if bc == ad:
        if i == 90:
            print('its a rect')
        else:
            print('its a parralel')
    else:
        print('its a irrgular quad')
else:
    print('its a irrgular quad')