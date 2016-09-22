#!/usr/bin/sage -python

# by lwc
# 2016/09/22

from sage.all import *

def find_p_Coppersmith(n, pLow, lowerBitsNum, beta=0.5):
    x = PolynomialRing(Zmod(n), names='x').gen()
    nbits = n.bit_length()

    f = 2**lowerBitsNum*x + pLow
    f = f.monic()
    roots = f.small_roots(X=2**(nbits//2-lowerBitsNum), beta=beta)
    if roots:
        x0 = roots[0]
        p = gcd(2**lowerBitsNum*x0 + pLow, n)
        return ZZ(p)

def find_p(n, e, dLow, beta=0.5):
    X = var('X')
    lowerBitsNum = dLow.bit_length()

    for k in xrange(1, e+1):
        results = solve_mod([e*dLow*X - k*X*(n-X+1) + k*n == X], 2**lowerBitsNum)
        for x in results:
            pLow = ZZ(x[0])
            p = find_p_Coppersmith(n, pLow, lowerBitsNum)
            if p:
                return p

def partial_key_exposure_attack(n, e, dLow, beta=0.5):
    p = find_p(n, e, dLow, beta)
    assert p is not None and n % p == 0, 'fail'
    q = n / p
    return p, q

n = 123541066875660402939610015253549618669091153006444623444081648798612931426804474097249983622908131771026653322601466480170685973651622700515979315988600405563682920330486664845273165214922371767569956347920192959023447480720231820595590003596802409832935911909527048717061219934819426128006895966231433690709
e = 97

beta = 0.5
dLow = 48553333005218622988737502487331247543207235050962932759743329631099614121360173210513133
p, q = partial_key_exposure_attack(n, e, dLow, beta)
d = inverse_mod(e, (p-1)*(q-1))
print 'p =', p
print 'q =', q
print 'd =', d
