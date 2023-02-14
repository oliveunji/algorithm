def solution(input):
    sum = 0
    alphabet_arr = []
    for char in input:
        if char.isnumeric():
            sum += int(char)
        else:
            alphabet_arr.append(char)
    alphabet_arr.sort()
    result = "".join(alphabet_arr) + str(sum)
    return result


input = "K1KA5CB7"
expected_output = "ABCKK13"

if solution(input) == expected_output:
    print('Your answer is right')
else:
    print(
        f'Expected answer: {expected_output}, Your output: {solution(input)}')
