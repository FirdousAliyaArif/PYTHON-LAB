#Python program for sum of n numbers
n = int(input("Enter the range of sum\n"))
sum = 0
for i in range(n+1):
    sum += i 
    print("sum of",n,"numbers is:",sum)