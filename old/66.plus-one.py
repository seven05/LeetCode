#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        answer = []
        n = len(digits)
        num = 0
        for i in range(n):
            temp = digits[i]
            for _ in range(n-i-1):
                temp *= 10
            num += temp
        # print(num)
        num += 1
        while num > 0 :
            answer.insert(0,num%10)
            num = num // 10
        return answer

        
# @lc code=end