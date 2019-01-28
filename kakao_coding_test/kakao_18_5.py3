import sys
sys.setrecursionlimit(10**6)

tree_dict = {}
def get_root(nodeinfo):
    maximum = -1
    max_index = -1
    for i in range(len(nodeinfo)):
        if nodeinfo[i][1] > maximum:
            maximum = nodeinfo[i][1]
            max_index = i
    if max_index == -1:
        return (-1,-1)
    return nodeinfo[max_index][0], nodeinfo[max_index][2]

def make_tree(nodeinfo):
    if nodeinfo == []:
        return
    # 모든 노드는 x좌표로 유니크하게 구분함
    root = get_root(nodeinfo)
    left = list(filter(lambda x: x[0] < root[0], nodeinfo))
    right = list(filter(lambda x: x[0] > root[0], nodeinfo))
    left_root = get_root(left)
    right_root = get_root(right)
    tree_dict[root[1]] = [left_root[1], right_root[1]]
    
    make_tree(left)
    make_tree(right)
    return
    
def pre_order(current):
    if current == -1:
        return []
    left = tree_dict[current][0]
    right = tree_dict[current][1]
    result = [current] + pre_order(left) + pre_order(right)
    return result

def post_order(current):
    if current == -1:
        return []
    left = tree_dict[current][0]
    right = tree_dict[current][1]
    result = post_order(left) + post_order(right) + [current]
    return result

def solution(nodeinfo):
    answer = [[]]
    nodeinfo = [val + [idx+1] for idx,val in enumerate(nodeinfo)]
    make_tree(nodeinfo)
    root = get_root(nodeinfo)[1]
    answer = [pre_order(root), post_order(root)]
    return answer
