def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1
        
nums = [1,12,23,34,4,5,66,7,77]
target = 4
result = linear_search(nums, target)
if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the array")
