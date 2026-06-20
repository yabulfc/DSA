# Question 1

# 1, Check if pair with given sum exists in array

# Given an array of A[] of n numbers and another number X , the is to check whether or not
# there exist a pair in the array A[] whose sum is exactly X.

# Example 1:

# input: A[] = {0, -1, 2, -3, 1},X=-2
# Output: True
# Explanation: There is a pair in the array whose sum is -2, i.e., (-1, -1)

# Example 2:A[] = {1, -2, 1, 0, 5},X=0
# Output: False   
# Explanation: There is no pair in the array whose sum is 0.

#Answer:  

def has_pair_with_sum(arr, target_sum):
    arr = sorted(arr)   
    left, right = 0, len(arr) - 1   
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            return True
        elif current_sum < target_sum:
            left += 1
        else:
            right -= 1
    return False
print(has_pair_with_sum([0, -1, 2, -3, 1], -2) ) # Output: True
print(has_pair_with_sum([1, -2, 1, 0, 5], 0))  # Output: False
