def zip(s, size):
    prev = []
    zip_s = ""

    for idx in range(0, len(s)+1, size):
        cur = s[idx:idx+size]
        if not prev:
            prev.append(cur)
        else:
            if prev[-1] == cur:
                prev.append(cur)
            else:
                if len(prev) == 1:
                    zip_s += prev[-1]
                else:
                    zip_s += str(len(prev)) + prev[-1]
                prev = []
                prev.append(cur)
    if len(prev) != 0:
        zip_s += prev.pop()
    return len(zip_s)


def solution(s):
    results = []
    if len(s) == 1:
        return 1
    for i in range(1, len(s)):
        results.append(zip(s, i))
    return min(results)


input = "aabbaccc"
expected_output = 7

if solution(input) == expected_output:
    print('Your answer is right')
else:
    print(
        f'Expected answer: {expected_output}, Your output: {solution(input)}')
