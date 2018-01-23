import sys
import os
import threading
cmds = []

def exec_cmd(cmd):
    p = os.popen(cmd)
    x = p.read()
    print x
    p.close()

def get_result(filename):
    for i in range(0,4):
        cmd = "./maus SIGNAL=" + filename + str(i) + ".wav BPF=youtellme.par OUTFORMAT=TextGrid LANGUAGE=eng-US"
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
    for filename in allfiles:
        print filename
        if filename.endswith('test.wav'):
            get_result(filename[:-4])

def main():
    path = "./"
    allfile = []
    dirlist(path, allfile)
    get_same_file_name(allfile)

if __name__ == "__main__":
    main()

