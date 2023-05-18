from collections import deque


def solution(N, M, graph):

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        while queue:
            x, y = queue.popleft()
            # print(x, y)
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))

        return graph[N-1][M-1]

    result = bfs(0, 0)
    print(result)


solution(5, 6, [
    [1, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]
])


# from collections import deque

# n, m = map(int, input().split())

# graph = []
# for i in range(n):
#     graph.append(list(map(int, input().split())))


# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]


# def bfs(x, y):
#     queue = deque((x, y))
#     while queue:
#         x, y = queue.popleft()

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue
#             if graph[nx][ny] == 0:
#                 continue
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = graph[x][y] + 1
#                 queue.append((nx, ny))
#     return graph[n-1][m-1]


# print(bfs(0, 0))
