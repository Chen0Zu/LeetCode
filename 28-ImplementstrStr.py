class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(haystack)
        m = len(needle)
        result = -1
        for i in range(n-m+1):
            if haystack[i:i+m] == needle:
                result = i
                break
        return result

haystack = "aaaaa"
needle = "bba"
print(Solution().strStr(haystack, needle))