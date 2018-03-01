"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        start = 0
        ans = 0
        for i, c in enumerate(s):
            if c in d:
                #更新起始点
                start = max(start, d[c] + 1)
            d[c] = i
            #收录一个字符，更新长度
            ans = max(ans, i - start + 1)
        return ans


if __name__ == '__main__':
    solve = Solution()
    length = solve.lengthOfLongestSubstring("dvdf")
    print(length)