import math
import matplotlib.pyplot as plt


def calculate(ans_x, ans_y):
    a, b = 0.8, 0.3
    t, h = 0, 0.2

    while t < 4:
        ans_x.append(ans_x[-1] + h * a * ans_x[-1] ** 2)
        ans_y.append(ans_y[-1] + h * b * ans_y[-1])
        t += h

    return ans_x, ans_y


def main():
    final_x, final_y = [], []
    x_opt = [-0.8, -0.8, 0.3, 0.3]
    y_opt = [-0.8, 0.8, -0.8, 0.8]

    for x, y in zip(x_opt, y_opt):
        ans_x, ans_y = calculate([x], [y])
        plt.plot(ans_x, ans_y)

    # plt.plot(final_x, final_y)
    plt.ylabel('x')
    plt.xlabel('y')
    plt.show()


main()
