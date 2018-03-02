from svmutil import *
import sys
import eer_calc

def classify(file_model):
    # same to train_data_script.py
    file_model_name = file_model

    # file of test data
    #file_test_name = "asvsproof/test_dev"
    file_test_name = "asvsproof/phoneme/sentence0/mfcc_file_eval"
    label, data = svm_read_problem(file_test_name)

    model = svm_load_model(file_model_name)
    p_labels, p_acc, p_vals = svm_predict(label, data, model, "-b 1")
    print p_labels
    print p_acc
    print p_vals

    eer_calc.eer_calc(p_vals, file_model_name, file_test_name)
    #eer_calc.eer_calc(p_labels, file_model_name, file_test_name) # 2 places need to record

def main():
    # file_name = "asvsproof/model/model_file"
    file_name = "asvsproof/phoneme/model/model"
    for i in range(0, 2):
        if i == 2:
            continue
        #for j in range(4):
        for j in range(2,3):
            f_name = file_name + "_" + str(i) + "_" + str(j)
            classify(f_name)

if __name__ == '__main__':
    main()
