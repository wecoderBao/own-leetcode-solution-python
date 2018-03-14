"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def twoSumClosest(nums, start, sum2):
            end = len(nums) - 1
            distance = abs(sum2 - nums[start] - nums[end])
            ans = nums[start] + nums[end]
            while start < end:
                if nums[start] + nums[end] == sum2:
                    ans = nums[start] + nums[end]
                    break
                elif nums[start] + nums[end] > sum2:
                    if abs(sum2 - nums[start] - nums[end]) < distance:
                        distance = abs(sum2 - nums[start] - nums[end])
                        ans = nums[start] + nums[end]
                    end -= 1
                elif nums[start] + nums[end] < sum2:
                    if abs(sum2 - nums[start] - nums[end]) < distance:
                        distance = abs(sum2 - nums[start] - nums[end])
                        ans = nums[start] + nums[end]
                    start += 1
            return ans
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        # float("inf")正无穷 float("-inf")负无穷
        distance = float("inf")
        for i in range(len(nums)):
            if i + 1 < len(nums) - 1:
                sum3 = nums[i] + twoSumClosest(nums, i + 1, target - nums[i])
                if abs(target - sum3) < distance:
                    distance = abs(target - sum3)
                    result = sum3
        return result


if __name__ == '__main__':
    arr = [-3,-2,-5,3,-4]
    s = Solution()
    print(s.threeSumClosest(arr, -1))
