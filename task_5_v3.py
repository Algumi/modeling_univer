# task 3 Part 2.1 - REWORKED
import random


def experiment_results(n):
    ans = [0, 0]
    periods = []
    cur_period = 0

    for _ in range(n):
        ans[random.randint(0, 1)] += 1

        if ans[0] > ans[1]:
            cur_period += 1
        else:
            if cur_period != 0:
                periods.append(cur_period)
                cur_period = 0
    print(periods)
    return sum(periods) / max(len(periods), 1)


def main():
    n = 1000
    exp_num = 10
    stats = []

    for _ in range(exp_num):
        stats.append(experiment_results(n))

    for i, x in enumerate(stats):
        print(f"Exp №{i + 1} -- {x}")

    print(f"Final - {sum(stats) / exp_num}")


main()
