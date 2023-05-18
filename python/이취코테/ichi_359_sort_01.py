from functools import cmp_to_key


def compare(std1, std2):
    if std1[1] == std2[1] and std1[2] == std2[2] and std1[3] == std2[3]:
        if std1[0].lower() < std2[0].lower():
            return -1
        else:
            return 1
    elif std1[1] == std2[1] and std1[2] == std2[2]:
        if std1[3] < std2[3]:
            return 1
        else:
            return -1
    elif std1[1] == std2[1]:
        if std1[2] < std2[2]:
            return -1
        else:
            return 1
    else:
        if std1[1] < std2[1]:
            return 1
        else:
            return -1


def sort_students(input_str):
    input_arr = []
    input_str_arr = input_str.split("\n")
    for str_input in input_str_arr[1:]:
        input_arr.append(str_input.split())

    input_arr.sort(key=cmp_to_key(compare))
    # print(input_arr)
    for item in input_arr:
        print(item[0])


input = """12
Junkyu 50 60 100
Sangkeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90"""

expected_output = """Donghyuk
Sangkeun
Sunyoung
nsj
Wonseob
Sanghyun
Sei
Kangsoo
Haebin
Junkyu
Soong
Taewhan"""

sort_students(input)
# if sort_students(input) == expected_output:
#     print('Your answer is right')
# else:
#     print(
#         f'Expected answer: {expected_output}, Your output: {sort_students(input)}')
