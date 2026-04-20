# Problem: Merge Sorted Array (LeetCode #88)
def merge(nums1, m, nums2, n):
    i = m - 1  # i = 3
    j = n - 1  # j = 2
    k = m + n - 1  # k = 6

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
nums1 = [1, 2, 3, 4, 0, 0, 0]
# m is the number of elements in nums1 that are part of the merge, and n is the number of elements in nums2
m = 4
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)