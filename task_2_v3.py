import math
import matplotlib.pyplot as plt


def main():
    r = 0.5
    R = 4
    p = 0.1
    k = 0.4

    h = 0.01
    ans_r, ans_p = [], []

    while p < 10:
        r = r + h * k * (R - r)
        p += h

        ans_r.append(r)
        ans_p.append(p)

    print(r, p)
    plt.plot(ans_r, ans_p)
    plt.ylabel('r')
    plt.xlabel('p')
    plt.show()


main()
