# LeetCode Problem 27: Remove Element
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

def removeElement(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val: # Agar kaam ka number hai
            nums[k] = nums[i] # Usay seat do
            k += 1            # Ab agli seat par nazar rakho (k inside IF)
    return k

nums = [3, 2, 2, 3]
val = 3
print(removeElement(nums, val)) # Output ab 2 aayega (Jo ke sahi hai!)