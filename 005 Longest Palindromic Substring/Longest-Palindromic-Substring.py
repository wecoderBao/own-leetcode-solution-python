"""

"""

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        for i in range(len(s)):
            ans1 = self.centerGrow(s, i, i)
            ans2 = self.centerGrow(s, i, i+1)
            if len(ans) < len(ans1):
                ans = ans1
            if len(ans) < len(ans2):
                ans = ans2
        return ans

    def centerGrow(self, s, i, j):
        maxLen = 0
        ans = ""
        while i >= 0 and j <= len(s) - 1:
            if s[i] == s[j]:
                if j - i + 1 > maxLen:
                    maxLen = j - i + 1
                    ans = s[i:j+1]
                i -= 1
                j += 1
            else:
                break
        return ans


if __name__ == '__main__':
    s = Solution()
    ans = s.longestPalindrome("cbbd")
    print(ans)