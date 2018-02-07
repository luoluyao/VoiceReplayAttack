from svmutil import *
import sys
import eer_calc

# same to train_data_script.py
file_model_name = "model_file"

# file of test data
file_test_name = "asvsproof/test_eval"
label, data = svm_read_problem(file_test_name)

model = svm_load_model(file_model_name)
p_labels, p_acc, p_vals = svm_predict(label, data, model, "-b 1")

print p_labels
print p_acc
print len(p_vals)
print p_vals

eer_calc.eer_calc(p_vals, file_test_name)







