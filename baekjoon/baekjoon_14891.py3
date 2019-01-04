def rotate(gears, n, d):
    gear = gears[n-1]
    if d == 1:
        new_gear = [gear[-1]] + gear[:len(gear)-1]
    else:
        new_gear = gear[1:] + [gear[0]]
        
    gears[n-1] = new_gear
        
def process(gears, n, d, prev):
    if n == 0 or n == 5:
        return
    curr_gear = gears[n-1]
    prev_gear = gears[n-1+prev]
    
    if curr_gear[2 * prev] != prev_gear[(-2) * prev]:
        process(gears, n-prev, -d, prev)
        rotate(gears, n, d)


def solution(gears, rotations):
    #print(gears, rotations)
    result = 0
    for n, d in rotations:
        process(gears, n-1, -d, 1)
        process(gears, n+1, -d, -1)
        rotate(gears, n, d)
        #for i in range(4):
        #    print(''.join(map(str,gears[i])))
    
    for i in range(4):
        #print(gears[i])
        result += gears[i][0] * 2**i
        
    return result
        

if __name__ == '__main__':
    gears = []
    for i in range(4):
        gears.append(list(map(int, list(input()))))
    
    K = int(input())
    rotations = [list(map(int, input().split())) for _ in range(K)]
    
    print(solution(gears, rotations))
    