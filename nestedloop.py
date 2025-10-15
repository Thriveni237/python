for i in range(4):
    for j in range(4):
        print("i=",i,"j=",j)
    print()

n =int(input("enter rows:"))
for i in range(n):
       print(" * "*n)

s =int(input("enter rows:"))
for i in range(s):
       print((chr(65+i)+' ')*s)
