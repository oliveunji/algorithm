def solution(n, results):
    # 순위 정보를 가지고 테이블 만듬
    INF = int(1e9)
    graph = [[INF]*(n+1) for _ in range(n+1)]

    # 자기 경기 결과는 0으로 초기화
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                graph[i][j] = 0

    # 경기결과를 보고 아는 경기는 값 할당
    for i, j in results:
        graph[i][j] = 1

    # 플로이드 알고리즘 이용하여 나머지 값 계산
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

    # graph 돌면서 결과 계산
    result = 0
    for i in range(1, n+1):
        count = 0
        for j in range(1, n+1):
            if graph[i][j] != INF or graph[j][i] != INF:
                count += 1
        if count == n:
            result += 1
    return result
