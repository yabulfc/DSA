fruits = []

fruits.append("Apple")
fruits.append("Banana")
fruits.append("Cherry")

print("friuts list:" ,fruits) # Output: ['Apple', 'Banana', 'Cherry']   

secFriuts = fruits[1] # Get the second element (index 1 is "banana")
print("Second fruit:" , secFriuts) # Output: Banana

containsMango = "Mango" in fruits # Check if "Mango" is in the list and returns in boolean
print("Contains Mango:" , containsMango) # Output: False

removeFruit = "Banana"
removedFruit = fruits.remove("Banana") # Remove "Banana" from the list
print('removed fruit:' ,removeFruit ) # Output: Banana

print("Updated fruits list:" , fruits) # Output: ['Apple', 'Cherry']

isEmpty = len(fruits) == 0 # Check if the list is empty and returns in boolean
print("Is fruits list empty:" , isEmpty) # Output: False

size = len(fruits) # Get the size of the list
print("Size of the fruits list:" , size) # Output 2

fruits = fruits.clear() # Clear the list
isEmptyAfterClear = not fruits # Check if the list is empty after clear and returns in boolean
print("Is fruits list empty after clear:" , isEmptyAfterClear) # Output True

