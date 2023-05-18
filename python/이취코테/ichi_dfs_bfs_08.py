def solution(board):

    count = 0
    N = len(board)

    def dfs(x, y, count):
        if x == N-1 and y == N-1:
            return count

        # 오른쪽으로 이동하는 경우
        if y+2 < N:
            if board[x][y+2] != 1:
                count += 1
                dfs(x, y+2, count)

        if x+1 < N and y+1 < N:
            if board[x+1][y+1] != 1:
                count += 1
                dfs(x+1, y+1, count)

    result = dfs(0, 0, count)
    print(result)


solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [
         0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]])
