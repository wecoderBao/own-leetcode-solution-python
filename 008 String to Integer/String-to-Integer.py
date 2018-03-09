"""
Requirements for atoi:

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found.
Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible,
and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no
effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists
because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable
values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
"""

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if str == '' or not str[0].isnumeric() and str[0] != '+' and str[0] != '-':
            return 0
        sign = 1
        if str[0] == '+':
            str = str[1:]
        elif str[0] == '-':
            sign = -1
            str = str[1:]
        len = 0
        for i, s in enumerate(str):
            if not s.isnumeric():
                len = i
                break
            else:
                len = i + 1

        str = str[:len]
        if str == '':
            return 0
        if int(str) > 2147483647:
            if sign == 1:
                return 2147483647
            else:
                return -2147483648
        return int(str) * sign


if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi('-2147483648'))




