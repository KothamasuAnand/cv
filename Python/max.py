a=int(input("Enter 1 :"))
b=int(input("Enter 2 :"))
c=int(input("Enter 3 :"))

if a>=b and a>=c:
    print(a)
elif b>=a and b>=c:
    print(b)
else:
    print(c)