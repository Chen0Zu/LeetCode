'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
'''
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        if x < 0:
            sign = -1
        b = 0
        x = x*sign
        while x:
            b = b*10+x % 10
            if b*sign <-2**31 or b*sign > 2**31-1:
                return 0
            x = int(x / 10 )
        return b*sign

x = -123
print(Solution().reverse(x))
