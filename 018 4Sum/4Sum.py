"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""


class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if nums is None or len(nums) < 4:
            return []
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i - 1 >= 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                if j - 1 > i and nums[j-1] == nums[j]:
                    continue
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    # 先计算出sum的值， 否则重复计算会增加时间复杂度
                    sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum == target:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                    elif sum > target:
                        right -= 1
                    elif sum < target:
                        left += 1

        return ans

if __name__ == '__main__':
    arr = [1, 0, -1, 0, -2, 2]
    arr = [-3,-2,-1,0,0,1,2,3]
    s = Solution()
    print(s.fourSum(arr, 0))