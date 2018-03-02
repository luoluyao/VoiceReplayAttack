from svmutil import *
import sys
import eer_calc

def classify(num):
    # same to train_data_script.py
    file_model_name = "asvsproof/different_sentence/model/model" + str(num)

    # file of test data
    file_test_name = "asvsproof/different_sentence/eval/result_asvsproof_mfcc" + str(num)
    label, data = svm_read_problem(file_test_name)

    model = svm_load_model(file_model_name)
    p_labels, p_acc, p_vals = svm_predict(label, data, model, "-b 1")
    print p_labels
    print p_acc
    print p_vals

    eer_calc.eer_calc(p_vals, file_model_name, file_test_name)
    #eer_calc.eer_calc(p_labels, file_model_name, file_test_name)

def main():
    classify(6)

if __name__ == '__main__':
    main()
