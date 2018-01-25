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

def get_mfcc_from_files(filename):
    sigs = []
    rate = 16000  # default sample rate
    for i in range(MICS_NUMBER):  # ATTENTION: filename start from 0
        sig, rate = readwav.read_wave_data(filename + str(i) + ".wav")
        sigs.append(sig)

    phonemesResults = []
    phonemesSize = 4  # default phoneme size
    for i in range(MICS_NUMBER):
        phonemesSize, phonemesResult = readwav.analysisFile(filename + str(i) + ".TextGrid")
        phonemesResults.append(phonemesResult)
    mfcc_features = []
    for i in range(phonemesSize):
        start_min = phonemesResults[0][i][0]
        end_max = phonemesResults[0][i][1]
        for j in range(1, MICS_NUMBER):  # using: JIAOJI
            start_min = max(start_min, phonemesResults[j][i][0])
            end_max = min(end_max, phonemesResults[j][i][1])
        if start_min > end_max:  # using: BINGJI
            for m in range(0, MICS_NUMBER):
                start_min = min(start_min, phonemesResults[m][i][0])
                end_max = max(end_max, phonemesResults[m][i][1])
        start_index = int(start_min * rate)
        end_index = int(end_max * rate)
        winlen = end_max - start_min
        for j in range(MICS_NUMBER):
            mfcc_feature = get_mfcc(sigs[j][start_index: end_index], rate, winlen, get_min_two_power(winlen * rate))
            mfcc_features.append(mfcc_feature[0])
    print_data(mfcc_features)

def print_data(features):
    '''
    print data
    :param feature:
    :return:
    '''
    for feature in features:
        count = 0
        string_data = ""
        for f in feature:
            string_data += str(count) + ":" + str(round(f, 2)) + " "
            count += 1
        print string_data

def main():
    filename = sys.argv[1] # ATTENTION: ALL FILES HAVE SAME NAMES
    get_mfcc_from_files(filename)

if __name__ == '__main__':
    main()
