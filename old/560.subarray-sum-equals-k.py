#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#
# https://leetcode.com/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (44.27%)
# Likes:    22062
# Dislikes: 689
# Total Accepted:    1.4M
# Total Submissions: 3.3M
# Testcase Example:  '[1,1,1]\n2'
#
# Given an array of integers nums and an integer k, return the total number of
# subarrays whose sum equals to k.
# 
# A subarray is a contiguous non-empty sequence of elements within an array.
# 
# 
# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:
# Input: nums = [1,2,3], k = 3
# Output: 2
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 2 * 10^4
# -1000 <= nums[i] <= 1000
# -10^7 <= k <= 10^7
# 
# 
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {0: 1}
        current_sum = 0
        count = 0

        for num in nums:
            current_sum += num
            
            if current_sum - k in prefix_sum:
                count += prefix_sum[current_sum - k]
            
            if current_sum in prefix_sum:
                prefix_sum[current_sum] += 1
            else:
                prefix_sum[current_sum] = 1

        return count
        
# @lc code=end

