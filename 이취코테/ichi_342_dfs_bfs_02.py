# link: https://www.acmicpc.net/problem/14502


import sys
f = sys.stdin.readline

N, M = map(int, f().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, f().split())))
