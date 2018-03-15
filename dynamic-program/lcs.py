"""
两个字符串的最长公共字串
用k[i][j]表示A[i]，B[j]结尾的最长公共串的最大长度
如果A[i+1] == B[j+1] 则k[i+1][j+1]=k[i][j]+1，否则，k[i+1][j+1]=0
"""


def longestCommonString(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    temp = [[0 for j in range(len2)] for i in range(len1)]
    for j in range(len2):
        if str1[0] == str2[j]:
            temp[0][j] = 1
    for i in range(len1):
        if str1[i] == str2[0]:
            temp[i][0] = 1
    longest = 0
    for i in range(len1):
        for j in range(len2):
            if i - 1 >= 0 and j - 1 >= 0 and str1[i] == str2[j]:
                temp[i][j] = temp[i-1][j-1] + 1
                longest = max(longest, temp[i][j])
            elif i > 0 and j > 0:
                temp[i][j] = 0
    for i in range(len1):
        print(temp[i])
    return longest


if __name__ == '__main__':
    s1 = 'abcdefgh'
    s2 = 'bcdef'
    print(longestCommonString(s1, s2))

