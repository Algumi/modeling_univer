# Task 14 Part 2.4

import random
import math


def poisson(lam):
    return -1 / lam * math.log(random.random())


def main():
    exp_num = 1000
    lam = 0.1
    duration = []

    for _ in range(exp_num):
        p1, p2 = poisson(lam), poisson(lam)
        duration.append(max(p1, p2))

    m_e = sum(duration) / exp_num
    dev = math.sqrt(sum([(x - m_e) ** 2 for x in duration]) / (exp_num - 1))

    print(f"Mathematical expectation: {m_e}")
    print(f"Average square deviation: {dev}")


main()
