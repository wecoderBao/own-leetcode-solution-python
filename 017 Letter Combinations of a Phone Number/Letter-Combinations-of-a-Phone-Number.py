"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []

        d = {1: "", 2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}

        def dfs(digits, index, path, res, d):
            if index == len(digits):
                res.append("".join(path))
                return

            digit = int(digits[index])
            if digit == 1 or digit == 0:
                dfs(digits, index+1, path, res, d)
            else:
                for c in d.get(digit, []):
                    path.append(c)
                    dfs(digits, index + 1, path, res, d)
                    path.pop()

        res = []
        dfs(digits, 0, [], res, d)
        return res


if __name__ == '__main__':
    solution = Solution()
    s = "322"
    print(solution.letterCombinations(s))