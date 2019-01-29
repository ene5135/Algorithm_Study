import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while(True):
        minimum = heapq.heappop(scoville)
        if minimum >= K:
            return answer
        if scoville == []:
            return -1
        minimum += heapq.heappop(scoville)*2
        heapq.heappush(scoville, minimum)
        answer += 1
        
    return answer