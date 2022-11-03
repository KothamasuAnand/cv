import sys
while True:
    print("1.ADDITION")
    print("2.SUBRACTION")
    print("3.MULTIPLICATION")
    print("4.DIVISION")
    print("5.POWER")
    print("0.EXIT")

    choice=int(input("Enter your choice :"))

    if choice==1:
        a = int(input("Enter first Number: "))
        b = int(input("Enter Second Number: "))
        print(a+b)
    if choice==2:
        a = int(input("Enter first Number: "))
        b = int(input("Enter Second Number: "))
        print(a-b)
    if choice==3:
        a = int(input("Enter first Number: "))
        b = int(input("Enter Second Number: "))
        print(a*b)
    if choice==4:
        a = int(input("Enter first Number: "))
        b = int(input("Enter Second Number: "))
        print("Quotient: "+a//b+"Remainder: "+a%b)
    if choice==5:
        a = int(input("Enter first Number: "))
        b = int(input("Enter Second Number: "))
        print(pow(a,b))
    if choice==0:
        sys.exit()
    
    