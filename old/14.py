# Longest Common Prefix
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        min_len = min(len(s) for s in strs)
        common_prefix = ""
        for i in range(min_len):
            curr_char = strs[0][i]
            if all(s[i] == curr_char for s in strs):
                common_prefix += curr_char
            else:
                break
        return common_prefix