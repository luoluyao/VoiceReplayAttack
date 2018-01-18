import sys
import sympy as sp


# high is 19cm
high = 190
length_side = 58
length_bevel = 82

# o
o_length = 60
# i
i_length = 30
# cos135
cos_135 = -0.707



# data number for one set
one_set_sample = 12

# data number for phoneme
phoneme_num = 4

# compare .wav name
def cmd_func(a, b):
    return cmp(a, b)

# read file datas
def read_file(file_name):
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

# is legal?
def legal_value(value):
    if len(value) != 0:
        return round(float(value[0]), 2)
    else:
        return 0

# example for tolley : t, o, l, i
def cal_dis_x(datas):
    x = sp.Symbol('x', real=True)
    values_all = []
    for data in datas:
        values = []
        # 1
        tdoa = data[0]
        a = sp.solve((sp.sqrt(high ** 2 + x ** 2) + tdoa) ** 2 - (length_bevel + x) ** 2 - high ** 2, x)
        values.append(legal_value(a))

        # 2
        tdoa = data[1]
        a = sp.solve((sp.sqrt(high ** 2 + (x+o_length) ** 2) + tdoa) ** 2 - (length_bevel + (x+o_length)) ** 2 - high ** 2, x)
        values.append(legal_value(a))

        # 3
        tdoa = data[2]
        a = sp.solve((sp.sqrt(high ** 2 + x ** 2) + tdoa) ** 2 - (length_bevel + x) ** 2 - high ** 2, x)
        values.append(legal_value(a))

        # 4
        tdoa = data[3]
        a = sp.solve((sp.sqrt(high ** 2 + (x + i_length) ** 2) + tdoa) ** 2 - (length_bevel + (x + i_length)) ** 2 - high ** 2, x)
        values.append(legal_value(a))

        # 5
        tdoa = data[4]
        a = sp.solve((sp.sqrt(high ** 2 + x ** 2) + tdoa) ** 2 - (x ** 2 + length_side ** 2 - 2 * cos_135 * x * length_side) - high ** 2, x)
        values.append(legal_value(a))

        # 6
        tdoa = data[5]
        a = sp.solve((sp.sqrt(high ** 2 + (x+o_length) ** 2) + tdoa) ** 2 - ((x+o_length) ** 2 + length_side ** 2 - 2 * cos_135 * (x+o_length) * length_side) - high ** 2, x)
        values.append(legal_value(a))

        # 7
        tdoa = data[6]
        a = sp.solve((sp.sqrt(high ** 2 + x ** 2) + tdoa) ** 2 - (x ** 2 + length_side ** 2 - 2 * cos_135 * x * length_side) - high ** 2, x)
        values.append(legal_value(a))

        # 8
        tdoa = data[7]
        a = sp.solve((sp.sqrt(high ** 2 + (x + i_length) ** 2) + tdoa) ** 2 - ((x + i_length) ** 2 + length_side ** 2 - 2 * cos_135 * (x + i_length) * length_side) - high ** 2, x)
        values.append(legal_value(a))

        # 9
        tdoa = data[8]
        a = sp.solve((sp.sqrt(high ** 2 + x ** 2) + tdoa) ** 2 - (x ** 2 + length_side ** 2 - 2 * cos_135 * x * length_side) - high ** 2, x)
        values.append(legal_value(a))

        # 10
        tdoa = data[9]
        a = sp.solve((sp.sqrt(high ** 2 + (x + o_length) ** 2) + tdoa) ** 2 - ((x + o_length) ** 2 + length_side ** 2 - 2 * cos_135 * (x + o_length) * length_side) - high ** 2, x)
        values.append(legal_value(a))

        # 11
        tdoa = data[10]
        a = sp.solve((sp.sqrt(high ** 2 + x ** 2) + tdoa) ** 2 - (x ** 2 + length_side ** 2 - 2 * cos_135 * x * length_side) - high ** 2, x)
        values.append(legal_value(a))

        # 12
        tdoa = data[11]
        a = sp.solve((sp.sqrt(high ** 2 + (x + i_length) ** 2) + tdoa) ** 2 - ((x + i_length) ** 2 + length_side ** 2 - 2 * cos_135 * (x + i_length) * length_side) - high ** 2, x)
        values.append(legal_value(a))
        values_all.append(values)
    return values_all

def value_cut_avg(datas):
    cut_after_values = []
    for data in datas:
        avg = sum(data) / len(data)
        cut_after_values.append([round(d - avg, 2) for d in data])
    return cut_after_values




def main():

    # test data file
    test_file_name = sys.argv[1]
    datas = read_file(test_file_name)
    print datas
    #new data file
    new_data_file_name = sys.argv[2]
    new_data_file = open(new_data_file_name, 'w')
    values_all = cal_dis_x(datas)
    cut_after_values = value_cut_avg(values_all)
    for c_v in cut_after_values:
        new_data_file.write(str(c_v))
        new_data_file.write('\n')
    new_data_file.close()


if __name__ == '__main__':
    main()