from python_speech_features import mfcc
import wave
import numpy as np
import string
import sys

import scipy.io.wavfile as wav

MICS_NUMBER = 4

def get_mfcc(sig, rate, winlen):
    '''
    calc mfcc values
    :param sig: .wav data
    :param rate: sample rate
    :param winlen: time of .wav
    :return:
    '''
    mfcc_feat = mfcc(sig, rate, winlen=winlen)
    return mfcc_feat

def analysisFile(path):
    file = open(path)
    datas = file.readlines()
    size = 0
    indexline = 0
    count = 0
    result = []
    realSize = 0
    for data in datas:
        d = data.split(" ")
        if 'intervals:' in d and 'size' in d:
            size = string.atoi(d[len(d) - 1])
            indexline = count
            break
        count += 1
    for i in range(size):
        lineText = datas[i * 4 + 4 +  indexline]
        if 'text = "<p:>"' in lineText:
            continue
        xmaxText = datas[i * 4 + 3 + indexline].strip('\n').split(" ")
        xmax = string.atof(xmaxText[len(xmaxText) - 1])
        xminText = datas[i * 4 + 2 + indexline].strip('\n').split(" ")
        xmin = string.atof(xminText[len(xminText) - 1])
        result.append([xmin, xmax])
        realSize += 1
    file.close()
    return realSize, result

def main():
    filename = sys.argv[1]
    filenameGrid = sys.argv[2]

    sigs = []
    rate = 16000 # default sample rate
    for i in range(MICS_NUMBER):# ATTENTION: filename start from 0
        (rate, sig) = wav.read(filename + i)
        sigs.append(sig)

    phonemesResult = []
    phonemesSize = 4 # default phoneme size
    for i in range(MICS_NUMBER):
        phonemesSize, phonemesResult = analysisFile(filenameGrid + i)
        phonemesResult.append(phonemesResult)

    mfcc_features = []
    for i in range(phonemesSize):
        start_max = phonemesResult[i][0]
        end_min = phonemesResult[i][0]
        for j in range(1, MICS_NUMBER):
            start_max = max(start_max, phonemesResult[i][j][0])
            end_min = min(end_min, phonemesResult[i][j][1])
        start_index = start_max * rate
        end_index = end_min * rate
        winlen = end_index - start_index
        for j in range(MICS_NUMBER):
            mfcc_feature = get_mfcc(sigs[j][start_index : end_index], rate, winlen)
            mfcc_features.append(mfcc_feature)
    print mfcc_features



if __name__ == 'main':
    main()