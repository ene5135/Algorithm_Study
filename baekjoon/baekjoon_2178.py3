four_D = [(-1,0), (1,0), (0,-1), (0,1)]

def miro(N, M, maze):
    call_queue = [(1,1)]
    maze[1][1] = 1
    
    while(call_queue != []):
        call_queue = process_queue(call_queue, maze)
        
    return maze[N][M]
                
def process_queue(call_queue, maze):
    new_call_queue = call_queue.copy()
    for x, y in call_queue:
        curr_dist = maze[y][x]
        for x_D, y_D in four_D:
            next_x = x+x_D
            next_y = y+y_D
            if maze[next_y][next_x] == 0:
                maze[next_y][next_x] = curr_dist + 1
                new_call_queue.append((next_x, next_y))
                
        del new_call_queue[0]
                
    return new_call_queue

def transform(y):
    if y == '0':
        return -1
    else:
        return 0
        
if __name__ == '__main__':
    line = input().split()
    N = int(line[0])
    M = int(line[1])
    maze = [([-1]*(M+2))]+[[-1]+list(map(transform, list(input())))+[-1] for _ in range(N)]+[([-1]*(M+2))]

    result = miro(N, M, maze)
    print(result)