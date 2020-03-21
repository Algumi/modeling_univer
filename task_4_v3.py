import matplotlib.pyplot as plt


def calculate(x, y, a, b):
    k1, k2, k3 = 1.1, 1.3, 1.5
    t, h = 0, 0.2
    a = [a]
    b = [b]
    ans_x, ans_y = [x], [y]

    while t < 10:
        a.append(a[-1] + h * ((-k1 - k2) * ans_x[-1] + k2 * ans_y[-1]))
        b.append(b[-1] + h * ((-k2 - k3) * ans_y[-1] + k2 * ans_x[-1]))
        ans_x.append(ans_x[-1] + h * a[-1])
        ans_y.append(ans_y[-1] + h * b[-1])
        t += h

    return ans_x, ans_y


def main():
    x_opt = [-1.8, -1.8, 1.8, 1.8]
    y_opt = [-1.8, 1.8, -1.8, 1.8]
    a = [-3.8, -3.8, 3.8, 3.8]
    b = [-0.8, 0.8, -0.8, 0.8]

    for x, y, a, b in zip(x_opt, y_opt, a, b):
        ans_x, ans_y = calculate(x, y, a, b)
        plt.plot(ans_x, ans_y)

    plt.ylabel('x')
    plt.xlabel('y')
    plt.show()


main()
