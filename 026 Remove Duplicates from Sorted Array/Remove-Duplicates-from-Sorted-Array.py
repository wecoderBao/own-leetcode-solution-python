"""
Given a sorted array, remove the duplicates in-place such that each element appear only once and
return the new length.
Do not allocate extra space for another array, you must do this by modifying the input
array in-place with O(1) extra memory.
Example:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
"""


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        start = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[start]:
                start += 1
                nums[start] = nums[i]
        return start + 1


if __name__ == '__main__':
    s = Solution()
    nums = []
    print(s.removeDuplicates(nums))