"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {'(': 1, ')': -1, '{': 2, '}': -2, '[': 3, ']': -3}
        stack = []
        for ch in s:
            if len(stack) == 0 or d.get(stack[-1]) + d.get(ch) != 0:
                stack.append(ch)
            else:
                stack.pop()
        if len(stack) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    s = "(("
    solution = Solution()
    print(solution.isValid(s))
