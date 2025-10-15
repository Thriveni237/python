try:
    x=int(input("Enter first number:"))
    y=int(input("Enter second number:"))
    print(x/y)
except ZeroDivisionError:
    print("Can't divide with zero")
except ValueError:
    print("Please provide int value only")
    
