def multiply_or_sum(input):
    result = -1
    for num in map(int, list(input)):
        if result == -1:
            result = num
        else:
            if result == 0 or num == 0:
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
