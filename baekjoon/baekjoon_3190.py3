
from collections import OrderedDict
four_D = [(0,1), (1,0), (0,-1), (-1,0)]


def draw(board, snake_dict):
    for key, value in snake_dict.items():
        board[key[0]][key[1]] = 7

def solution(N, board, commands):
    #print(N,board,commands)

    snake_dict = OrderedDict()
    snake_dict[(1,1)] = True
    
    curr_r, curr_c = 1, 1
    curr_d = 0
    time = 0

    while(True):
        
        command = commands.get(time, None)
        if command is not None:
            if command == 'L':
                curr_d = (curr_d-1) % 4
            elif command == 'D':
                curr_d = (curr_d+1) % 4
                
        next_r = curr_r + four_D[curr_d][0]
        next_c = curr_c + four_D[curr_d][1]
        
        if board[next_r][next_c] == 1:
            return time+1
        elif snake_dict.get((next_r,next_c), False):
            return time+1
        elif board[next_r][next_c] == 0:
            snake_dict.popitem(False)
        elif board[next_r][next_c] == 2:
            board[next_r][next_c] = 0
        
        snake_dict[(next_r,next_c)] = True
        curr_c = next_c
        curr_r = next_r
        
        time += 1
        
    
if __name__ == '__main__':
    N = int(input())
    wall = [[1]*(N+2)]
    board = wall+[[1]+[0 for _ in range(N)]+[1] for _ in range(N)]+wall
    K = int(input())
    for _ in range(K):
        r, c = map(int, input().split())
        board[r][c] = 2 # apple
    L = int(input())
    commands = {}
    for _ in range(L):
        time, dir = input().split()
        commands[int(time)] = dir
    result = solution(N, board, commands)
    print(result)
    
    