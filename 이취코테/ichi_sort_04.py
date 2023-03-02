import heapq
N = int(input())
q = []

for _ in range(N):
    heapq.heappush(q, int(input()))

result = 0

while len(q) != 1:
    num1 = heapq.heappop(q)
    num2 = heapq.heappop(q)
    sum_val = num1 + num2
    result += sum_val
    heapq.heappush(q, sum_val)
print(result)
