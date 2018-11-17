import numpy as np
import wave as we
import matplotlib.pyplot as plt

# 读取wav
def wavread(path):
    wavfile = we.open(path, "rb")
    params = wavfile.getparams()
    nchannels, sampwidth, framesra, frameswav = params[:4]
    print("nchannels:%d" % nchannels)
    print("sampwidth:%d" % sampwidth)
    datawav = wavfile.readframes(frameswav)
    wavfile.close()
    datause = np.fromstring(datawav, dtype=np.short)
    print(len(datause))
    if nchannels == 2:
        datause.shape = -1, 2
    datause = datause.T
    time = np.arange(0, frameswav) * (1.0 / framesra)
    return datause, time, nchannels


# 绘制wav
def wavedraw(wav_path):
    path = wav_path
    print(path)
    wavdata, wavtime, nchannels = wavread(path)
    df = 1
    freq = [df * n for n in range(0, len(wavdata))]
    print(len(wavtime))
    c = np.fft.fft(wavdata) * nchannels
    fig, ax = plt.subplots(2, 1)
    ax[0].plot(wavtime, wavdata, color='green')
    ax[0].set_xlabel('Time')
    ax[0].set_ylabel('Amplitude')
    ax[1].plot(freq, abs(c), color='red')
    ax[1].set_xlabel('Freq(HZ)')
    ax[1].set_ylabel('Y(freq)')
    plt.show()
