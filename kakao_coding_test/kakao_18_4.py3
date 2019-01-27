import heapq

def get_value(string): # ���ڵ��� ���ҿ��� value���� �����´�.
    return int(string.split('_')[0])

def get_index(string): # ���ڵ��� ���ҿ��� ���� index���� �����´�.
    return int(string.split('_')[1])

def solution(food_times, k):
    """
    food_times�� ���� min_heap�� �����ϰ�
    (�ּҰ� * food_times��length) �� k���� �۰ų� ������ k���� ���ְ� food_times���� �� ���� �������� ���(0���� �����)
    (�ּҰ� * food_times��length) �� k���� ũ�� ���� ���̽���, length���� k�� ���� �������� ���Ͽ� �����ִ� �����ڸ��� ���� �ε����� ���Ͽ� ��ȯ�Ѵ�.
    """

    if sum(food_times) <= k: # Ʈ��, ���� ��� �Ļ�ð��� ���� k ���� ������ ���� ������ ����.
        return -1

    # min_heap�� �����Ѵ�. �̶�, ������ ���� �ڸ��� ����ϱ� ���� ���������� ���ڵ� �Ѵ�.
    # "0000000value_index"
    # �̶� food_time�� �ִ밪�� 100000000 �̰�, ��Ʈ���� ���������� �񱳵ǹǷ� �տ� 0�� ���°�����ŭ �ٿ��ش�.
    # [3,1,2] --> ["000000003_0","000000001_1","000000002_2"]
    min_heap = []
    for i in range(len(food_times)):
        min_heap.append("0"*(9-len(str(food_times[i])))+str(food_times[i])+"_"+str(i))

    # min_heap�� ������ ���Ҹ� pop ���Ѱ��� �����ϰ�, food_times�� pop��Ű���ʰ� heap���� �������� �ʰ� �� ���� ���ĸ� 0���� �ٲ��ش�.
    food_times = min_heap[:]
    heapq.heapify(min_heap)
    # rotation�� ��Ź�� ��� ȸ���ߴ����� ����Ѵ�.
    rotation = 0
    
    while(True):
        length = len(min_heap)
        min_val = get_value(min_heap[0]) - rotation # �Ź� ������ ���� ���� ���̳ʽ� ���� �ʿ���� min_val�� �����ö� rotation���� ���ش�.
        
        # ���� �ּҰ� - ���� ��Ź�� ���� Ƚ���� 0�̶� ���� �ٷ� �� �ܰ迡�� �ּҰ��̾��� ������ ���� ���� �ּҰ��� �����ϴٴ� ���̴�. �׷��� �׳� �߰����۾��� ������ ���ְ� food_times���� 0���� �����.
        # [3,1,1,1,2] -> [2,0,0,0,1] ���� 1,1,1 �� ���� �ּҰ��� �������� ��츦 ���Ѵ�.
        if min_val == 0:
            root = heapq.heappop(min_heap)
            food_times[get_index(root)] = 0
            continue
        
        # �ּҰ��� ������ �� ���� ��ŭ ��Ź�� ȸ���ص� k�� ���� ��� �׸�ŭ k���� ���ְ� ��Ź�� ���� Ƚ���� �߰������ش�. ���� �ּҰ��� ������ ������ pop�Ǹ� food_times���� 0���� �ٲ��ش�.
        elif min_val*length <= k:
            root = heapq.heappop(min_heap)
            k -= min_val*length
            rotation += min_val
            food_times[get_index(root)] = 0
            continue
            
        # �ּҰ��� ������ �� ���� ��ŭ ��Ź�� ȸ����ų �� ���� ���, �� k�ʰ� ������ ���̻� �������� ������ ������� �������̽���, ���� ������ ������ŭ k���� ���� �������� �ε��� �ڸ��� �ִ� ������ ���� �ڸ��� ���� �ȴ�. (�̶� �ڸ� = �ε���+1)
        elif min_val*length > k:
            food_times = list(filter(None, food_times))            
            remain = k % length
            answer = get_index(food_times[remain]) + 1
            break
            
        else:
            print("error")
            
    return answer