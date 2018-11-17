import os


# 下载(语言，语言名称，XML文件)
def curl(lang, langstr, XML):
    f = os.popen("curl -X POST -F 'SPKR_LANG=" + langstr + "' -F 'SPKR=" + lang +"' -F 'SYNALPHA=0.55' -F 'VIBPOWER=1' -F 'F0SHIFT=0' -F  'SYNSRC=@" + XML + "' http://sinsy.sp.nitech.ac.jp/index.php | grep 'lf0'")
    textsrc = f.readlines()
    return textsrc