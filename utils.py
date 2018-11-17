import time
import datetime
from functools import reduce

VOICE_XML_ROOT_PATH = "inputs/musicXMLs/"
WAVS_ROOT = "output/"
LAST_VOICE_WAV = WAVS_ROOT + "voice_last_recording.wav"

# 时间
def tag():
    ts = time.time()
    return datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H-%M-%S')


# 获取文件名称
def text(src):
    text = reduce(lambda accum,x: accum + x, src, "")
    index = text.find('./temp/') + len('./temp/')
    text = text[index:index+40].split(".")[0]
    print ("Get target File:" + text)
    return text
