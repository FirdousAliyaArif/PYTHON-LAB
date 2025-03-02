#Python program for finding wether the number is armstrong or not
num = int(input("Enter a number:\n"))
sum = 0
temp = num 
while temp > 0:
    digit = temp%10
    sum += digit**3
    temp//= 10

if num == sum:
    print(num,"is an armstrong number\n")
else:
    print(num,"is not an arm strong number\n")
        