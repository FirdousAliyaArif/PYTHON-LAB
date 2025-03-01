#Python program for finding wether the given number is prime or not
a = int(input("Enter a number\n"))
b = int(input("Enter another number"))
if (a>b):
    print(a,"is greatest")
elif(b>a):
    print(b,"is greatest")
else:
    print("Both are equal")