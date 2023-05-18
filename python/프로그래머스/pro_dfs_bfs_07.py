# https://bladejun.tistory.com/164
import copy


def dfs(graph, x, y, position, n, num):
    dic = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]}
    ret = [position]

    for i in range(4):
        nx = x + dic[i][0]
        ny = y + dic[i][1]

        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == num:
            graph[nx][ny] = 2
            ret = ret + \
                dfs(graph, nx, ny, [position[0] + dic[i]
                    [0], position[1] + dic[i][1]], n, num)
    return ret


def rotate(lst):
    n = len(lst)
    ret = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ret[j][n-1-i] = lst[i][j]
    return ret


def solution(game_board, table):
    answer = 0
    game_board_copy = copy.deepcopy(game_board)

    N = len(game_board)
    block = []

    for i in range(N):
        for j in range(N):
            if game_board_copy[i][j] == 0:
                game_board_copy[i][j] = 2
                # 블록의 위치를 파악하여 result에 저장
                result = dfs(game_board_copy, i, j, [0, 0], N, 0)[1:]
                block.append(result)

    for r in range(4):
        table = rotate(table)
        # table을 rotate 시켜서 저장
        table_rotate_copy = copy.deepcopy(table)
        # rotate 한 table 마다 block과 일치하는 경우가 있는지 확인

        for i in range(N):
            for j in range(N):
                if table_rotate_copy[i][j] == 1:
                    table_rotate_copy[i][j] = 2
                    result = dfs(table_rotate_copy, i, j, [0, 0], N, 1)[1:]
                    if result in block:
                        block.pop(block.index(result))
                        answer += (len(result) + 1)
                        table = copy.deepcopy(table_rotate_copy)
                    else:
                        table_rotate_copy = copy.deepcopy(table)
    return answer


GAME_BOARD = [[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [
    1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 0]]
TABLE = [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1],
         [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0], [0, 1, 0, 0, 0, 0]]
solution(GAME_BOARD, TABLE)
