# Get Lang
def lang():
    print("Language Option: ")
    print("\tja :Japanese")
    print("\tch :Chinese")
    print("\ten :English")
    langs = "1" # defult
    lang = input("Please input language:")
    if lang == "ja":
        print("Voice List:")
        print("\ta :f00001j : Yoko ")
        print("\tb :f00002j : XiangLing ")
        print("\tc :f00004j_beta : Namine Ritsu S ")
        print("\td :f00005j : undefined ")
        print("\te :m01083j : undefined ")
        print("\tf :f00001j_dnn_beta2 : Yoko")
        langc = input("Please input vocal:")
        if langc == "a":
            langs = "0"
            return langs
        elif langc == "b":
            langs = "1"
            return langs
        elif langc == "c":
            langs = "2"
            return langs
        elif langc == "d":
            langs = "3"
            return langs
        elif langc == "e":
            langs = "7"
            return langs
        elif langc == "f":
            langs = "8"
            return langs
        else:
            print("Error:Unknown command,Set to default")
            return "1"
    elif lang == "ch":
        print("Voice List:")
        print("\ta :f00002m : XiangLing ")
        langc = input("Please input vocal:")
        if langc == "a":
            langs = "6"
            return langs
        else:
            print("Error:Unknown command,Set to default")
            return "1"
    elif lang == "en":
        print("Voice List:")
        print("\ta :f00002e : XiangLing ")
        print("\tb :f00003e : Matsou-P  ")
        langc = input("Please input vocal:")
        if langc == "a":
            langs = "4"
            return langs
        elif langc == "b":
            langs = "5"
            return langs
        else:
            print("Error:Unknown command,Set to default")
            return "1"
    else:
        print("Error:Unknown command,Set to default")
        return "1"


def langstr(lang):
    if lang == "0":
        return "japanese"
    if lang == "1":
        return "japanese"
    if lang == "2":
        return "japanese"
    if lang == "3":
        return "japanese"
    if lang == "7":
        return "japanese"
    if lang == "8":
        return "japanese"
    if lang == "4":
        return "english"
    if lang == "5":
        return "english"
    if lang == "6":
        return "chinese"


def langnum(lang):
    if lang == "ja":
        print("Voice List:")
        print("\ta :f00001j : Yoko ")
        print("\tb :f00002j : XiangLing ")
        print("\tc :f00004j_beta : Namine Ritsu S ")
        print("\td :f00005j : undefined ")
        print("\te :m01083j : undefined ")
        print("\tf :f00001j_dnn_beta2 : Yoko")
        langc = input("Please input vocal:")
        if langc == "a":
            langs = "0"
            return langs
        elif langc == "b":
            langs = "1"
            return langs
        elif langc == "c":
            langs = "2"
            return langs
        elif langc == "d":
            langs = "3"
            return langs
        elif langc == "e":
            langs = "7"
            return langs
        elif langc == "f":
            langs = "8"
            return langs
        else:
            print("Error:Unknown command,Set to default")
            return "1"
    elif lang == "ch":
        print("Voice List:")
        print("\ta :f00002m : XiangLing ")
        langc = input("Please input vocal:")
        if langc == "a":
            langs = "6"
            return langs
        else:
            print("Error:Unknown command,Set to default")
            return "1"
    elif lang == "en":
        print("Voice List:")
        print("\ta :f00002e : XiangLing ")
        print("\tb :f00003e : Matsou-P  ")
        langc = input("Please input vocal:")
        if langc == "a":
            langs = "4"
            return langs
        elif langc == "b":
            langs = "5"
            return langs
        else:
            print("Error:Unknown command,Set to default")
            return "1"
    else:
        print("Error:Unknown command,Set to default")
        return "1"
