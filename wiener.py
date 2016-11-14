# by lwc
# 2016/11/14

from sage.all import *

def wiener(n, e):
    """Wiener's attack"""
    n = Integer(n)
    e = Integer(e)
    cf = (e / n).continued_fraction().convergents()
    for f in (e / n).continued_fraction().convergents()[1:]:
        k, d = f.numerator(), f.denominator()
        phi = ((e * d) - 1) / k
        b = -(n - phi + 1)
        dis_sqrt = sqrt(b * b - 4 * n)
        if dis_sqrt.is_integer():
            p = (-b + dis_sqrt) / 2
            q = (-b - dis_sqrt) / 2
            if p < q:
                p, q = q, p
            return (p, q, d)

