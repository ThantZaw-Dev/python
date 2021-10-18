n = int(input("Enter the number? "))
for i in range(0,n):
    print()
    for j in range(0,n-i):
        print(" ",end="")
    for x in range(1, (i * 2)):
        print("*",end="")

for x in range(0,n):
    print()
    for y in range(1,x+1):
        print(" ",end="")
    for y in range(1,(n-x)*2):
        print("*",end="")

    
    