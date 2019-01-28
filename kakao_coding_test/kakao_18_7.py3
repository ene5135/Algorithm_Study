def check_point(board, x, y):
    """
    해당 좌표점에서 가로방향으로 2x3 사각형이나 세로방향으로 3x2 사각형 속에
    검은블록이 2개 같은숫자가 4개 인 경우가 있는지 확인
    """
    horizon = []
    vertical = []
    if x+2 < len(board) and y+1 < len(board):
        horizon = board[y][x:x+3] + board[y+1][x:x+3]
    if y+2 < len(board) and x+1 < len(board):
        vertical = board[y][x:x+2] + board[y+1][x:x+2] + board[y+2][x:x+2]
    
    block_num = 0
    black_count = 0
    block_count = 0
    for point in horizon:
        if point == -2:
            break
        if point == -1:
            black_count += 1
        elif point == block_num:
            block_count += 1
        elif point != block_num and block_num == 0:
            block_num = point
            block_count += 1
    
    if black_count == 2 and block_count == 4:
        return "horizon"
    
    block_num = 0
    black_count = 0
    block_count = 0
    for point in vertical:
        if point == -2:
            break
        if point == -1:
            black_count += 1
        elif point == block_num:
            block_count += 1
        elif point != block_num and block_num == 0:
            block_num = point
            block_count += 1    
    
    if black_count == 2 and block_count == 4:
        return "vertical"
    
    return None
    
def fill_the_board(board, start_col, end_col):
    for col in range(start_col, end_col):
        fill_number = -1
        for row in range(len(board)):
            if board[row][col] <= 0:
                board[row][col] = fill_number # 드랍가능지역 = -1, 불가지역 = -2
            else:
                fill_number = -2
    return board

def solution(board):
    board = fill_the_board(board, 0, len(board))
    count = 0
    for row_idx in range(len(board)):
        for col_idx in range(len(board)):
            check = check_point(board, col_idx, row_idx)
            if check: # 지울 수 있으면 지우고 다시 검정블럭 비를 내린 후 처음부터 보드를 다시 탐색한다.
                print(col_idx, row_idx)
                if check == "horizon":
                    for j in range(2):
                        for i in range(3):
                            board[row_idx+j][col_idx+i] = 0
                    fill_the_board(board, col_idx, col_idx+3)
                else:
                    for j in range(3):
                        for i in range(2):
                            board[row_idx+j][col_idx+i] = 0
                    fill_the_board(board, col_idx, col_idx+2)
                count += 1
                return solution(board) + 1
    answer = count
    return answer