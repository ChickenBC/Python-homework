try:
    x = input("Enter a number:")
    x = int(x)

    y = input("Enter a number:")
    y = int(y)
except ValueError:
    print("Sorry, I really need a number.")
else:
    sum = x + y
    print("The sum of " + str(x) + " and " + str(y) + " is " + str(sum) + ".")
