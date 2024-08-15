#empty list creation
my_list = []
#output before append
print("Before Append:", my_list)
#using append
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
#output after append
print("After Append:", my_list)
#Insert a value on the second position of the list
my_list.insert(1,15)
#output after insert
print("After Insert:", my_list)
#Extend on my_list
my_list.extend([50,60,70])
#Output after extend
print("After Extend:", my_list)
#Remove an element
my_list.remove(70)
#Output after removal
print("After removal:", my_list)
#Sort my_list
my_list.sort()
#Output after sorting
print("After sorting:", my_list)
#find and print
print("Element found is:", my_list[3])
