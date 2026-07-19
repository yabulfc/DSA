# Product of Array Ecept Self

nums = list(map(int, input("Enter the numbers separated by space: ").split() ) )

storeOutput = [0] * len(nums)


for x in range(len(nums)):
    product = 1

    for i in range(len(nums)):
        if nums[x] == nums[i]:
            continue
        elif nums[x] != nums[i]:
            product *= nums[i] 
    storeOutput[x] = product
    

print(storeOutput)


#OR it can be solved as 

nums = list(map(int, input("Enter numbers: ").split(",")))

storeOutput = [0] * len(nums)

for x in range(len(nums)):
    product = 1

    for i in range(len(nums)):
        if x == i:
            continue
        product *= nums[i]

    storeOutput[x] = product

print(storeOutput)




