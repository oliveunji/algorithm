import sys
input = sys.stdin.readline

num = input().strip()
i = len(num)//2
first_part_sum = sum(map(int, list(num[:i])))
second_part_sum = sum(map(int, list(num[i:])))

if first_part_sum == second_part_sum:
    print("LUCKY")
else:
    print("READY")
