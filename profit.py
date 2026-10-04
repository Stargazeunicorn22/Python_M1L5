x = input("How many oranges would you like to buy? ")
x = int(x)
if type(x) == int and x > 0:
    y = 100*x
    z = 120 * x
    if z > y:
        z = z-y
        print("Yay! We have a profit of "+ str(z))
    else:
        print("We aren't getting a profit :(")
else:
    print("Please give a valid number.")
    