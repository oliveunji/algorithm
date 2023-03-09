import sys
import heapq
input = sys.stdin.readline
N, M = map(int, input().split())

INF = 1e9
distance = [INF] * (N+1)

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

q = []
heapq.heappush(q, (0, 1))
distance[1] = 0

while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for n, d in graph[now]:
        cost = dist + d
        if cost < distance[n]:
            distance[n] = cost
            heapq.heappush(q, (cost, n))

# print(distance[1:])
max_dist = max(distance[1:])
index = distance[1:].index(max_dist)
index += 1
count = distance[1:].count(max_dist)

print(f'{index} {max_dist} {count}')
