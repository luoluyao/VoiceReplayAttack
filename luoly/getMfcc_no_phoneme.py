from python_speech_features import mfcc
import wave
import numpy as np
import string
import sys
import scipy.io.wavfile as wav
import readwav

MICS_NUMBER = 4

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

def print_data(features):
    '''
    print data
    :param feature:
    :return:
    '''
    count = 0
    string_data = "-1 "
    for feature in features:
        string_data += str(count) + ":" + str(round(feature, 2)) + " "
        count += 1
    print string_data

def get_mfcc_from_files(filename):
    rate = 16000  # default sample rate
    sigs = []
    for i in range(MICS_NUMBER):  # ATTENTION: filename start from 0
        sig, rate = readwav.read_wave_data(filename + str(i) + ".wav")
        sigs.append(sig)
        winlen = len(sig) / float(rate)
        mfcc_feature = get_mfcc(sig, rate, winlen, get_min_two_power(winlen * rate))
        print_data(mfcc_feature[0])

def main():
    filename = sys.argv[1] # ATTENTION: ALL FILES HAVE SAME NAMES
    get_mfcc_from_files(filename)

if __name__ == '__main__':
    main()
