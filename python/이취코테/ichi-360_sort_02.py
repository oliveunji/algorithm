import sys


def solution(input):
    # processing input
    input_arr = input.split("\n")
    N = input_arr[0]
    location = list(map(int, input_arr[1].split()))
    location.sort()
    # print(location)
    min_val = location[0]
    max_val = location[-1]

    min_dist = sys.maxsize
    min_dist_idx = 0
    for i in range(min_val, max_val+1):
        cur_dist = 0
        for pos in location:
            cur_dist += abs(i-pos)
        if cur_dist < min_dist:
            min_dist = cur_dist
            min_dist_idx = i
        # print(cur_dist, min_dist, min_dist_idx)
    print(min_dist_idx)


input = """4
5 1 7 9"""

expected_output = 5

if solution(input) == expected_output:
    print('Your answer is right')
else:
    print(
        f'Expected answer: {expected_output}, Your output: {solution(input)}')
