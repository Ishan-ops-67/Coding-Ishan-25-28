len_rect = float(input('enter the lenght of rectangle in metres: '))
wid_rect = float(input('enter the width of rectangle in metres: '))
peri_rect = len_rect * wid_rect
cost_per_met = float(input('enter the cost per metre: '))
price = cost_per_met * peri_rect
print('the price is: ',price)
