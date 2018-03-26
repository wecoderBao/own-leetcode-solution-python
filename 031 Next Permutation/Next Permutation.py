"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""


class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0 or len(nums) == 1:
            return
        right = len(nums) - 1
        while right >= 1 and nums[right] <= nums[right-1]:
            right -= 1
        i = right - 1
        # 原序列降序
        if i < 0:
            nums.sort()
            return
        for j in range(right, len(nums)):
            if nums[i] >= nums[j]:
                j = j - 1
                break
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        i = right
        j = len(nums) - 1
        while i < j:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i += 1
            j -= 1

    def nextPermutation2(self, nums):
        i = len(nums) - 2
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1
        # 若i小于零则原序列为降序，转换为升序即可
        if i >= 0:
            j = len(nums) - 1
            #
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            self.swap(nums, i, j)
        self.reverse(nums, i+1)
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
    def reverse(self, nums, i):
        j = len(nums) - 1
        while i < j:
            self.swap(nums, i, j)
            i += 1
            j -= 1


if __name__ == '__main__':
    s = Solution()
    nums = [5,1,3, 3]
    s.nextPermutation(nums)
    print(nums)

