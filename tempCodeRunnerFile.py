def strStr(haystack, needle):
    m = len(haystack)
    n = len(needle)
    if n == 0:
        return 0
    for i in range(m - n + 1):
        if haystack[i:i + n] == needle:
            return i
    return -1
haystack = "Pakistan"
needle = "stan"
print(strStr(haystack, needle))


