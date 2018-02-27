"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for k in range(i+1, len(nums)):
                if nums[i] + nums[k] == target:
                    return [i, k]

    def twoSum2(self, nums, target):
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return [d.get(target - num), i]
            else:
                d[num] = i


s = Solution()
nums = [2, 7, 3]
target = 9
print(s.twoSum(nums, target))
print(s.twoSum2(nums, target))