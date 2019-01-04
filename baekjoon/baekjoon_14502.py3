four_D = [(1,0), (0,1), (-1,0), (0,-1)]

def _check(r, c, board, check_dict):
    
    result = 1
    for d_r, d_c in four_D:
        next_r = r+d_r
        next_c = c+d_c
        if board[next_r][next_c] == 0 and check_dict.get((next_r, next_c), True):
            check_dict[(next_r, next_c)] = False
            result += _check(next_r, next_c, board, check_dict)
    
    return result

def check(N, M, virus_list, board, num_of_wall):
    check_dict = {}
    result = 0
    for r,c in virus_list:
        if board[r][c] == 2:
            result += _check(r,c,board,check_dict)
    return N*M - num_of_wall - result

def find_max_safe_zone(N, M, curr_idx, more_wall, board, virus_list, num_of_wall):
    if more_wall == 0:
        return check(N, M, virus_list, board, num_of_wall)
    result = 0
    
    for idx in range(curr_idx, N*M):
        r = (idx // M) +1
        c = (idx % M) +1
        if board[r][c] == 0:
            board[r][c] = 1
            result = max(result, find_max_safe_zone(N,M,idx+1,more_wall-1,board,virus_list,num_of_wall+1))
            board[r][c] = 0
            
    return result
        

def solution(N, M, board):
    #print(N, M, board)

    virus_list = []
    num_of_wall = 0
    for r in range(1,N+1):
        for c in range(1,M+1):
            if board[r][c] == 1:
                num_of_wall += 1
            elif board[r][c] == 2:
                virus_list.append((r,c))

    #print(check(N,M,virus_list,board, num_of_wall))
    result = find_max_safe_zone(N, M, 0, 3, board, virus_list, num_of_wall)
    
    return result 
    
if __name__ == '__main__':
    N, M = map(int, input().split())
    wall = [[1]*(M+2)]
    board = wall+[[1]+list(map(int, input().split()))+[1] for _ in range(N)]+wall
    
    result = solution(N,M,board)
    print(result)
    