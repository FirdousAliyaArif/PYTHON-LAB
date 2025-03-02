#Python program for performing tuple operations
tpl=('python','is','a','programming','language')
print(tpl) #printing the tuple
print(type(tpl)) #printing the type
print(len(tpl)) #printing the length of the tuple
#Indexing of the tuple
print(tpl[1])
#Reverse indexing of the tuple
print(tpl[-1])
#slicing of the tuple
print(tpl[0:4])
#adding two tuples
new=('abc','123')
print(new) #printing the new tuple
addtpls=tpl+new
print(addtpls)
print(len(addtpls)) #length of the cocatented tuples
print(tpl*2) #printing the items in tuple twice
#count of an item in the tuple
print(tpl.count('is'))
#index of an item in the concatenated tuple
print(addtpls.index('a'))
#converting the tuple into a list to an item
tup=list(tpl) #the tuple is being converted into a list
tup[2]="lol" #replacig the item at index 2
tpl=tuple(tup) #converting back into a tuple
print(tpl) #printing the updated tuple