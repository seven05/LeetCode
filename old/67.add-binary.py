#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l_a = len(a)
        l_b = len(b)
        n_a = 0
        n_b = 0
        mult_numa = 1
        mult_numb = 1
        for i in range(l_a-1,-1,-1):
            n_a += int(a[i]) * mult_numa
            mult_numa *= 2
        print(n_a)
        for j in range(l_b-1,-1,-1):
            n_b += int(b[j]) * mult_numb
            mult_numb *= 2
        print(n_b)
        answer_int = n_a + n_b
        print(answer_int)
        if answer_int == 0:
            return "0"
        answer = ""
        while answer_int > 0:
            temp = answer_int % 2
            answer = str(temp) + answer
            answer_int = answer_int // 2
        return answer
        
# @lc code=end

