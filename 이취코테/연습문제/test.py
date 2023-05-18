def after_cleaning(cur_time):
    cur_time, cur_min = map(int, cur_time.split(":"))
    cur_min += 10
    if cur_min >= 60:
        cur_time += 1
        cur_min -= 60
    next_time = str(cur_time).rjust(2, "0") + ":" + str(cur_min).rjust(2, "0")
    return next_time


def compare_time(a, b):
    a_time, a_min = map(int, a.split(":"))
    b_time, b_min = map(int, b.split(":"))

    if a_time > b_time:
        return True
    elif a_time == b_time:
        if a_min >= b_min:
            return True
        else:
            return False
    return False


def solution(book_time):
    stack = []
    book_time.sort(key=lambda x: (x[0], x[1]))
    print(book_time)

    for a, b in book_time:
        if not stack:
            stack.append(after_cleaning(b))
        else:
            flag = False
            for i in range(len(stack)):
                if compare_time(a, stack[i]):
                    stack[i] = after_cleaning(b)
                    flag = True
            if not flag:
                stack.append(after_cleaning(b))

    return len(stack)


solution([["15:00", "17:00"], ["16:40", "18:20"], [
         "14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]])

# def solution(maps):
#     answer = 0
#     N = len(maps)
#     M = len(maps[0])

#     # find start
#     def find_start():
#         for i in range(N):
#             for j in range(M):
#                 if maps[i][j] == "S":
#                     return [i, j]

#     str_i, str_j = find_start()
#     dx = [1, 0, -1, 0]
#     dy = [0, 1, 0, -1]

#     results = []

#     def dfs(i, j, count, l_visited):
#         for i in range(4):
#             nx = i + dx[i]
#             ny = j + dy[i]

#             if 0 <= nx < N and 0 <= ny < M:
#                 if maps[nx][ny] == "E" and l_visited == True:
#                     results.append(count)
#                     return
#                 elif maps[nx][ny] == "L":
#                     dfs(i+1, j, count+1, True)
#                     dfs(i, j+1, count+1, True)
#                     dfs(i-1, j, count+1, True)
#                     dfs(i, j-1, count+1, True)
#                 elif maps[nx][ny] == "O" or maps[nx][ny] == "S":
#                     dfs(i+1, j, count+1, l_visited)
#                     dfs(i, j+1, count+1, l_visited)
#                     dfs(i-1, j, count+1, l_visited)
#                     dfs(i, j-1, count+1, l_visited)

#     dfs(str_i, str_j, 0, False)
#     print(results)


# solution(["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"])
