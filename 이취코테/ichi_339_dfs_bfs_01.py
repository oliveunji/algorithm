# problem link: https://www.acmicpc.net/problem/18352
# solution link: https://wonyoung2257.tistory.com/71
# submission: https://www.acmicpc.net/status?user_id=angie4u&problem_id=18352&from_mine=1

import sys
from collections import deque
input = sys.stdin.readline
INF = 1e9

N, M, K, X = map(int, input().split())
graph = [[]*(N+1)]
distance = [INF]*(N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, 1))


def bfs(x):
    queue = deque()
    queue.append(x)
    distance[x] = 0
    while queue:
        x = queue.popleft()
        for node, dist in graph[x]:
            if distance[node] > dist + distance[x]:
                distance[node] = dist + distance[x]
                queue.append(node)


bfs(1)
for i in range(1, N+1):
    if distance[i] == K:
        print(i)


# import sys
# from collections import deque

# input = sys.stdin.readline

# # N 도시 수, M 도로 수, K 거리 정보 X 출발 도시
# N, M, K, X = map(int, input().split(' '))
# graph = [[] for _ in range(N+1)]

# for _ in range(M):
#   a, b =  map(int, input().split(' '))
#   graph[a].append(b)

# distance = [-1] *(N+1)
# distance[X] = 0

# # BFS 부분
# q = deque([X])
# while q:
#   now = q.popleft()

#   for next in graph[now]:
#     if distance[next] == -1:
#       distance[next] = distance[now]+1
#       q.append(next)

# # K값이 distance에 있다면 i값출력 없다면 -1 출력
# if K in distance:
#   for i in range(1, N+1):
#     if distance[i] == K:
#       print(i)
#       check = True
# else:
#   print(-1)
