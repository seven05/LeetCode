# 56. Merge Intervals
#https://leetcode.com/problems/merge-intervals/description/
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x : x[0])
        # print(intervals)
        answer = []
        for s,e in intervals:
            # print(s,e)
            if len(answer) == 0:
                answer.append([s,e])
                continue
        # print(answer[-1])
            if answer[-1][1] >= s:
                if  answer[-1][1] < e:
                    answer[-1][1] = e
            else:
                answer.append([s,e])    
        # print(answer)
        return answer
