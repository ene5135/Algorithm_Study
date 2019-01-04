
def simulation(N, H, ladder):
    for c in range(N):
        if c != simul_single_col(c, H, ladder):
            return False 
    return True
        
            
def simul_single_col(curr_col, H, ladder):
    for r in range(H):
        curr_col = curr_col + ladder[curr_col][r]
    
    return curr_col
    
def comb_ladders(N, H, ladder, more_line, start_idx):
    if more_line == 0:
        return simulation(N,H,ladder)
    
    for idx in range(start_idx, (N-1)*H):  
        a = idx % H
        b = idx // H
        if ladder[b][a] != 0 or ladder[b+1][a] != 0:
            continue
        else:
            ladder[b][a] = 1
            ladder[b+1][a] = -1
            if comb_ladders(N,H,ladder,more_line-1, idx+1):
                return True

            ladder[b][a] = 0
            ladder[b+1][a] = 0

    return False
    
def solution(N, H, ladder):   

    for i in range(4):

        if comb_ladders(N, H, ladder, i, 0):
            return i
    return -1
            
    
if __name__ == '__main__':
    N, M, H = map(int, input().split())
    ladder = [[0]*H for _ in range(N)]
    
    for _ in range(M):
        a, b = map(lambda y: int(y)-1, input().split())
        ladder[b][a] = 1 # 정방향
        ladder[b+1][a] = -1 # 역방향
        
    result = solution(N, H, ladder)
    print(result)

