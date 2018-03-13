"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        def twoSum(arr, start, target):
            end = len(arr) - 1
            another = start -1
            while start < end:
                if arr[start] + arr[end] == target:
                    ans.append([arr[another], arr[start], arr[end]])
                    start += 1
                    end -= 1
                    while start < end and arr[start] == arr[start-1]:
                        start += 1
                    while start < end and arr[end] == arr[end+1]:
                        end -= 1
                elif arr[start] + arr[end] > target:
                    end -= 1
                elif arr[start] + arr[end] < target:
                    start += 1
        nums.sort()
        for i, x in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            twoSum(nums, i+1, -nums[i])
        return ans


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    s = Solution()
    print(s.threeSum(nums))