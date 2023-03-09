import heapq
import sys
input = sys.stdin.readline
INF = 1e9

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

T = int(input())

for _ in range(T):
    N = int(input())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))

    distance = [[INF]*N for _ in range(N)]

    q = [(graph[0][0], 0, 0)]
    distance[0][0] = graph[0][0]

    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
        print(distance[N-1][N-1])




















# import heapq

# T = int(input())
# INF = 1e9
# move = [(1, 0), (-1, 0), (0, 1), (0, -1)]


# def dijkstra(d, i, j):
#     q = []
#     heapq.heappush(q, (d, i, j))
#     distance[i][j] = d

#     while q:
#         now, a, b = heapq.heappop(q)
#         if distance[a][b] < now:
#             continue

#         for x, y in move:
#             dx = a + x
#             dy = a + y

#             if dx < 0 or dx >= N or dy < 0 or dy >= N:
#                 continue

#             cost = now + graph[dx][dy]
#             if cost < distance[dx][dy]:
#                 distance[dx][dy] = cost
#                 heapq.heappush(q, (cost, dx, dy))


# for _ in range(T):
#     N = int(input())

#     graph = []
#     for _ in range(N):
#         graph.append(list(map(int, input().split())))

#     distance = [[INF] * N for _ in range(N)]
#     dijkstra(graph[0][0], 0, 0)
#     print(distance[N-1][N-1])
