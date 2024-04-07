from decimal import Decimal

import numpy as np

luminance_grey_18 = Decimal((33/58) ** 3)

lightness_grey_18 = 50

def f(t):
    threshold = Decimal((6 / 29) ** 3)
    if t > threshold:
        return t ** Decimal(1/3)
    else:
        return Decimal(1/3) * (Decimal(29/6) ** 2) * t + Decimal(4/29)

def inverse_f(t):
    delta = Decimal(6/29)
    if t > delta:
        return t ** 3
    else:
        return 3 * delta ** 2 * (t - Decimal(4/29))

def Lstar(Y_div_Yn): 
    return 116 * Y_div_Yn - 16

def Y(Lstar):
    return inverse_f((Lstar + 16) / 116)

for t in np.linspace(0, lightness_grey_18, 51):
    t = Decimal(str(t))
    Y_value = Y(t)
    Lstar_value = Lstar(f(Y_value))
    print(f"L*={int(t)} Y={Y_value:.6f} <---> L*={int(Lstar_value)}")

for t in np.linspace(lightness_grey_18, 100, 51):
    t = Decimal(str(t))
    Y_value = Y(t)
    Lstar_value = Lstar(f(Y_value))
    print(f"L*={int(t)} Y={Y_value:.6f} <---> L*={int(Lstar_value)}")
