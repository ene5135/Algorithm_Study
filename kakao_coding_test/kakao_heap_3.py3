import heapq

def solution(jobs):
    start = 0
    answer = 0
    min_heap = list(map(lambda x: (x[1],x[0]), jobs))
    heapq.heapify(min_heap)
    total = 0
    temp = []
    while(True):
        if min_heap == []:
            if temp == []:
                break
            start += 1
            heapq.heapify(temp)
            min_heap = temp
            temp = []
        minimum = heapq.heappop(min_heap)
        if minimum[1] <= start:
            total += minimum[0] + (start-minimum[1])
            start += minimum[0]
            for t in temp:
                heapq.heappush(min_heap, t)
            temp = []
        else:
            temp.append(minimum)
            
    return int(total/len(jobs))