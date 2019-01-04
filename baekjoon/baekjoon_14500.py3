TETS = [
    # +x, +y
    [(0,0), (1,0), (0,1), (1,1)], # ㅁ
    [(0,0), (1,0), (2,0), (3,0)], # ㅡ
    [(0,0), (0,1), (0,2), (1,2)], # ㄴ
    [(0,0), (0,1), (1,1), (1,2)], # ㄹ
    [(0,0), (1,0), (1,1), (2,0)] # ㅗ
]

def rotation(blocks):
    result = blocks.copy()
    for block in blocks:
        block_90 = list(map(lambda z: (-z[1],z[0]), block)) # x->y, y->-x
        block_180 = list(map(lambda z: (-z[0],-z[1]), block)) # x->-x, y->-y
        block_270 = list(map(lambda z: (z[1],-z[0]), block)) # x->y, y->-x
        result = result + [block_90, block_180, block_270]
    return result

def sym(blocks):
    result = blocks.copy()
    for block in blocks:
        x_sym_block = list(map(lambda z: (-z[0],z[1]), block)) # x->-x, y->y
        y_sym_block = list(map(lambda z: (z[0],-z[1]), block)) # x->x, y->-y
        result.append(x_sym_block)
        result.append(y_sym_block)
    return result

def block_to_str(block):
    result = ""
    min_x = 0
    min_y = 0
    for p in block:
        if p[0] < min_x:
            min_x = p[0]
        if p[1] < min_y:
            min_y = p[1]
    aligned_block = list(map(lambda p: (p[0]+abs(min_x), p[1]+abs(min_y)), block))
    
    aligned_block.sort(key=lambda y: str(y[0])+str(y[1]))
   
    return str(aligned_block)

    

def solution(N, M, board):
    #print(N,M,board)
    #board[y][x]
    
    # 19개의 블록 케이스 정리
    block_cases = set(list(map(block_to_str, sym(rotation(TETS))))) # 회전, 대칭 결과에서 중복 없에기
    block_cases = list(map(eval, block_cases)) # 스트링으로 된거 다시 리스트 타입으로
    
    # 여기가 time dominant part
    # for문 안에서 쓸대없는짓하면 시간초과됨
    max_result = 0
    for x in range(M):
        for y in range(N):
            for case in block_cases:
                block_sum = 0
                for p in case:
                    new_x = x+p[0]
                    new_y = y+p[1]
                    if new_x >= M or new_y >= N:
                        break
                    block_sum = block_sum + board[new_y][new_x]
                if block_sum > max_result:
                    max_result = block_sum       

                        
    return max_result

if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    board = [list(map(int, input().split())) for _ in range(N)]
    
    result = solution(N, M, board)
    print(result)
        
