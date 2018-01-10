import sys
import numpy as np
from math import sqrt
from math import isnan
from sympy import *

# triangle's three edges : 58, d , d
d = np.sqrt(58 * 58/2)

# data number for phoneme
phoneme_num = 4

def cal_position_multi(datas):
    '''
    Using cal_position to calculate all datas
    :param datas:
    :return:
    '''
    positions = []
    tmp = []
    for data in datas:
        for d in data:
            r = cal_position(d[1], d[0], d[2])
            if r is not None and len(r) != 0:
                tmp.append(r)
        positions.append(tmp)
        tmp = []
    return positions

def isComplex(num):
    '''
    is complex?
    :return:
    '''
    try:
        float(num)
        return False
    except:
        return True

def calc_z(x, y, r1):
    '''
    calcaute the value of z
    :param x:
    :param y:
    :param r1:
    :param r2:
    :param r3:
    :param r4:
    :return: 0 means wrong!
    '''
    z = Symbol('z')
    z_solve = solve([(x - d) ** 2 + y ** 2 + z ** 2 - r1 ** 2], [z])
    z_value = z_solve[1][0]  # positive number
    if not isComplex(z_value):
      return z_value
    return 0




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
    if r14 == 0:
        print "[error]:wrong input:",r12,r13,r14
        return
    #print r12,r13,r14
    result_r =  solve([2*(r12 + r14 - r13)*r1 - (r13**2 - r12**2 - r14**2),
             r1 + r12 - r2,
             r1 + r13 - r3,
             r1 + r14 - r4],
            [r1,r2,r3,r4])
    if len(result_r) == 0:
        print "[error]:solve failed"
        return
    r1 = result_r[r1]
    r2 = result_r[r2]
    r3 = result_r[r3]
    r4 = result_r[r4]

    x = (r3*r3 - r1*r1) / (4 * d)
    y = (r4*r4 - r2*r2) / (4 * d)

    z = calc_z(x,y,r1)
    if z == 0:
        print "[error] complex:"
        return

    R = sqrt(x*x + y*y + z*z)

    return round(x,2), round(y,2), round(z,2), round(R,2)

def main():
    file_name = sys.argv[1]
    file_name_write = sys.argv[2]
    data = read_file(file_name)
    datas = transform_data(data)
    position = cal_position_multi(datas)
    f_wite = open(file_name_write, "w")
    for p in position:
        f_wite.write(str(p))
        f_wite.write("\n")
    f_wite.close()
    print data
    print datas
    print position

def transform_data(datas):
    '''
    change data to formated data
    :param data:
    :return:
    '''
    result = []
    tmp = []
    for data in datas:
        for i in range(phoneme_num):
            tmp.append([d for d in data[i::phoneme_num]])
        result.append(tmp)
        tmp = []
    return result

def cmd_func(a, b):
    '''
    compare .wav name
    :param a:
    :param b:
    :return:
    '''
    return cmp(a, b)

def read_file(file_name):
    '''
    read file datas
    :param file_name:
    :return:
    '''
    file = open(file_name)
    test_data = file.readlines()
    line_count = 1
    datas = []
    tmp = []
    merge_tmp = []
    for t_data in test_data:
        t_data = t_data.strip()
        tmp.append(t_data)
        if (line_count % 3 == 0):
            tmp.sort(cmp=cmd_func)
            tmp = str(tmp).strip()
            tmp = tmp.replace('[', '')
            tmp = tmp.replace(']', '')
            tmp = tmp.replace('"', '')
            tmp_new = tmp.split(", ")
            for i in range(len(tmp_new)):
                if i % (phoneme_num + 2) == 0 or i % (phoneme_num + 2) == 1:
                    continue
                merge_tmp.append(abs(float(tmp_new[i])))
            tmp = []
            datas.append(merge_tmp)
            merge_tmp = []
        line_count += 1
    file.close()
    return datas

if __name__ == "__main__":
    main()


# ['sound/log/test2.wav', 'sound/log/test3.wav', -15.94, -10.63, -15.94, -18.59]
# ['sound/log/test2.wav', 'sound/log/test0.wav', -38.52, -42.5, -38.52, -41.17]
# ['sound/log/test2.wav', 'sound/log/test1.wav', -17.27, -7.97, -17.27, -18.59]

# ['sound/log/test2.wav', 'sound/log/test0.wav', -75.7, -87.66, -57.11, -73.05]
# ['sound/log/test2.wav', 'sound/log/test1.wav', -38.52, -41.17, -38.52, -35.86]
# ['sound/log/test2.wav', 'sound/log/test3.wav', -39.84, -46.48, -42.5, -41.17]

# ['sound/log/test2.wav', 'sound/log/test3.wav', -37.19, -49.14, -37.19, -34.53]
# ['sound/log/test2.wav', 'sound/log/test0.wav', -71.72, -85.0, -85.0, -73.05]
# ['sound/log/test2.wav', 'sound/log/test1.wav', -35.86, -42.5, -26.56, -35.86]