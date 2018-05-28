#coding: utf-8
import chardet

def detect_str_encoding():
    inputStr = '当前文件是utf-8, 所以你看到的这段字符串也是utf-8的'
    detectedEncodingDict = chardet.detect(inputStr.encode())
    print('type(detectedEncodingDict)=', type(detectedEncodingDict))
    print('detectedEncodingDict=', detectedEncodingDict)
    detectedEncoding = detectedEncodingDict['encoding']
    print('That is, we have %4.3f%% confidence to say that the input string\
 encoding is %s' % (detectedEncodingDict['confidence']*100, detectedEncoding))


if __name__ == '__main__':
    detect_str_encoding()
