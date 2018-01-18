import sys

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


def main():

    # test data file
    test_file_name = sys.argv[1]
    datas = read_file(test_file_name)
    print datas

    # new data file
    new_data_file_name = sys.argv[2]
    new_data_file = open(new_data_file_name, 'w')

    feature_file_name = "feature"
    feature = open(feature_file_name)
    feature_data = feature.readline()
    feature_datas = feature_data.split(',')
    processed_data = [round(datas[0][i] - float(feature_datas[i]), 2) for i in range(one_set_sample)]
    print processed_data
    new_data_file.write(str(processed_data))
    feature.close()
    new_data_file.close()

if __name__ == '__main__':
    main()