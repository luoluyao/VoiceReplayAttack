import sys

def get_classifier(value, thr, label):
    '''

    :param value:
    :param thr:
    :return:
    1: FP
    2: FN
    3: TP,TN
    '''
    if label == -1:
        if value > thr:
            return 1
    elif label == 1:
        if value <= thr:
            return 2
    return 3

def read_origin_label(filename):
    file = open(filename)
    lines = file.readlines()
    labels = []
    for line in lines:
        l = line.split(" ")
        labels.append(int(l[0]))
    file.close()
    return labels


def eer_calc(p_values,filename, test_file_name):
   '''
   calc EER using svm data
   :param labels:
   :param p_values:
   :return:
   '''
   thrs = set()
   for p_val in p_values:
       thrs.add(p_val[0])
       #thrs.add(p_val)

   p_label_count = 0
   n_label_count = 0
   labels = read_origin_label(test_file_name)
   for l in labels:
       if l == 1:
           p_label_count += 1
       elif l == -1:
           n_label_count += 1

   all_data_count = len(p_values)

   min_diff_value = 1
   min_thr = -1
   fpr_equal = 0
   fnr_equal = 0

   counts = 0
   for thr in thrs:
       counts += 1
       fp_count = 0
       fn_count = 0
       for count in range(all_data_count):
           labels_value = get_classifier(p_values[count][0], thr, labels[count])
           #labels_value = get_classifier(p_values[count], thr, labels[count])
           if labels_value == 1:
               fp_count += 1
           elif labels_value == 2:
               fn_count += 1
       fpr = float(fp_count) / n_label_count
       fnr = float(fn_count) / p_label_count
       if abs(fpr - fnr) < min_diff_value:
           min_diff_value = abs(fpr- fnr)
           fnr_equal = fnr
           fpr_equal = fpr
           min_thr = thr
   f = open(filename + "result_dev", "w")
   f.write("min_diff:" + str(min_diff_value) + "\n")
   f.write("fp:" + str(fpr_equal) + "fn:" + str(fnr_equal) + "\n")
   f.write("thr:" + str(min_thr))
   f.write("avg:" + str((fpr_equal + fnr_equal) / 2))
   f.close()
   print filename



