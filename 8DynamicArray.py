# create an empty dynamic array
arr = []

# adding elements (append)
arr.append(int(input()))
arr.append(int(input()))
arr.append(int(input()))

if len(arr) == 0 :
    print('Empty')

# OR another alternative
# if not arr :
#    print('Empty')

else:
 print("Array after adding elements:", arr)

# inserting element at a specific position
arr.insert(1, 15)   # insert 15 at index 1
print("After insertion:", arr)

# removing elements
arr.remove(arr[2])   # removes index value 2 
print("After removing index 2:", arr)

# accessing elements
print("Element at index 2:", arr[2])

# dynamic resizing demonstration
for i in range(5):
    arr.append(i * 100)

print("Final array:", arr)