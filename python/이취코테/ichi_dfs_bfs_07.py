from collections import deque

N, L, R = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

result = 0


def process(x, y, index):
    united = []
    united.append((x, y))

    q = deque()
    q.append((x, y))

    union[x][y] = index
    summary = graph[x][y]
    count = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and union[nx][ny] == -1:
                if L <= abs(graph[nx][ny] - graph[x][y]) <= R:
                    q.append((nx, ny))
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx, ny))
    for i, j in united:
        graph[i][j] = summary // count
    # return count


total_count = 0
while True:
    union = [[-1]*N for _ in range(N)]
    index = 0
    for i in range(N):
        for j in range(N):
            if union[i][j] == -1:
                process(i, j, index)
                index += 1
    if index == N*N:
        break
    total_count += 1
print(total_count)

# 2 20 50
# 50 30
# 20 40
