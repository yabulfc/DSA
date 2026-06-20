data = [None] * 5 # Create a list of size 5 to hold heterogeneous elements
data[0] = 10    
data[1] = "Hello"
data[2] = 3.14
data[3] = True
data[4] = 'A'

print("Heterogeneous elements in the list:" , data) # Output: [10, 'Hello', 3.14, True, 'A']

for x in data:
    print(x) # Output: 10, Hello, 3.14, True, A (each on a new line)