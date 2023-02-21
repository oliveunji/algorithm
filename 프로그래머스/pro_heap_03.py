import heapq


def solution(operations):
    heap = []
    for op in operations:
        command, num = op.split()
        if command == "I":
            heapq.heappush(heap, int(num))
        elif command == "D":
            if len(heap) == 0:
                continue
            if num == "-1":
                heapq.heappop(heap)
            else:
                heap = heapq.nlargest(len(heap), heap)[1:]
                heapq.heapify(heap)
    if len(heap) == 0:
        return [0, 0]
    else:
        return [max(heap), min(heap)]
