"""
Determine whether an integer is a palindrome. Do this without extra space.
负数都不是回文数
"""


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reverse_num = 0
        while x > reverse_num:
            reverse_num = reverse_num * 10 + x % 10
            x = x // 10
        return x == reverse_num or x == reverse_num / 10


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(0))