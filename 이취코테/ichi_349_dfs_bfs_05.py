# link: https://www.acmicpc.net/problem/14888

import sys
f = sys.stdin.readline

N = int(f())
data = list(map(int, f().split()))
for _ in range(N):
    plus_cnt, minus_cnt, mul_cnt, div_cnt = map(int, f().split())

# idea1 - 가능한 모든 경우의 연산에 대해 나열 후, eval 통해 min, max 구하기
# 풀이법 - https://data-flower.tistory.com/72 -> DFS를 통해 구함

max_val = -1e9
min_val = 1e9

def dfs(i, arr):
    if i == N:
        max_val = max(max_val, arr)
        min_val = min(min_val, arr)
    else:
        if plus_cnt > 0:
            plus_cnt -= 1
            dfs(i+1, arr + data[i])
            plus_cnt += 1
        if minus_cnt > 0:
            minus_cnt -= 1
            dfs(i+1, arr - data[i])
            minus_cnt += 1
        if mul_cnt > 0:
            mul_cnt -= 1
            dfs(i+1, arr * data[i])
            mul_cnt += 1
        if div_cnt > 0:
            div_cnt -= 1
            dfs(i+1, arr // data[i])
            div_cnt += 1

dfs(1, data[0])

print(max_val)
print(min_val)