#Python program for finding fibonacci series till a range
nterms = int(input("how many terms would you like to print?\n"))
n1,n2 = 0,1 
count = 0
if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci series upto",nterms,":")
    print(n1)
else:
    print("fibonacci sequene:")
while count < nterms:
    print (n1)
    nth = n1+n2
    n1 = n2
    n2 = nth
    count += 1