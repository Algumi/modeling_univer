import random


def experiment_results(p1, p2, p3):
    a, b, c = [random.random() for _ in range(3)]
    if a > p1 or b > p2 or c > p3:
        return False

    return True


def main():
    p1, p2, p3 = 0.9, 0.88, 0.95
    exp_num = 1000
    stats = []

    for _ in range(exp_num):
        stats.append(experiment_results(p1, p2, p3))

    print(sum(stats) / len(stats))


main()
