# Maximum element in array leetcode

nums = [10, 5, 25, 2]
def find_max(nums):
        max_num = nums[0]
        for i in nums:
                if i > max_num:
                        max_num = i
                else:
                        continue
        return max_num
print(find_max(nums))


