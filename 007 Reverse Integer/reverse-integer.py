"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output:  321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range.
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = 0
        flag = x < 0 and -1 or 1
        x = abs(x)
        while x:
            ans = ans * 10 + x % 10
            x = x // 10
        if ans > 0x7fffffff:
            ans = 0
        ans *= flag

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(-2147483648))

