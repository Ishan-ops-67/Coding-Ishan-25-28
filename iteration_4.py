#answer to question: if the user enters 100 it will print 100 200 300 400 500
number = int(input("enter a number"))
for count in range (1,6):
    print(number*count)