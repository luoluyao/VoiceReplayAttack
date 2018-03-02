import os
import threading
cmds = []

def exec_cmd(cmd):
    p = os.popen(cmd)
    x = p.read()
    print x
    p.close()

def thread_cmd(cmds):
    # threads pool
    threads = []

    # create four threads
    try:
        for cmd in cmds:
            th = threading.Thread(target=exec_cmd, args=(cmd,))
            print cmd
            th.start()
            threads.append(th)

    except:
        print "Error: unable to start thread"

    for th in threads:
        th.join()

def readfile(filename):
    '''
    get every file name according kinds
    :param filename:
    :return:
    '''
    file = open(filename)
    file_lines = file.readlines()
    result =[[] for i in range(10)]
    for file_line in file_lines:
        words = file_line.split(" ")
        num = int(words[1][1:])
        result[num - 1].append(words[0])
    #print result
    return result

dictionary = {}

def read_groundtruth_data(filename):
    f = open(filename, "r")
    lines = f.readlines()
    for line in lines:
        info_inline = line.strip().split(" ")
        dictionary[info_inline[0]] = info_inline[1]

def main():
    filename_origin = '/home/lly/ASVspoof2017_eval_v2.trl.txt'
    filename_groundtruth = '/home/lly/ASVspoof2017_eval_v2_key.trl.txt'
    read_groundtruth_data(filename_groundtruth)
    allfilenames = readfile(filename_origin)
    dir = "/home/lly/caoch/ASVspoof2017_eval/"
    # just test sentence No.1


    count = 1
    cmds = []
    for filename in allfilenames[0]:
        cmd = ""
        if dictionary[filename] == 'genuine':
            cmd = "python get_mfcc_asvsproof_phoneme_eval.py " + dir + filename + " genuine >> " + dir + "mfcc_file_eval_0"
        elif dictionary[filename] == 'spoof':
            cmd = "python get_mfcc_asvsproof_phoneme_eval.py " + dir + filename + " spoof >> " + dir + "mfcc_file_eval_0"
        cmds.append(cmd)
        if count % 10 == 0:
            thread_cmd(cmds)
            cmds = []
        count += 1


if __name__ == "__main__":
    main()