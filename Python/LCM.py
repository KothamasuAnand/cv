a=int(input("Enter the First Number :"))
b=int(input("Enter the Second Number :"))
smaller=min(a,b)
larger=max(a,b)
i=1
while True:
    if (smaller*i)%larger==0:
        print(smaller*i)
        break
    i+=1
