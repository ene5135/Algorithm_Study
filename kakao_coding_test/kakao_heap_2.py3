import heapq
import sys
sys.setrecursionlimit(10**6)

"""
DFS 버전, 시간초과

def DFS(stock, dates, supplies, k, count, past):
    if k <= stock:
        return count
    if dates == []:
        return 20001
    
    gone = dates[0] - past
    stock = stock - gone
    k = k - gone

    if stock < 0:
        return 20001
    return min(DFS(stock+supplies[0], dates[1:], supplies[1:], k, count+1, dates[0]), DFS(stock, dates[1:], supplies[1:], k, count, dates[0]))

def solution(stock, dates, supplies, k):
    answer = DFS(stock, dates, supplies, k, 0, 0)
    return answer
"""

def solution(stock, dates, supplies, k):
    max_heap = list(zip(list(map(lambda x: -x, supplies)), dates))
    heapq.heapify(max_heap)
    temp = []
    answer = 0
    while(True):
        if stock >= k:
            return answer
        maximum = heapq.heappop(max_heap)
        if maximum[1] <= stock:
            stock += -maximum[0]
            for t in temp:
                heapq.heappush(max_heap, t)
            temp = []
            answer += 1
        else:
            temp.append(maximum)
    return 0
    
    