def solution(N, M, graph):

    def dfs(x, y):
        if x < 0 or x >= N or y < 0 or y >= M:
            return False
        elif graph[x][y] == 0:
            graph[x][y] = 1
            dfs(x-1, y)
            dfs(x, y-1)
            dfs(x+1, y)
            dfs(x, y+1)
            return True

    result = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                if dfs(i, j):
                    result += 1

    print(result)


solution(4, 5, [
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
])


# def solution(N, M, graph):
#     def dfs(x,y):
#         if 0<= x < N and 0<= y < M and graph[x][y] == 0:
#             graph[x][y] = 1
#             dfs(x + 1, y)
#             dfs(x - 1, y)
#             dfs(x, y + 1)
#             dfs(x, y - 1)
#             return True
#         else:
#             return False
#     result = 0
#     for i in range(N):
#         for j in range(M):
#             if dfs(i, j):
#                 result += 1

#     print(result)
#     return result


# def solution(N, M, graph):
#     total = 0

#     def dfs(x, y):
#         if 0 <= x < N and 0 <= y < M and graph[x][y] == 0:
#             graph[x][y] = 1
#             dfs(x-1, y)
#             dfs(x, y-1)
#             dfs(x+1, y)
#             dfs(x, y+1)
#             return True

#         else:
#             return False

#     for i in range(N):
#         for j in range(M):
#             if dfs(i, j):
#                 total += 1
#     print(total)
#     return total


solution(4, 5, [
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
])
