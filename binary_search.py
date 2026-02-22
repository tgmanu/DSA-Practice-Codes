def binary_search(nums, target):
    left = 0
    right = len(nums) -1
    while left <= right:
        mid = (left+right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

array = [10,16,27,33,45,56,67,69]
target = 67
result = binary_search(array, target)
if result != -1:
    print(f"Element found in the array at index: {result}")
else:
    print("Element not found in the array")