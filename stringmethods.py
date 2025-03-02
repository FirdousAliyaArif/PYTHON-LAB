#Python program to show string operations
s = "Python was created by Guido Van Rossum"
print(s)
print(type(s))
print(len(s)) #to print length of the string
print(s.startswith('P')) #to check the starting character
print(s.endswith('m')) #to check the ending character
print(s.split(' ')) #to split a string into a list
print(s.isalnum()) #to check if all the characters are alpha-numerical
print(s.isdecimal()) #to check if all the characters are decimal 
print(s[:4]) #slicing the string
print(s.index('c')) #to find the index of a character
print(s.upper()) #to onert all the characters into upper case 
print(s.lower()) #to convert all the characters into lower case 
print(s.center(10)) #to center the string
print(s.capitalize()) #to capitalize the first charater
print(s.isupper()) #to check if all the characters are in upper case
print(s.islower()) #to heck if all the characters are in lower case
print(s.replace('was','replaccement')) #replacing one character with another character