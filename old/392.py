#https://leetcode.com/submissions/detail/1431514466/
#Is Subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        num = len(s)
        if num == 0:
            return True
        n = len(t)
        s_index = 0
        for i in range(n):
            if s[s_index] == t[i]:
                s_index += 1
            if s_index == num:
                return True
        return False