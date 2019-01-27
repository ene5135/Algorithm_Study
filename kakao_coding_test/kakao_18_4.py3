import heapq

def get_value(string): # 인코딩된 원소에서 value값만 가져온다.
    return int(string.split('_')[0])

def get_index(string): # 인코딩된 원소에서 최초 index값만 가져온다.
    return int(string.split('_')[1])

def solution(food_times, k):
    """
    food_times를 통해 min_heap을 구성하고
    (최소값 * food_times의length) 가 k보다 작거나 같으면 k에서 빼주고 food_times에서 다 먹은 음식으로 취급(0으로 만든다)
    (최소값 * food_times의length) 가 k보다 크면 종료 케이스로, length에서 k를 나눈 나머지를 구하여 남아있는 음식자리의 최초 인덱스를 구하여 반환한다.
    """

    if sum(food_times) <= k: # 트릭, 만약 모든 식사시간의 합이 k 보다 작으면 남는 음식은 없다.
        return -1

    # min_heap을 구성한다. 이때, 음식의 최초 자리를 기억하기 위해 다음과같이 인코딩 한다.
    # "0000000value_index"
    # 이때 food_time의 최대값이 100000000 이고, 스트링이 사전순서로 비교되므로 앞에 0을 남는갯수만큼 붙여준다.
    # [3,1,2] --> ["000000003_0","000000001_1","000000002_2"]
    min_heap = []
    for i in range(len(food_times)):
        min_heap.append("0"*(9-len(str(food_times[i])))+str(food_times[i])+"_"+str(i))

    # min_heap은 실제로 원소를 pop 시켜가며 진행하고, food_times는 pop시키지않고 heap으로 만들지도 않고 다 먹은 음식만 0으로 바꿔준다.
    food_times = min_heap[:]
    heapq.heapify(min_heap)
    # rotation은 식탁을 몇번 회전했는지를 기억한다.
    rotation = 0
    
    while(True):
        length = len(min_heap)
        min_val = get_value(min_heap[0]) - rotation # 매번 힙속의 실제 값을 마이너스 해줄 필요없이 min_val을 가져올때 rotation값을 빼준다.
        
        # 힙의 최소값 - 현재 식탁을 돌린 횟수가 0이란 말은 바로 전 단계에서 최소값이었던 음식의 값과 현재 최소값이 동일하다는 말이다. 그래서 그냥 추가조작없이 힙에서 빼주고 food_times에서 0으로 만든다.
        # [3,1,1,1,2] -> [2,0,0,0,1] 에서 1,1,1 과 같이 최소값이 여러개인 경우를 말한다.
        if min_val == 0:
            root = heapq.heappop(min_heap)
            food_times[get_index(root)] = 0
            continue
        
        # 최소값의 음식을 다 먹을 만큼 식탁을 회전해도 k가 남는 경우 그만큼 k에서 빼주고 식탁을 돌린 횟수를 추가시켜준다. 또한 최소값의 음식은 힙에서 pop되며 food_times에서 0으로 바꿔준다.
        elif min_val*length <= k:
            root = heapq.heappop(min_heap)
            k -= min_val*length
            rotation += min_val
            food_times[get_index(root)] = 0
            continue
            
        # 최소값의 음식을 다 먹을 만큼 식탁을 회전시킬 수 없을 경우, 즉 k초가 지나도 더이상 없어지는 음식이 없을경우 종료케이스로, 남은 음식의 갯수만큼 k에서 나눈 나머지의 인덱스 자리에 있는 음식의 최초 자리가 답이 된다. (이때 자리 = 인덱스+1)
        elif min_val*length > k:
            food_times = list(filter(None, food_times))            
            remain = k % length
            answer = get_index(food_times[remain]) + 1
            break
            
        else:
            print("error")
            
    return answer