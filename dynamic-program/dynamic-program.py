"""
有n级台阶，一个人每次上一级或者两级，问有多少种走完n级台阶的方法。
"""

class Solution:
    def stepKinds(self, n):
        temp = [None for i in range(n)]

        temp[1] = 1
        temp[2] = 2
        def dp(i):
            if i == 1 or i == 2:
                return i
            if not temp[i-1]:
                temp[i-1] = dp(i-1)
            if not temp[i-2]:
                temp[i-2] = dp(i-2)
            return temp[i-1] + temp[i-2]

        return dp(n)


"""
给定数组arr，返回arr的最长递增子序列的长度，比如arr=[2,1,5,3,6,4,8,9,7]，
最长递增子序列为[1,3,4,8,9]返回其长度为5.
"""

def subIncrementSeq(arr):

    dp = [1 for i in range(len(arr))]
    for i, x in enumerate(arr):
        tempMax = 1
        for j in range(i):
            if arr[i] > arr[j] and dp[j] + 1 > tempMax:
                tempMax = dp[j] + 1

        dp[i] = tempMax
    ans = 1
    for i in range(len(arr)):
        if dp[i] > ans:
            ans = dp[i]

    return ans


if __name__ == '__main__':
    arr = [2, 4, 5, 3, 1]
    print(subIncrementSeq(arr))