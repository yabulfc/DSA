nums = [20, 30, 40, 50, None] # Added a 'None' as a placeholder for the new space
insertIndex = 2
insertValue = 25

# 1. Shift elements to the right (Backwards loop)
# We start from the last index and move down to insertIndex
for i in range(len(nums) - 1, insertIndex, -1):
    nums[i] = nums[i-1]

# 2. Insert the value into the "hole" we created
nums[insertIndex] = insertValue

# 3. Print the updated array
print(nums)




