# my var - 3
# next task = current + 11
# current task = 3
import math
import matplotlib.pyplot as plt


def main():
    k, g, = 0.6, 9.8
    cyl_s, hole_s = math.pi * 4, math.pi * 0.01
    h = 0.1
    x = 6
    t = 0

    ans_x, ans_t = [6], [0]

    while x > 0.1:
        x = x + h * -k * hole_s * math.sqrt(2 * g * x) / cyl_s
        t += h
        ans_x.append(x)
        ans_t.append(t)

    print(x, t)
    plt.plot(ans_t, ans_x)
    plt.ylabel('Water level (m)')
    plt.xlabel('Time (s)')
    plt.show()


main()
