import random


def experiment_results(a, b, n):
    ans = [0] * (b - a + 1)
    periods = []
    cur_period = 0

    for _ in range(n):
        ans[random.randint(0, 1)] += 1

        if ans[a] > ans[b]:
            cur_period += 1
        else:
            if cur_period != 0:
                periods.append(cur_period)
                cur_period = 0
    print(periods)
    return sum(periods) / max(len(periods), 1)


def main():
    a, b, n = 0, 1, 1000
    exp_num = 10
    stats = []

    for _ in range(exp_num):
        stats.append(experiment_results(a, b, n))

    for i, x in enumerate(stats):
        print(f"Exp №{i + 1} -- {x}")

    print(f"Final - {sum(stats) / exp_num}")


main()
