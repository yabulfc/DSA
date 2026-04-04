numbers = [10 ,20 ,30 ,40 ,50 ,60]
deleteIndex = 2

#Replacing the index from 2 upto the end, By the next index value
for i in range(deleteIndex , len(numbers)-1):
    numbers[i] = numbers[i+1]

#Remove the last unwanted value 
numbers[len(numbers)-1] = None

#display the result
for x in numbers:
    print(x)