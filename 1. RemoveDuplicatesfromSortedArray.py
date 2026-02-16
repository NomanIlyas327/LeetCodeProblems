def remove_duplicates(nums):
    if not nums: return 0
    i = 0
    for j in range (1 ,len(nums)):
     if nums[j] != nums[i]:
        i = i + 1
        nums[i] = nums[j]
    return i + 1
nums = [1, 1, 2 , 3, 3, 4, 5, 5]
length = remove_duplicates(nums)
print(f"Length of array after removing duplicates: {length}")
print(f"Array after removing duplicates: {nums[:length]}")
