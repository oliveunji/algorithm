# import heapq


# def solution(operations):
#     heap = []
#     for op in operations:
#         command, num = op.split()
#         if command == "I":
#             heapq.heappush(heap, int(num))
#         elif command == "D":
#             if len(heap) == 0:
#                 continue
#             if num == "-1":
#                 heapq.heappop(heap)
#             else:
#                 heap = heapq.nlargest(len(heap), heap)[1:]
#                 heapq.heapify(heap)
#     if len(heap) == 0:
#         return [0, 0]
#     else:
#         return [max(heap), min(heap)]

import heapq


def solution(operations):
    min_q = []
    max_q = []
    for op in operations:
        command, num = op.split()
        if command == "I":
            heapq.heappush(min_q, int(num))
            heapq.heappush(max_q, -int(num))
        elif command == "D":
            if len(min_q) == 0 or len(max_q) == 0:
                continue
            else:
                if num == "-1":
                    min_item = heapq.heappop(min_q)
                    max_q.remove(-min_item)
                else:
                    max_item = heapq.heappop(max_q)
                    min_q.remove(-max_item)
    if len(min_q) == 0 and len(max_q) == 0:
        return [0, 0]
    else:
        min_val = heapq.heappop(min_q)
        max_val = heapq.heappop(max_q)
    answer = [min_val, -max_val]
    return answer


solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])
