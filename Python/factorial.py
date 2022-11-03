import sys
n=int(input())
if n==0 or n==1:
    print("1")
    sys.exit()
f=1
for i in range(2,n+1):
    f=i*f
print(f)