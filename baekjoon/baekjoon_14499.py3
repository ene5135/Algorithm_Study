# EAST, WEST, NORTH, SOUTH = '1', '2', '3', '4'
    
def solution(y_limit, x_limit, y, x, my_map, comds):
    #print(y_limit, x_limit, y, x, my_map, comds)
    #print(my_map[y][x])
    curr_x = x
    curr_y = y
    
    """
    dice shape
      2
    4 1 3
      5
      6
    """
    shape_dict = {
        'east': 3,
        'west': 4,
        'north': 2,
        'south': 5,
        'opp': 6,
        'curr': 1
    }
    
    """
    remember dice value of each side
    """
    value_dict = {
        1: '0',
        2: '0',
        3: '0',
        4: '0',
        5: '0',
        6: '0'
    }
    
    """
    iterate all commands
    """
    for direction in comds:
        if direction == '1': # move east
            if curr_x == x_limit: # if dice can not move east
                continue        
                
            # update current x
            curr_x = curr_x + 1
            
            # new dice shape after moving
            new_east = shape_dict['opp']
            new_west = shape_dict['curr']
            new_north = shape_dict['north']
            new_south = shape_dict['south']
            new_curr = shape_dict['east']
            new_opp = shape_dict['west']
        
        elif direction == '2': # move west
            if curr_x == 0:
                continue
            curr_x = curr_x - 1
            
            new_east = shape_dict['curr']
            new_west = shape_dict['opp']
            new_north = shape_dict['north']
            new_south = shape_dict['south']
            new_curr = shape_dict['west']
            new_opp = shape_dict['east']

        elif direction == '3': # move north
            if curr_y == 0:
                continue
            curr_y = curr_y - 1
            
            new_east = shape_dict['east']
            new_west = shape_dict['west']
            new_north = shape_dict['opp']
            new_south = shape_dict['curr']
            new_curr = shape_dict['north']
            new_opp = shape_dict['south']

        elif direction == '4': # move south
            if curr_y == y_limit:
                continue
            curr_y = curr_y + 1
            
            new_east = shape_dict['east']
            new_west = shape_dict['west']
            new_north = shape_dict['curr']
            new_south = shape_dict['opp']
            new_curr = shape_dict['south']
            new_opp = shape_dict['north']

        # update dice shape
        shape_dict['east'] = new_east
        shape_dict['west'] = new_west
        shape_dict['north'] = new_north
        shape_dict['south'] = new_south
        shape_dict['curr'] = new_curr
        shape_dict['opp'] = new_opp    
        
        # update dice value and map value
        if my_map[curr_y][curr_x] == '0':
            my_map[curr_y][curr_x] = value_dict[shape_dict['curr']]      
        else:
            value_dict[shape_dict['curr']] = my_map[curr_y][curr_x]
            my_map[curr_y][curr_x] = '0'
        
        # print opposite side value
        print(value_dict[shape_dict['opp']])

#if __name__ == '__main__':
    
N, M, y, x, comd_num = [int(elt) for elt in input().split()]
my_map = [input().split() for i in range(N)]
comds = input().split()
    
solution(N-1, M-1, y, x, my_map, comds)
        