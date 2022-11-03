n=int(input("Enter the Number :"))
da=input("Enter a day:").title()
l=["Sunday","Monday",'Tuesday','Wednesday','Thursday','Friday','Saturday']

for i in range(7):
    if l[i]==da:
        sum=i
sum=sum+n
k=sum%7
print(l[k])


