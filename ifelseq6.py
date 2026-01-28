n = int(input("Enter a number: "))

if n < 0:
    n = -n

if n < 10:
    print("Number of digits: 1")
elif n < 100:
    print("Number of digits: 2")
elif n < 1000:
    print("Number of digits: 3")
elif n < 10000:
    print("Number of digits: 4")
else:
    print("Number has more than 4 digits")