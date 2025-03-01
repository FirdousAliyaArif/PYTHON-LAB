#Python program for finding wether the given number is prime or not
a = int(input("Enter the number to check\n"))
i = 2 
count = 0 
while (i < a):
    if(a % i == 0):
        count+=1 
    i+=1 
if(count == 0):
    print("The given nuber is prime\n")
else:
    print("The given number is not prime\n")