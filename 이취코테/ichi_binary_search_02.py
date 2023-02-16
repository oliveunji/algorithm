def solution(N, arr):

    def binary_search(start_idx, end_idx):
        if start_idx > end_idx:
            return -1
        mid = (start_idx + end_idx) // 2
        if arr[mid] == mid:
            return mid
        elif arr[mid] < mid:
            return binary_search(mid+1, end_idx)
        else:
            return binary_search(start_idx, mid-1)
    result = binary_search(0, N-1)
    return result


# N = 5
# arr = [-15, -6, 1, 3, 7]
# expected_output = 3

# N = 7
# arr = [-15, -4, 2, 8, 9, 13, 15]
# expected_output = 2

N = 7
arr = [-15, -4, 3, 8, 9, 13, 15]
expected_output = -1

if solution(N, arr) == expected_output:
    print('Your answer is right')
else:
    print(
        f'Expected answer: {expected_output}, Your output: {solution(N, arr)}')
