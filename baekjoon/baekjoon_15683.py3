four_D = [(1,0), (0,-1), (-1,0), (0, 1)]

def mark(r, c, d, N, M, office, mode): # d = 1 정방향 or -1 역방향
    # mode = 1 : 지우기, -1 : 마크하기
    while(True):
        c = c+four_D[d][0]
        r = r+four_D[d][1]
        if c >= M or c < 0 or r >= N or r < 0:
            return
        elif office[r][c] == 6:
            return
        elif office[r][c] <= 0:
            office[r][c] = office[r][c] + mode

def get_blind_spot(office):
    count = 0
    for row in office:
        count = count + row.count(0)
    return count
            
def retrieve(N, M, office, curr_idx):
    result = 999
 
    for idx in range(curr_idx, N*M):
        r = idx // M
        c = idx % M
        cctv_type = office[r][c]
        if cctv_type == 1:
            for d in range(4):
                mark(r, c, d, N, M, office, -1) # 마킹
                result = min(result, retrieve(N, M, office, idx+1))
                mark(r, c, d, N, M, office, 1) # 언마킹
            return result
        elif cctv_type == 2:
            for d in range(2):
                mark(r, c, d, N, M, office, -1) # 마킹
                mark(r, c, d+2, N, M, office, -1) # 마킹
                result = min(result, retrieve(N, M, office, idx+1))       
                mark(r, c, d, N, M, office, 1) # 언마킹
                mark(r, c, d+2, N, M, office, 1) # 언마킹
            return result
        elif cctv_type == 3:
            for d in range(4):
                mark(r, c, d, N, M, office, -1) 
                mark(r, c, (d+1)%4, N, M, office, -1) 
                result = min(result, retrieve(N, M, office, idx+1))
                mark(r, c, d, N, M, office, 1) 
                mark(r, c, (d+1)%4, N, M, office, 1) 
            return result
        elif cctv_type == 4:
            for d in range(4):
                mark(r, c, d, N, M, office, -1) 
                mark(r, c, (d+1)%4, N, M, office, -1)
                mark(r, c, (d+2)%4, N, M, office, -1)
                result = min(result, retrieve(N, M, office, idx+1))
                mark(r, c, d, N, M, office, 1) 
                mark(r, c, (d+1)%4, N, M, office, 1) 
                mark(r, c, (d+2)%4, N, M, office, 1) 
            return result
        elif cctv_type == 5:
            for d in range(4):
                mark(r, c, d, N, M, office, -1) 
            result = retrieve(N, M, office, idx+1)
            for d in range(4):
                mark(r, c, d, N, M, office, 1)
            return result
              
    return get_blind_spot(office)
         
            
def solution(N, M, office):
    #print(N, M, office)
    #mark_col(2,0,-1,N,M,office)
    #for r in office:
    #    print(r)
    
    result = retrieve(N, M, office, 0)
    
    return result
            
    
    
if __name__ == '__main__':
    N, M = map(int, input().split())
    office = [list(map(int, input().split())) for _ in range(N)]
    
    result = solution(N, M, office)
    print(result)

