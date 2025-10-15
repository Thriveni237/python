def fibonacci(n):
    if n<=0:
        return "invalid input"
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+(n-2)
n=int(input("enter n:"))
print("the",n,"th fibonacci number is:",fibonacci(n))
