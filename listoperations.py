#Python program for performing list operations
lst=['python','was','created','in','1991']
print(lst) #printing the list
print(type(lst)) #printing the type
print(len(lst)) #printing the length of the list
#appending to the list
app = input("Enter the item to append\n")
lst.append(app)
print(lst)
#copying the list into anothr list
copy = lst.copy()
print(copy)
#count of an item in the list
print(lst.count('was'))
#return the index of aniem in the list
print(lst.index('in'))
#inserting items at specific index into the list
lst.insert(2,'abc')
print(lst)
#pop items at a specific index in the list
lst.pop(2)
print(lst)
#removing a specific item in the list
lst.remove('was')
print(lst)
#sorting another list
num = ['1','23','12','2','72','45']
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
#sorting the orignal list
lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)