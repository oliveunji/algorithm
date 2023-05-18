def multiply_or_sum(input):
    result = -1
    for num in map(int, list(input)):
        if result == -1:
            result = num
        else:
            if result <= 1 or num <= 0:
                result += num
            else:
                result *= num
    return result


input = '567'
expected_output = 210
if multiply_or_sum(input) == expected_output:
    print('Your answer is right')
else:
    print(
        f'something is wrong. Expected output: {expected_output}, your answer: {multiply_or_sum(input)}')

# 개선점
# 1. 0인 경우만 생각하고, 1인 경우에 대해서는 생각하지 못했다.
