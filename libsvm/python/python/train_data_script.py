from svmutil import *

def train_data(svm_type, kernel_type):
    # file to save model
    #file_model_name = "asvsproof/model/model_file" + "_" + str(svm_type) + "_" + str(kernel_type)
    file_model_name = "asvsproof/phoneme/model/model" + "_" + str(svm_type) + "_" + str(kernel_type)
    # file of training data
    #file_training_name = "asvsproof/train_train"
    file_training_name = "asvsproof/phoneme/sentence0/mfcc_file_all"
    label, data = svm_read_problem(file_training_name)


    # -s  2 -- one-class SVM
    # -t 2 -- radial basis function: exp(-gamma*|u-v|^2)
    # -n 0.5 default
    # model = svm_train(label, data, '-s 0 -t 1 -n 0.5')


    option = '-s '+ str(svm_type) + ' -t ' + str(kernel_type) + ' -n 0.5 -b 1'
    print option
    model = svm_train(label, data, option)
    svm_save_model(file_model_name, model)
    # p_labels, p_acc, p_vals = svm_predict(label, data, model, "-b 1")
    # print p_vals


def main():
    for i in range(5):
        if i == 2:
            continue
        for j in range(4):
            train_data(i, j)

if __name__ == "__main__":
    main()

