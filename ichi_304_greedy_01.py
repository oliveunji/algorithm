def adventurers(N, input):
    result = 0
    previous_item = 0
    input.sort()
    for num in input:
        if num == previous_item:
            continue
        else:
            if input.count(num) >= num:
                result += 1
            previous_item = num
    return result


N = 5
input = [2, 3, 1, 2, 2]
expected_output = 2

if adventurers(N, input) == expected_output:
    print("you are right")
else:
    print(
        f"something is wrong. expected output: {expected_output}, your output: {adventurers(N, input)}")
