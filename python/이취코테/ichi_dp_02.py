# https://techblog-history-younghunjo1.tistory.com/290
import sys
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    t, p = map(int, input())
    arr.append([t, p])


def solution(N, arr):
    arr = []
    for _ in range(N):
        t, p = map(int, input())
        arr.append([t, p])

    results = []
    for idx, t, p in enumerate(arr):
        temp_total = 0
        cur_idx = idx
        while cur_idx < len(arr):
            temp_total += arr[cur_idx]
            cur_idx += t
        results[idx] = temp_total
    return max(results)


solution(N, arr)
