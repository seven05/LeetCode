#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        answer = 0
        rti = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for i in range(len(s)-1):
            if rti[s[i]] < rti[s[i+1]]:
                answer = answer - rti[s[i]]
            else:   
                answer = answer + rti[s[i]]
        answer += rti[s[-1]]
        return answer
# @lc code=end

