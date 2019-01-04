step = [(1,0), (0,-1), (-1,0), (0,1)]

def rotate(points): # x->-y, y->x
    result = []
    rest, center = points[:-1], points[-1]
    for point in rest: # 회전 기준은 마지막점 = center
        pp_x = point[0] - center[0]
        pp_y = point[1] - center[1]
        
        pr_x = -pp_y
        pr_y = pp_x
        
        pp_x = pr_x + center[0]
        pp_y = pr_y + center[1]
        
        result.append((pp_x, pp_y))
        
    result.reverse() # 바로붙일수있게 마지막점은 뺴고, 뒤집어서 반환
        
    return result
        
def make_dragon(x,y,d,g):
    result = [(x,y), (x+step[d][0], y+step[d][1])]
    
    for n in range(g):
        result = result + rotate(result)
    
    return result

def check_square(point, point_dict):
    x, y = point[:]
    p1 = (x+1, y)
    p2 = (x+1, y+1)
    p3 = (x, y+1)

    v1 = point_dict.get(p1, 0)
    v2 = point_dict.get(p2, 0)
    v3 = point_dict.get(p3, 0)
    
    if v1+v2+v3 is 3:
        return True
    else:
        return False
    
def solution(N, dragons):
    #print(N, dragons)
    dragon_points = set([])
    for [x,y,d,g] in dragons:
        point_set = set(make_dragon(x,y,d,g))
        dragon_points = dragon_points | point_set
        
    point_dict = {}
    for point in dragon_points:
        point_dict[point] = 1
        
    count = 0
    for point in dragon_points:
        if check_square(point, point_dict):
            count = count + 1
    
    return count

    
            
    
if __name__ == '__main__':
    N = int(input())
    dragons = [list(map(int, input().split())) for _ in range(N)]

    result = solution(N, dragons)
    print(result)