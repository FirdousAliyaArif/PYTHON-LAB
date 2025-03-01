#Python program for reverse of a number

a = int(input("Enter the number to reverse\n"))
rev = 0
while( a > 0 ):
    rem = a % 10  
    rev = rev * 10 + rem  
    a = a // 10 
print("The reversed number is:",rev)
