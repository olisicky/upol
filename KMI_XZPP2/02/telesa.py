from math import pi


def objem_krychle(a):
    return a**3


def povrch_krychle(a):
    return 6 * a**2


def objem_kvadr(a, b, v):
    return a * b * v


def povrch_kvadr(a, b, c):
    return 2 * (a * b + a * c + b * c)


def objem_valec(r, v):
    return pi * r**2 * v


def povrch_valec(r, v):
    return 2 * pi * r * (r + v)


def objem_kuzel(r, v):
    return 1/3 * pi * r**2 * v


def povrch_kuzel(r, v):
    s = (r**2 + v**2)**(1/2)
    return pi * r * (r + s)


def objem_koule(r):
    return 4/3 * pi * r**3


def povrch_koule(r):
    return 4 * pi * r**2


def objem_hranol(sp, v):
    return sp * v


def povrch_hranol(sp, spl):
    return 2 * sp + spl


def objem_jehlan(sp, v):
    return 1/3 * sp * v


def povrch_jehlan(sp, spl):
    return sp + spl
