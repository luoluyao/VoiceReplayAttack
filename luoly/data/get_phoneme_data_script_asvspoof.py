import sys
import os
import threading

# record dictionary
dictionary = {}

def exec_cmd(cmd):
    p = os.popen(cmd)
    x = p.read()
    print x
    p.close()

def get_result(filenames):
    cmds = []
    for filename in filenames:
        origin_name = filename
        if "/" in filename:
            f_name = filename.split("/")
            origin_name = f_name[len(f_name) - 1]
        cmd = "./maus SIGNAL=" + filename  +" BPF=" + str(dictionary[origin_name]) + ".par OUTFORMAT=TextGrid LANGUAGE=eng-US"
        cmds.append(cmd)
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

def get_same_file_name(allfiles):
    '''
    remove same files
    :param allfiles:
    :return:
    '''
    size = len(allfiles)
    one_size = size / 10
    for i in range(one_size + 1):
        end = min((i + 1) * 10, size)
        partfiles = allfiles[i * 10 : end]
        filenames = []
        for filename in partfiles:
            newfilename = filename[:-4] + ".TextGrid"
            if newfilename in allfiles:
                continue
            if filename.endswith('.wav'):
                filenames.append(filename)
        get_result(filenames)

def read_groundtruth_data_content(filename):
    f = open(filename, "r")
    lines = f.readlines()
    for line in lines:
        info_inline = line.strip().split(" ")
        dictionary[info_inline[0]] = info_inline[3]

def main():
    path = sys.argv[1]
    file_data_content = sys.argv[2]
    read_groundtruth_data_content(file_data_content)
    allfile = []
    dirlist(path, allfile)
    get_same_file_name(allfile)

if __name__ == "__main__":
    main()

