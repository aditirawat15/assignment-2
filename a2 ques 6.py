a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

if a >= b+c:
    print("Yes")
elif b >= a+c:
    print("Yes")
elif c >= a+b:
    print("Yes")
else:
    print("No")
