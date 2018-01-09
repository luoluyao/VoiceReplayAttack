import sys
import numpy as np
from math import sqrt
from sympy import *
# triangle's three edges : 58, d , d
d = np.sqrt(58 * 58/2)


def cal_position(r12, r13, r14):
    '''
    calculate the position using tdoa
    :param r12:
    :param r13:
    :param r14:
    :return: x, y, z, R
    '''
    r1 = Symbol('r1')
    r2 = Symbol('r2')
    r3 = Symbol('r3')
    r4 = Symbol('r4')

    result_r =  solve([2*(r12 + r14 - r13)*r1 - (r13**2 - r12**2 - r14**2),
             r1 + r12 - r2,
             r1 + r13 - r3,
             r1 + r14 - r4
            ],
            [r1,r2,r3,r4])

    r1 = result_r[r1]
    r2 = result_r[r2]
    r3 = result_r[r3]
    r4 = result_r[r4]

    x = (r3*r3 - r1*r1) / (4 * d)
    y = (r4*r4 - r2*r2) / (4 * d)

    z = Symbol('z')
    z_solve = solve([(x - d)**2 + y**2 + z**2 - r1**2],[z])
    z = z_solve[1][0] # positive number

    R = sqrt(x*x + y*y + z*z)
    return x, y, z, R

def main():
    r12 = 35.86  # 21
    r13 = 73.05  # 20
    r14 = 41.17  # 23
    result = cal_position(r12, r13, r14)
    print result

if __name__ == "__main__":
    main()


# r12 = 17.27 #21
# r13 = 38.52 #20
# r14 = 15.94 #23

# r12 = -35.86 #21
# r13 = -71.72 #20
# r14 = -37.19 #23

# r12 = 17.27 #21
# r13 = 38.52 #20
# r14 = 15.94 #23
#
# x = Symbol('x')
# y = Symbol('y')
# z = Symbol('z')
# R = Symbol('R')
# r1 = Symbol('r1')
# r2 = Symbol('r2')
# r3 = Symbol('r3')
# r4 = Symbol('r4')
#
#
# print solve([x**2 + y**2 + z**2 - R**2,
#              (x - d)**2 + y**2 + z**2 - r1**2,
#              x**2 + (y - d)**2 + z**2- r2**2,
#              (x + d)**2 + y**2 + z**2 - r3**2,
#              x**2 +(y + d)**2 + z**2 - r4**2,
#              r2 - r1 - r12,
#              r3 - r1 - r13,
#              r4 - r1 - r14],
#             [x, y, z, R, r1, r2, r3, r4])


# 
# 
# # triangle's three edges : 58, d , d
# d = np.sqrt(58/2)
# 
# # velocity for sound:mm/s
# v = 340000
# 
# # three tdoa:
# # ATTENTION: signal
# 
# #  calc values.
# 
# r12 = -17.27 #21
# r13 = -38.52 #20
# r14 = -15.94 #23
# 
# 
# r = (np.power(r12,2) + np.power(r14,2) - np.power(r13,2)) / (2 * (r13 - r12 - r14))
# 
# angle1 = np.arctan((r14 - r12) / r13)
# 
# angle2 = np.arcsin(np.sqrt(np.power(r13, 2) + np.power(r14 - r12, 2))  / (2 * d))
# 
# print "r:", r," angle1:", angle1, " angle2:", angle2


# ['sound/log/test2.wav', 'sound/log/test3.wav', -15.94, -10.63, -15.94, -18.59]
# ['sound/log/test2.wav', 'sound/log/test0.wav', -38.52, -42.5, -38.52, -41.17]
# ['sound/log/test2.wav', 'sound/log/test1.wav', -17.27, -7.97, -17.27, -18.59]


# ['sound/log/test2.wav', 'sound/log/test0.wav', -75.7, -87.66, -57.11, -73.05]
# ['sound/log/test2.wav', 'sound/log/test1.wav', -38.52, -41.17, -38.52, -35.86]
# ['sound/log/test2.wav', 'sound/log/test3.wav', -39.84, -46.48, -42.5, -41.17]

# ['sound/log/test2.wav', 'sound/log/test3.wav', -37.19, -49.14, -37.19, -34.53]
# ['sound/log/test2.wav', 'sound/log/test0.wav', -71.72, -85.0, -85.0, -73.05]
# ['sound/log/test2.wav', 'sound/log/test1.wav', -35.86, -42.5, -26.56, -35.86]