def solution(number, k):
    num_arr = list(map(int, list(number)))
    result_arr = []

    start_idx = 0
    last_idx = k

    while k != 0:
        target_range = num_arr[start_idx:last_idx + 1]
        cur_max = max(target_range)
        cur_max_idx = target_range.index(cur_max)
        result_arr.append(cur_max)

        k -= 1
        start_idx = start_idx + cur_max_idx + 1
        last_idx += 1

    result_arr += num_arr[last_idx:]
    result = ''.join(map(str, result_arr))
    return result


input = "4177252841"
k = 4
expected_output = "775841"
if solution(input, k) == expected_output:
    print("Your answer is right")
else:
    print(
        f"Expected output: {expected_output}, your answer: {solution(input, k)}")
