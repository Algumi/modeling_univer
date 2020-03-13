import random


def normal(e, d):
    return e + d * (sum([random.random() for _ in range(12)]) - 6)


def main():
    exp_num = 1000

    ans = 0
    for _ in range(exp_num):
        fact = normal(10, 0.03)
        mes = normal(fact, 0.02)
        if 10.03 >= mes >= 0.97:
            ans += 1

    print(ans / exp_num)


main()
