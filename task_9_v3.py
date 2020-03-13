import random


def normal(e, d):
    return e + d * (sum([random.random() for _ in range(12)]) - 6)


def main():
    exp_num = 1000

    ans = 0
    for _ in range(exp_num):
        cyl = normal(100, 1)
        kern = normal(99, 1)
        if cyl <= kern:
            ans += 1

    print(ans)


main()
