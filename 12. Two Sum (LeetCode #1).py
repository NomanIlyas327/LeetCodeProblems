# 1. Two Sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

nums = [7, 11, 2, 15]
target = 9


# def twoSum(nums , target):
#     for i in range(len(nums)):
#         for j in range(i + 1 , len(nums)):
#             if nums[i] + nums[j] == target:
#              return[i,j]
            
# print(twoSum(nums, target))


# Approach 2: Dictionary/Hash Map

def twoSum(nums, target):
        # 1. Diary banai
        seen = {} 
        
        # 2. Sair shuru ki (Index aur Value dono ke saath)
        for i, num in enumerate(nums):
            
            # 3. Hisab lagaya ke kitna mazeed chahiye
            remaining = target - num
            
            # 4. Diary mein check kiya
            if remaining in seen:
                # Agar mil gaya to purana index aur ab wala index bhej do
                return [seen[remaining], i]
            
            # 5. Agar nahi mila, to aaj wala number diary mein save kar lo
            seen[num] = i
print(twoSum(nums, target))