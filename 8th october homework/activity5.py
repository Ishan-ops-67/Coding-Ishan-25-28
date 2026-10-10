sales = float(input('enter your monthly sales: '))
if sales >= 40000:
    commission = sales * 0.15
    print('your commission is', commission)
else:
    commission = sales * 0.05
    print('your commission is', commission)