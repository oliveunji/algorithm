import heapq


def solution(n, edge):
    INF = 1e9
    distance = [INF] * (n+1)
    graph = [[] for _ in range(n+1)]

    for i, j in edge:
        graph[i].append((j, 1))
        graph[j].append((i, 1))

    def dijkstra(start):
        q = []
        distance[start] = 0
        heapq.heappush(q, (0, 1))

        while q:
            dist, now = heapq.heappop(q)
            if dist < distance[now]:
                continue

            for item in graph[now]:
                cost = dist + item[1]
                if cost < distance[item[0]]:
                    distance[item[0]] = cost
                    heapq.heappush(q, (cost, item[0]))
    dijkstra(1)
    max_val = max(distance[1:])
    return distance[1:].count(max_val)
