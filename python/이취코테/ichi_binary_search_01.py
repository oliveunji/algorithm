from bisect import bisect_left, bisect_right


def solution(N, X, arr):
    idx = bisect_left(arr, X)
    if idx == N:
        return -1
    elif idx == 0 and X != arr[0]:
        return -1
    else:
        cnt = 0
        for i in range(idx, N):
            if arr[i] == X:
                cnt += 1
            else:
                break
        return cnt


N = 7
X = 2
arr = [1, 1, 2, 2, 2, 2, 3]
expected_output = 4

if solution(N, X, arr) == expected_output:
    print('Your answer is right')
else:
    print(
        f'Expected answer: {expected_output}, Your output: {solution(N, X, arr)}')
