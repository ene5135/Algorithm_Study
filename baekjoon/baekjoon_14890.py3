def check_row(i, L, board):
    row = board[i][1:]
    curr_h = board[i][0]
    n_more_blocks = 0
    n_continuous_blocks = 1
    
    for h in row:
        if n_more_blocks != 0:
            if curr_h != h:
                return False
            n_more_blocks -= 1
            continue
        
        if curr_h - h == 1: # 하강 경사
            curr_h = h
            n_more_blocks = L - 1
            n_continuous_blocks = 0
            continue

        elif curr_h - h == -1: # 상승 경사
            if n_continuous_blocks >= L:
                n_continuous_blocks = 1
                curr_h = h
                continue
            else:
                return False
        
        
        elif curr_h == h:
            n_continuous_blocks += 1
            continue
        
        else: # 두칸이상 차이
            return False

    if n_more_blocks != 0: # 경사로 짓다가 말았으면
        return False
    
    return True
        
def trans(N, board):
    result = []
    for i in range(N):
        result.append([row[i] for row in board])
    
    return result
    
def solution(N, L, board):
    #print(N, L, board)
    count = 0
    board_trans = trans(N, board)
    for i in range(N):
        #print("i", i, "row", check_row(i, L, board), "col", check_row(i, L, board_trans))
        
        if check_row(i, L, board):
            count += 1
        if check_row(i, L, board_trans):
            count += 1
            
    return count


if __name__ == '__main__':
    N, L = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    
    print(solution(N, L, board))
    