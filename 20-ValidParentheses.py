'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
'''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = ['(','{', '[']
        if s == '':
            return True
        if s[0] not in brackets or len(s) % 2:
            return False

        stack = []
        stack.append(s[0])
        i = 1
        flag = True
        n = len(s)
        
        while stack and i < n:
                if s[i] in brackets:
                        stack.append(s[i])
                        i = i+1
                else:
                        tmp = stack.pop()
                        if (s[i] == ')' and tmp != '(') or (s[i] == '}' and tmp != '{') or (s[i] == ']' and tmp != '['):
                                flag = False
                                break
                        i = i+1
        if stack != [] and i == n:
            return False
        else:
            return flag
s = '([)]'
print(Solution().isValid(s))