# problem link: https://www.acmicpc.net/problem/18352
# solution link: https://steadily-worked.tistory.com/646

from collections import deque
import sys
f = sys.stdin.readline

n, m, k, x = map(int, f().split())
graph = [[] for _ in range(n+1)]
distance = [0] * (n+1)
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, f().split())
    graph[a].append(b)


def bfs(start):
    answer = []
    q = deque([start])
    visited[start] = True
    distance[start] = 0

    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                distance[i] = distance[now] + 1
                if distance[i] == k:
                    answer.append(i)
    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i, end='\n')


bfs(x)

# def dfs(graph, v, visited):
#     visited[v] = True
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)


# def distance_count(input):
#     input_arr = input.split("\n")
#     values = list(map(int, input_arr[0].split()))
#     N = values[0]
#     K = values[2]
#     X = values[3]  # start node

#     distance_arr = []
#     for item in input_arr[1:]:
#         distance_arr.append(list(map(int, item.split())))
#     # print(distance_arr, K, X)

#     visited = [False] * (N+1)
#     graph = [[] for _ in range(N+1)]
#     for a, b in distance_arr:
#         graph[a].append(b)
#     # print(graph)
#     dfs(graph, visited, X)


# input = """4 4 2 1
# 1 2
# 1 3
# 2 3
# 2 4"""

# expected_output = 4
# distance_count(input)
