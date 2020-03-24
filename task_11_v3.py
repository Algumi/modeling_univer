# Task 3 Part 2.4

import random
import math
import matplotlib.pyplot as plt


def poisson(lam):
    return -1 / lam * math.log(random.random())


def main():
    exp_num = 1000
    first_flow = []
    second_flow = []
    last = 0

    for _ in range(exp_num):
        val = poisson(1)
        if random.random() > 0.25:
            first_flow.append(val + last)
        else:
            second_flow.append(val + last)
        last = val

    for data in [first_flow, second_flow]:
        a, b = min(data), max(data)

        length = (b - a) / 19
        ans = [0] * 20
        for elem in data:
            ans[int(elem // length)] += 1
        ans = [a / len(data) for a in ans]

        plt.subplots(figsize=(7, 4))
        plt.bar([a * length for a in range(20)], ans, width=0.2, align='center')  # A bar chart
        plt.xlabel('i')
        plt.ylabel('p')

    plt.show()


main()
