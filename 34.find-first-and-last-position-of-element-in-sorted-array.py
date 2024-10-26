#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        first = -1
        last = -1
        for i in range(len(nums)):
            if nums[i] == target:
                if first == -1:
                    first = i
                    last = i
                else:
                    last = i
        return [first,last]
# @lc code=end

