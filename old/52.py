#52.N-QueensII
class Solution:
    def totalNQueens(self, n: int) -> int:
        pos = [0]*n
        flag_row = [False]*n
        flag_plus = [False]*((n*2)+1)
        flag_minus = [False]*((n*2)+1)
        globals()['count'] =0
        def q_set(i: int) -> None:
            """i 열의 알맞은 위치에 퀸을 배치"""
            for j in range(n):
                if(     not flag_row[j]            # j행에 퀸이 배치 되지 않았다면
                    and not flag_plus[i + j]        # 대각선 방향(↙↗)으로 퀸이 배치 되지 않았다면
                    and not flag_minus[i - j + n-1]):  # 대각선 방향( ↘↖)으로 퀸이 배치 되지 않았다면
                    pos[i] = j  # 퀸을 j행에 배치
                    if i == n-1:  # 모든 열에 퀸을 배치하는 것을 완료
                        globals()['count'] += 1
                    else:
                        flag_row[j] = flag_plus[i + j] = flag_minus[i - j + n-1] = True
                        q_set(i + 1)  # 다음 열에 퀸을 배치
                        flag_row[j] = flag_plus[i + j] = flag_minus[i - j + n-1] = False
        q_set(0)
        return count