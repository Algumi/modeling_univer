import random


def main():
    exp_num = 1000
    L = 100

    ans = 0
    for _ in range(exp_num):
        a, b, c = [random.randint(1, L) for _ in range(3)]
        if a + b > c and a + c > b and b + c > a:
            ans += 1

    print(ans / exp_num)


main()
