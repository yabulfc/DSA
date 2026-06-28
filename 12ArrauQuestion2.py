#Question 2
#Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order. 

#Example 1: 
# input: N=5
# array = [0, 1, 2, 0, 1]
#output: 0 0 1 1 2
#Explanation: 0s 1s and 2s are segregated into ascending order


#Example 2: 
# input: N=3
# array = [0, 1,0]
#output: 0 0 1 
#Explanation: 0s 1s and 2s are segregated into ascending order


#Answer:
def sort_array(arr):
    # Count the number of 0s, 1s, and 2s
    count_0 = arr.count(0)
    count_1 = arr.count(1)
    count_2 = arr.count(2)

    # Create a new sorted array based on the counts
    sorted_arr = [0] * count_0 + [1] * count_1 + [2] * count_2
    return sorted_arr

N = int(input("Enter the size of the array: "))   
arr = list(map(int,input("Enter the elements of the array (0s, 1s, and 2s only): ").split()))

sorted_arr = sort_array(arr)

for num in sorted_arr:
    print(num, end=' ')

