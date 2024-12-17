class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        max_len = 0
        start = 0
        for i in range(len(s)):
            if s[i] in window:
                start = max(start,window[s[i]]+1)
            window[s[i]] = i
            max_len = max(max_len,i-start+1)
        return max_len
        