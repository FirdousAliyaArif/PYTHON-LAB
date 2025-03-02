#Python program for finding th esum of even and odd numbers till a range 
a = (int(input("Please enter the maximum value to print the sum:\n")))
even = 0
odd = 0 
for number in range (1,a+1):
    if number % 2 == 0:
        even = even+number 
    else:
        odd = odd+number 
print("The sum of even numbers till",a,"is:\n",even)
print("The sum of odd numbers till",a,"is:\n",odd)
        