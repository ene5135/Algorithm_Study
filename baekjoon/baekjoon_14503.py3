four_D = [0,1,2,3] # NORTH,EAST,SOUTH,WEST
step = [(0,-1), (1,0), (0,1), (-1,0)] # NORTH,EAST,SOUTH,WEST

EMPTY,WALL,CLEAN = [0,1,2]

def solution(N, M, x, y, d, board):
    #print(N,M,x,y,d,board)
    state = 1
    count = 0
    while(True):
        if state is 1:
            board[y][x] = CLEAN
            state = 2
            count = count + 1
            #print(x,y)
            continue
        elif state is 2:
            found = False
            for i in range(1, 5):
                left = (d-i)%4
                left_x = x + step[left][0]
                left_y = y + step[left][1]
                if board[left_y][left_x] is EMPTY:
                    d = left
                    x = left_x
                    y = left_y
                    state = 1
                    found = True
                    break
            if not found:
                back = (d-2)%4
                back_x = x + step[back][0]
                back_y = y + step[back][1]
                if board[back_y][back_x] is WALL:
                    break
                else:
                    x = back_x
                    y = back_y
    
    
    return count
                


if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    y, x, d = list(map(int, input().split())) 
    board = [list(map(int, input().split())) for _ in range(N)]
    
    result = solution(N, M, x, y, d, board)
    print(result)
