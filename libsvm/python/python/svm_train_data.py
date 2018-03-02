from svmutil import *

# for i in range(10):
    # file to save model
    #file_model_name = "asvsproof/different_sentence/model/model" + str(i)

    # file of training data
    #file_training_name = "asvsproof/different_sentence/" \
                         # "train_human_machine/result_asvsproof_mfcc" + str(i)

file_model_name = "asvsproof/phoneme/model/" + "/model1"
file_training_name = "asvsproof/phoneme/sentence0/mfcc_file_all"
label, data = svm_read_problem(file_training_name)

# -s  2 -- one-class SVM
# -t 2 -- radial basis function: exp(-gamma*|u-v|^2)
# -n 0.5 default
model = svm_train(label, data, '-s 1 -t 0 -n 0.5 -b 1')
svm_save_model(file_model_name, model)
p_labels, p_acc, p_vals = svm_predict(label, data, model)
print p_labels
print p_acc
print p_vals
