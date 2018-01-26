# 文件说明
## generatePar.py

  * 使用maus切割，生成TextGrid文件
  
  * $ python generatePar.py **<filename(.wav not include)>**
  
  * **注意** 里面有个 //BPF=youtellme.par// 需要换成新的文件
  
## generateResult.py
  
  * 用于批量执行readwav.py 脚本
  
  * 输出三个麦克风与某一个麦克风的Tdoa（sample数） （**注意采样频率**）
  
  * 输出mfcc值 （**新增的**）
   
  * $ python generateResult.py **<filename(.wav not include)>**
  
## readwav.py

 * 输入：两个音频文件(.wav)和对应的TextGrid文件
 * 输出：三个麦克风与某一个麦克风各个音素的tdoa
 
 ## classify/python
 
 * 该文件夹提供检测异常（即，机器发声）的算法，包括svm。
 
 ## getMfcc.py
 
 * 用于获得音频文件对应的mfcc值
 
 * 输入：运行时，只要输入文件的名称。（实际会读入,4个.wav文件,4个TextGrid文件）
 
 * 输出：mfcc值，每个麦克风每个音素都会得到13个特征。最后输出 麦克风数*音素个数*13 个数据。
 
 * 环境支持：[mfcc库](https://github.com/luoluyao/python_speech_features) （需要先安装该库的环境才可以使用。可以使用以下命令安装 **pip install python_speech_features**）
 
 * 注意：在**generateResult.py** 已经增加了执行该脚本的代码，最终结果会存储到 **mfcc_record** 文件中。 
 
 * $ python getMfcc.py test-
 
  （**“test-”**是总名称，它实际包含了，test-0.wav，test-1.wav，..., test-0.TextGrid，...等**8个文件**）
  
 * 注意：**getMfcc_no_phoneme.py**也是类似的，只是，它是对整个原音频进行分析的。
 
## get_mfcc_data_script.py

* 用于批量处理执行 **getMfcc.py**脚本

* 输入包含音频文件和TextGrid文件的大目录，和 输出的log的文件名

* 输出mfcc的数据到原本的文件名中

* $ python get_mfcc_data_script.py sound/sound/machine/wav_machine_60cm/ mfcclog_no_phoneme/60cm_machine

* 注意：**get_mfcc_no_phoneme_data_script.py**类似。



## process.m

 * 输入：音频文件，及切割时间
 * 输出：各个音素时间差
 * 与 readwav区别是：使用的是matlab本身的互相关函数
