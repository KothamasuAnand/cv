n=int(input("Enter the number :"))
for i in range(1, 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FIZZ BUZZ")
    elif i % 3 == 0:
        print("FIZZ\n")
    elif i % 5 == 0:
        print("BUZZ")
    else:
        print(f'{i}\n')

