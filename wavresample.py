from scipy.io import wavfile


# 读取文件
def wavwrite(wavsrc):
    return wavsrc

# 文件压缩
def wavzip(wavsrc, filename, ziprate):
    # 读取原始文件采样率
    sampleRate, musicdata = wavfile.read(wavsrc)
    # 压缩，储存
    wavfile.write(filename, sampleRate // ziprate, musicdata[::5])


# wavzip("test.wav", "testout.wav", 5) # debug
