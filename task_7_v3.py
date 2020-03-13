import random
import matplotlib.pyplot as plt


def main():
    dots_num = 50
    raw_x = [random.random() for _ in range(dots_num + 2)]

    x, y = [], []
    for i, a in enumerate(raw_x):
        if len(x) < dots_num:
            x.append(a)
            y.append(raw_x[i + 2])

    plt.rcParams["figure.figsize"] = (7, 7)
    for i in range(dots_num):
        plt.scatter(x[i], y[i])

    plt.show()


main()
