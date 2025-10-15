try:
    print("TRY")
except:
    print("Exccept")
finally:
    print("Finally")
    
print("------------------")
try:
    print("try")
    print(10/0)
except ZeroDivisionError:
    print("Except")
finally:
    print("Finally")
    
        
