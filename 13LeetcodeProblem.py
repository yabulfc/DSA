#Two Sum 

#Given an array of integers nums and an integer target , return 
#indices of the two numbers such that they add up to target.
# you may assume that each input would have exactly one solution, 
# and you may not use the same element twice.
#you can return the answer in any order

#Answer
def twoSum(nums, target):   
    

    n = len(nums)

    left = 0
    right = n-1

    sorted_nums = sorted(nums)
    finalAns = []

    while left < right:
        currSum = sorted_nums[left] + sorted_nums[right]
        if currSum == target:
            for i in range(n):
                if nums[i] == sorted_nums[left]:
                    finalAns.append(i)
                    break
            for i in range(n):
                if nums[i] == sorted_nums[right]:
                    finalAns.append(i)
                    break
            break    
        elif currSum < target:
            left += 1
        else:
            right -= 1
    return finalAns

print(twoSum([3,2,4],6))