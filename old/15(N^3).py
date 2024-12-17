# 3sum
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        n_len = len(nums)
        nums.sort()
        for i in range(n_len):
            if i >0 and nums[i] == nums[i-1]:
                continue
            for j in range(i + 1, n_len):
                if j >i+1 and nums[j] == nums[j-1]:
                    continue
                for k in range(j + 1, n_len):
                    if k >j+1 and nums[k] == nums[k-1]:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        answer.append([nums[i], nums[j], nums[k]])
        return answer