def reverse_string(input):
    previous_item = None
    cnt_zero = 0
    cnt_one = 0
    for item in list(input):
        if not previous_item:
            previous_item = item
        else:
            if previous_item == item:
                continue
            else:
                previous_item = item
                if item == '0':
                    cnt_zero += 1
                else:
                    cnt_one += 1
    if cnt_zero > cnt_one:
        return cnt_one
    else:
        return cnt_zero


input = '0001100'
expected_output = 1

if reverse_string(input) == expected_output:
    print('Your answer is right')
else:
    print(
        f'Expected answer: {expected_output}, Your output: {reverse_string(input)}')
