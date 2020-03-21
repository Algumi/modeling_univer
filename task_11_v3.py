import random
import math


def poisson(lam):
    return -1 / lam * math.log(random.random())


def main():
    exp_num = 1000

    ans = 0
    for _ in range(exp_num):
        pass

    print(ans / exp_num)


main()