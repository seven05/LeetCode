class Solution:
    def reverse(self, x: int) -> int:
        is_minus = False
        if x < 0 :
            is_minus = True
        reversed_num = 0
        tmp = abs(x)
        while tmp > 0:
            reversed_num = reversed_num * 10 + tmp % 10
            tmp = tmp // 10
        if is_minus:
            reversed_num = reversed_num * (-1)
        if -2147483648 < reversed_num and reversed_num < 2147483647:
            return reversed_num
        else:
            return 0