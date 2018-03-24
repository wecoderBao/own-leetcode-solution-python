"""
You are given a string, s, and a list of words, words, that are all of the same length.
Find all starting indices of substring(s) in s that is a concatenation of each word
in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
"""


class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # 如果单词个数大于字符串长度 结果显然为空
        if len(words) > len(s):
            return []
        d = {}
        total = len(words)
        for word in words:
            d[word] = d.get(word, 0) + 1

        gap = len(words[0])
        ans = []
        for i in range(len(s)):
            head = i
            start = i
            end = start + gap
            dd = {}
            cnt = 0
            while end <= len(s) and s[start:end] in d:
                key = s[start:end]
                dd[key] = dd.get(key, 0) + 1
                # 单词出现次数有限制，总的单词数有限制，两者都满足则找到
                if dd[key] <= d[key]:
                    cnt += 1
                else:
                    break
                start += gap
                end += gap
            if cnt == total:
                ans.append(head)
        return ans


if __name__ == '__main__':
    s = Solution()
    str = 'barfoothefoobarman'
    words = ["foo", "bar"]
    print(s.findSubstring(str, words))