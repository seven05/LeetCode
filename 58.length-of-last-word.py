#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        # print(s)
        for i in range(len(s)-1,-1,-1):
            # print(f"s{i}: {s[i]}\n")
            if s[i] == ' ':
                # print("test")
                return len(s)-i-1
        return len(s)
# @lc code=end

