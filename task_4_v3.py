import matplotlib.pyplot as plt


def calculate(ans_x, ans_y):
    k1, k2, k3 = 1.1, 1.3, 1.5
    t, h = 0, 0.2

    while t < 4:
        ans_x.append(ans_x[-1] + h * ((-k1 - k2) * ans_x[-1] + k2 * ans_y[-1]))
        ans_y.append(ans_y[-1] + h * ((-k2 - k3) * ans_y[-1] + k2 * ans_x[-1]))
        t += h

    return ans_x, ans_y


def main():
    x_opt = [-1.8, -1.8, 1.8, 1.8]
    y_opt = [-1.8, 1.8, -1.8, 1.8]

    for x, y in zip(x_opt, y_opt):
        ans_x, ans_y = calculate([x], [y])
        plt.plot(ans_x, ans_y)

    plt.ylabel('x')
    plt.xlabel('y')
    plt.show()


main()
