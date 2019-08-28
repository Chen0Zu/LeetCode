'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs or len(strs)<1:
            return ""
        shortest = min(strs,key=len)
        for i,c in enumerate(shortest):
            for s in strs:
                if s[i] != c:
                    return s[:i]
        return shortest
    
strs = ["flower","flow","flight"]
print(Solution().longestCommonPrefix(strs))