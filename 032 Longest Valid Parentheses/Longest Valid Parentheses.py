"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
"""


class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        ans = 0
        for i, item in enumerate(s):
            if len(stack) == 0:
                stack.append([item, i])
            else:
                top = stack[-1]
                if top[0] == '(' and item == ')':
                    stack.pop()
                    if len(stack) == 0:
                        start = -1
                    else:
                        start = stack[-1][1]
                    ans = max(ans, i-start)
                else:
                    stack.append([item, i])
        return ans


    def dpSolution(self, s):
        ans = 0
        dp = [0 for i in range(len(s))]
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = (dp[i-2] if i >= 2 else 0) + 2
                elif i - dp[i-1] > 0 and s[i-dp[i-1]-1] == '(':
                    if i - dp[i - 1] >= 2:
                        dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
                    else:
                        dp[i] = dp[i-1] + 2
                ans = max(ans, dp[i])
        return ans


if __name__ == '__main__':
    s = Solution()
    str = ""
    print(s.longestValidParentheses(str))