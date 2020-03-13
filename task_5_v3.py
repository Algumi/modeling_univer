import random


def experiment_results(a, b, n):
    ans = [0] * (b - a + 1)
    period = 0

    for _ in range(n):
        ans[random.randint(0, 1)] += 1
        if ans[a] > ans[b]:
            period += 1
    print(ans)
    return period


def main():
    a, b, n = 0, 1, 1000
    exp_num = 10
    stats = []

    for _ in range(exp_num):
        stats.append(experiment_results(a, b, n))

    for i, x in enumerate(stats):
        print(f"Exp №{i + 1} -- {x / n}")

    print(f"Final - {sum(stats) / n * exp_num}")


main()
