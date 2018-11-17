import math
from utils import *
from hyphenator import Hyphenator


def cleanText(text):
    text.replace("\n", " ")
    text = text.lower()
    symbolsToDelete = ".,'!?" + '"'
    for symbol in symbolsToDelete:
        text = text.replace(symbol, "")
    return text


def separarEnSilabas(text):
    text = cleanText(text)
    print(text)
    h = Hyphenator("hyph_en_US.dic")
    textSyllables = h.inserted(text)
    print(textSyllables)
    return list(filter(lambda x: len(x) > 0, textSyllables.replace(" ", "-").split("-")))


def addVoiceTags(tempo, text, content):
    output = ""
    tempo_xml = '<direction>\n<sound tempo="{}"/>\n</direction>'.format(tempo)
    lyrics_xml = '<voice>1</voice>\n<lyric>\n<text>{}</text>\n</lyric>'
    i = 0
    for line in content:
        if "</note" in line:
            output += lyrics_xml.format(text[i])
            i += 1
        output += line
        if tempo != -1 and "<measure" in line:
            output += tempo_xml
    return output


def musicGenerator(tempo, text, content):
    text = separarEnSilabas(text)
    print(text)
    if len(text) < len(content):
        text = (text * int(math.ceil(len(content) / float(len(text)))))[:len(content)]
    return addVoiceTags(tempo, text, content)


def main(textFilePath, musicXMLPath, tempo):
    with open(textFilePath, 'r') as text:
        lyrics = text.read()

    with open(musicXMLPath, 'r') as c:
        content = [x.strip() for x in c.readlines()]
        with open(VOICE_XML_ROOT_PATH + 'voice.xml', 'w') as f:
            f.write(musicGenerator(tempo, lyrics, content))


if __name__ == "__main__":
    textFilePath = "test.txt"
    musicXMLPath = "test.musicxml"
    tempo = 0

    print(textFilePath)
    print(musicXMLPath)
    if tempo == 0:
        tempo = 80
    else:
        tempo = 120
    print(tempo)
    main(textFilePath, musicXMLPath, tempo)

