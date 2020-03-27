import heapq

class CompareAble:
    def __init__(self, number, priority):
        self.number = number
        self.priority = priority
    def __lt__(self, other):
        return self.priority < other.priority

def CheckFit(data):
    ss = 0
    tmp = data.priority
    while tmp > 0:
        ss += tmp%10
        tmp = tmp//10
    
    return ss == data.number


heap = []
heapq.heappush(heap, CompareAble(2, 4))

nNumber = 3
#n = 10
n = 30

index = 0
while index < n:
    front = heapq.nsmallest(1, heap)
    # 边界限制
    if nNumber < 300 and front[0].priority > nNumber * nNumber:
        heapq.heappush(heap, CompareAble(nNumber, nNumber * nNumber))
        nNumber += 1
    else:
        if front[0].priority >= 10 and CheckFit(front[0]):
            index += 1
            print(index, front[0].number, front[0].priority)

        heapq.heappop(heap)
        heapq.heappush(heap, CompareAble(front[0].number, front[0].priority*front[0].number))
    #if len(heap) % 1000 == 0:
    #    print(len(heap))
