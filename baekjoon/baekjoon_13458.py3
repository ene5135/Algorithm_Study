import math as np

def solution(rooms, B, C):
    #print(rooms, B, C)
    result = 0
    for room in rooms:
        room -= B
        result += 1
        if room <= 0:
            continue
        result += np.ceil(room/C)
            
    return result
        

if __name__ == '__main__':
    N = int(input())
    rooms = list(map(int, input().split()))
    B, C = map(int, input().split())
    
    print(solution(rooms, B, C))
    