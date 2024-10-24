#456. 132 Pattern

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        stack = []
        third = -1000000001 
        for i in range(n - 1, -1, -1):
            if nums[i] < third:
                return True  
            while stack and stack[-1] < nums[i]:
                third = stack.pop() 
            stack.append(nums[i])
        return False

# 시간초과
# class Solution:
#     def find132pattern(self, nums: List[int]) -> bool:
#         n = len(nums)
#         for i in range(n):
#             for j in range(i+1,n):
#                 for k in range(j+1,n):
#                     if nums[i] < nums[k] and nums[k] < nums[j]:
#                         return True
#         return False