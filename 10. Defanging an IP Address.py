# 1108. Defanging an IP Address
# Given a valid (IPv4) IP address, return a defanged version of that IP address.

# A defanged IP address replaces every period "." with "[.]".

# Example 1:

# Input: 
address = "1.1.1.1"

# Output:
"1[.]1[.]1[.]1"
# Example 2:
# Input:
address = "255.100.50.0"
# Output:
"255[.]100[.]50[.]0"
# Note: The input is a valid IPv4 address.
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")
# Runtime: 28 ms, faster than 99.97% of Python3 online submissions for Defanging an IP Address.
# Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Defanging an IP Address.
solution = Solution()
print(solution.defangIPaddr(address))



