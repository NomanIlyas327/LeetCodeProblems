# 1929. Concatenation of Array

class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return nums + nums
# Runtime: 128 ms, faster than 99.97% of Python3 online submissions for Concatenation of Array.
# Memory Usage: 15.1 MB, less than 100.00% of Python3 online submissions for Concatenation of Array.
solution = Solution()
print(solution.getConcatenation([1, 2, 1]))