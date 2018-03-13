"""
Write a function to find the longest common prefix string amongst an array of strings.
"""


class Solution:
    def longestCommonPrefix(self, strs):
        """
        横向扫描
        :type strs: List[str]
        :rtype: str
        """
        if not strs and len(strs) < 1:
            return ""
        def commonPrefix(str1, str2):
            pre = []
            len1 = len(str1)
            len2 = len(str2)
            i = 0
            while i < len1 and i < len2:
                if str1[i] == str2[i]:
                    pre.append(str1[i])
                    i += 1
                else:
                    break
            return ''.join(pre)

        ans = strs[0]
        for i in range(1, len(strs)):
            ans = commonPrefix(ans, strs[i])

        return ans

    def longestCommonPrefix2(self, strs):
        """
        竖向扫描
        :param strs:
        :return:
        """
        if not strs and len(strs) == 0:
            return ""
        ans = strs[0]
        for j in range(len(ans)):
            for i in range(1, len(strs)):
                if j == len(strs[i]) or strs[i][j] != ans[j]:
                    return ans[:j]
        return ans

    def longestCommonPrefix3(self, strs):
        """
        divide and conquer
        :param strs:
        :return:
        """
        def commonPrefix(str1, str2):
            if not str2 or not str1:
                return ""
            while str1:
                if not str2.startswith(str1):
                    str1 = str1[:len(str1)-1]
                else:
                    return str1
            return str1
        def longestCommon(strs, left, right):
            if left == right:
                return strs[left]
            else:
                mid = (left + right) // 2
                left_common = longestCommon(strs, left, mid)
                right_common = longestCommon(strs, mid+1, right)
                return commonPrefix(left_common, right_common)
        if not strs or len(strs) == 0:
            return ""
        return longestCommon(strs, 0, len(strs)-1)


if __name__ == '__main__':
    strs = ['']
    s = Solution()
    print(s.longestCommonPrefix3(strs))

