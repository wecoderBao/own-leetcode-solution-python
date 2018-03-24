"""
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
"""


class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return 0x7fffffff
        sign = 1
        if dividend * divisor < 0:
            sign = -1
        ans = 0
        cnt = 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        subsum = divisor
        while dividend >= divisor:
            #  位运算 除数扩大两倍
            while (subsum << 1) <= dividend:
                # 商扩大两倍
                cnt <<= 1
                subsum <<= 1
            ans += cnt
            cnt = 1
            dividend -= subsum
            subsum = divisor
        return max(min(sign*ans, 0x7fffffff), -2147483648)
