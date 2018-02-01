from python_speech_features import mfcc
import wave
import numpy as np
import string
import sys
import scipy.io.wavfile as wav
import readwav

MICS_NUMBER = 4

# record dictionary
dictionary = {}

def get_mfcc(sig, rate, winlen, nfft):
    '''
    calc mfcc values
    :param sig: .wav data
    :param rate: sample rate
    :param winlen: time of .wav
    :return:
    '''
    mfcc_feat = mfcc(sig, rate, winlen=winlen, nfft=nfft)
    return mfcc_feat

def get_min_two_power(value):
    '''
    :param value:
    :return:  min > value and min is 2 power
    '''
    min_default = 512
    while min_default < value:
        min_default *= 2
    return min_default

def print_data(features, filename):
    '''
    print data
    :param feature:
    :return:
    '''
    count = 0
    string_data = ""
    short_filename = filename.strip().split("/")
    if dictionary[short_filename[-1]] == 'genuine':
        string_data = "1 "
    elif dictionary[short_filename[-1]] == 'spoof':
        string_data = "-1 "
    for feature in features:
        string_data += str(count) + ":" + str(round(feature, 2)) + " "
        count += 1
    print string_data

def get_mfcc_from_files(filename):
    rate = 16000  # default sample rate
    sigs = []
    sig, rate = readwav.read_wave_data(filename)
    sigs.append(sig)
    winlen = len(sig) / float(rate)
    mfcc_feature = get_mfcc(sig, rate, winlen, get_min_two_power(winlen * rate))
    print_data(mfcc_feature[0], filename)

def read_groundtruth_data(filename):
    f = open(filename, "r")
    lines = f.readlines()
    for line in lines:
        info_inline = line.strip().split(" ")
        dictionary[info_inline[0]] = info_inline[1]
    # print dictionary

def main():
    filename_groundtruth = '/home/lly/caoch/ASVspoof2017_eval/ASVspoof2017_eval_v2_key.trl.txt' # ATTENTION: ALL FILES HAVE SAME NAMES
    filename_data = sys.argv[1]
    read_groundtruth_data(filename_groundtruth)
    get_mfcc_from_files(filename_data)


if __name__ == '__main__':
    main()
