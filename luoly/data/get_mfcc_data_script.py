import sys
import os
import threading
filename = sys.argv[1]
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

def main():
    path = sys.argv[1]
    distance_file = sys.argv[2]
    allfile = []
    dirlist(path, allfile)
    cmds = []
    for file in allfile:
        if file.endswith("test.wav"):
            cmd =  "python getMfcc.py " + file[:-4] + ">> " + distance_file
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





if __name__ == "__main__":
    main()