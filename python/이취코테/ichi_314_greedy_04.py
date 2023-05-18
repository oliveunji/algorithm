def cannot_make_amount(N, input):
    coin_arr = list(map(int, input.split()))
    coin_arr.sort()
    target = 1
    for coin in coin_arr:
        if target < coin:
            break
        target += coin
    return target


N = 5
input = '3 2 1 1 9'
excepted_output = 8

if cannot_make_amount(N, input) == excepted_output:
    print("Your answer is right")
else:
    print(
        f'Expected output: {excepted_output}, Your answer: {cannot_make_amount(N, input)}')

# 개선점
# 다음 만들어야 하는 동전(target)을 동적으로 더해나가면서 구해야 한다.
