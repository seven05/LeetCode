#22. Generate Parentheses
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        def backtrack(curr: str, o_cnt: int, c_cnt: int):
            if len(curr) == 2 * n:
                answer.append(curr)
                return
            if o_cnt < n:
                backtrack(curr + '(', o_cnt + 1, c_cnt)
            if c_cnt < o_cnt:
                backtrack(curr + ')', o_cnt, c_cnt + 1)
        backtrack("", 0, 0)
        return answer