a=int(input("Enter the First Number :"))
b=int(input("Enter the Second Number :"))

smaller=min(a,b)

while smaller:
    if a%smaller==0 and b%smaller==0:
        print(smaller)
        break
    smaller-=1