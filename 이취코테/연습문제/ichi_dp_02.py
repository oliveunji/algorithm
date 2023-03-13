def solution(N, M, arr):
    max_val = 0
    for i in range(N):
        max_val = max(max_val, min(arr[i]))
    print(max_val)
    return max_val


# solution(3, 3, [[3, 1, 2], [4, 1, 4], [2, 2, 2]])
solution(2, 4, [[7, 3, 1, 8], [3, 3, 3, 4]])
