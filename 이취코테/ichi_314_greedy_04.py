import collections


def cannot_make_amount(N, input):
    # do something
    coin_arr = list(map(int, input.split()))
    coin_counter = collections.Counter(coin_arr)

    while True:
        if not cannot_make_amount(coin_counter):


N = 5
input = '3 2 1 1 9'
excepted_output = 8

if cannot_make_amount(N, input) == excepted_output:
    print("Your answer is right")
else:
    print(
        f'Expected output: {excepted_output}, Your answer: {cannot_make_amount(N, input)}')
