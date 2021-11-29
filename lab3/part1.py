import math

import sympy as sy
from src.support_function import templateDevidChart


if __name__ == '__main__':
    sy.init_printing(use_unicode=True)
    r, a, d, theta = sy.symbols('r'), sy.symbols('a'), sy.symbols('d'), sy.symbols('theta')
    m = templateDevidChart(r, a, d, theta)
    for j in range(sy.shape(m)[0]):
        print(m.row(j))
    m = m.evalf(subs={r: 5, a: 0, d: 3, theta: math.pi / 2})
    for j in range(sy.shape(m)[0]):
        print(m.row(j))
