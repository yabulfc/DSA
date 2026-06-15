fruits = []

fruits.append("Apple")
fruits.append("Banana")
fruits.append("Cherry")

print("friuts list:" + fruits) # Output: ['Apple', 'Banana', 'Cherry']   

friuts = friuts.get(1) # Get the second element (index 1 is "banana")
print("Second fruit:" + fruits) # Output: Banana

containsMango = "Mango" in fruits # Check if "Mango" is in the list and returns in boolean
print("Contains Mango:" + containsMango) # Output: False

removeFruit = fruits.remove("Banana") # Remove "Banana" from the list
print('removed fruit:' + removeFruit) # Output: Banana

print("Updated fruits list:" + fruits) # Output: ['Apple', 'Cherry']

isEmpty = len(fruits) == 0 # Check if the list is empty and returns in boolean