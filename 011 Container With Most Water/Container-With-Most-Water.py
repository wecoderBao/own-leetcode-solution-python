"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        for i, x in enumerate(height):
            for j in range(i+1, len(height)):
                if (j - i) * min(x, height[j]) > ans:
                    ans = (j - i) * min(x, height[j])

        return ans

    """
    面积大小由最小高度决定，由两端逐渐靠近，由高度小边向高度大的边靠近
    """
    def maxAreaTwoPoints(self, height):
        start = 0
        end = len(height)-1
        ans = 0
        while start < end:
            ans = max(ans, (end-start)*min(height[start], height[end]))
            if height[start] > height[end]:
                end = end - 1
            else:
                start = start + 1
        return ans



if __name__ == "__main__":
    height = [1, 2]
    s = Solution()
    print(s.maxAreaTwoPoints(height))