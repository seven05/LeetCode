#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        answer = 0
        def fact(n):
            if n == 0 or n == 1:
                return 1
            return fact(n-1)*n
        for i in range(0,int(n/2)+1):
            a = n - i*2
            answer += fact(a+i)/(fact(a)*fact(i))
        return int(answer)

# @lc code=end

