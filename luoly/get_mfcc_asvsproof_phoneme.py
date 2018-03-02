from python_speech_features import mfcc
import sys
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
    string_data = "1 "
    for feature in features:
        for f in feature:
            string_data += str(count) + ":" + str(round(f, 2)) + " "
            count += 1
    print string_data


def analyze(filename):
    sig, rate = readwav.read_wave_data(filename)
    phonemesSize, phonemesResult = readwav.analysisFile(filename[:-4] + ".TextGrid")
    mfcc_features = []
    for i in range(phonemesSize):
        start_index = int(phonemesResult[i][0] * rate)
        end_index = int(phonemesResult[i][1] * rate)
        winlen = phonemesResult[i][1] - phonemesResult[i][0]
        mfcc_feature = get_mfcc(sig[start_index: end_index], rate, winlen, get_min_two_power(winlen * rate))
        mfcc_features.append(mfcc_feature[0])
    ## origin data:
    index = phonemesResult[0][0]
    end = phonemesResult[phonemesSize - 1][1]
    winlen = end - index
    mfcc_feature = get_mfcc(sig, rate, winlen, get_min_two_power(winlen * rate))
    mfcc_features.append(mfcc_feature[0])

    ##
    print_data(mfcc_features)


def main():
    filename = sys.argv[1]
    analyze(filename)


if __name__ == "__main__":
    main()