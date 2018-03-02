import sys
import os
import threading
cmds = []

def exec_cmd(cmd):
    p = os.popen(cmd)
    x = p.read()
    print x
    p.close()

def dirlist(path, allfile):
    '''
    get all files under path
    :param path:
    :param allfile:
    :return:
    '''
    filelist = os.listdir(path)
    for filename in filelist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            dirlist(filepath, allfile)
        else:
            allfile.append(filepath)
    return allfile

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
    return result


def main():
    result_filename = "result_asvsproof_mfcc"
    filename_origin = '/home/lly/caoch/protocol/ASVspoof2017_eval_v2.trl.txt'
    dir = "/home/lly/caoch/ASVspoof2017_eval/"
    allfilenames = readfile(filename_origin)
    count = 1
    cmds = []
    for i in range(10):
        filenames = allfilenames[i]
        for file in filenames:
            cmd = "python getMfcc_ASVsproof_2.py " + dir + file + " >> " + dir + result_filename + str(i)
            cmds.append(cmd)
            count += 1
            if count % 10 == 0:
                thread_cmd(cmds)
                cmds = []

if __name__ == "__main__":
    main()