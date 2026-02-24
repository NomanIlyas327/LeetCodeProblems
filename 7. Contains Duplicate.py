# 217. Contains Duplicate
first_list = [1, 2, 3, 1]
def containsDuplicate(nums):
    if len(nums) != len(set(nums)):
        return True
    return False
print(containsDuplicate(first_list))