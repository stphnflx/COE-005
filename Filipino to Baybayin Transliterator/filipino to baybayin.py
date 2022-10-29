from hyphenator import hyphenate as hyp
#baybayin in unicode
baybay={"a":"\u1700","a":"\u1700","i":"\u1701","u":"\u1702",
        "ka":"\u1703","ga":"\u1704","nga":"\u1705","ta":"\u1706",
        "da":"\u1707","na":"\u1708","pa":"\u1709","ba":"\u170A",
        "ma":"\u170B","ya":"\u170C","ra":"\u170D","la":"\u170E",
        "wa":"\u170F","sa":"\u1710","ha":"\u1711","k":"\u1703\u1714",
        "g":"\u1704\u1714","ng":"\u1705\u1714","t":"\u1706\u1714","d":"\u1707\u1714",
        "n":"\u1708\u1714","p":"\u1709\u1714","b":"\u170A\u1714","m":"\u170B\u1714",
        "y":"\u170C\u1714","r":"\u170D\u1714","l":"\u170E\u1714","w":"\u170F\u1714",
        "s":"\u1710\u1714","h":"\u1711\u1714","ki":"\u1703\u1712","gi":"\u1704\u1712",
        "ngi":"\u1705\u1712","ti":"\u1706\u1712","di":"\u1707\u1712","ni":"\u1708\u1712",
        "pi":"\u1709\u1712","bi":"\u170A\u1712","mi":"\u170B\u1712","yi":"\u170C\u1712",
        "ri":"\u170D\u1712","li":"\u170E\u1712","wi":"\u170F\u1712","si":"\u1710\u1712",
        "hi":"\u1711\u1712","ku":"\u1703\u1713","gu":"\u1704\u1713","ngu":"\u1705\u1713",
        "tu":"\u1706\u1713","du":"\u1707\u1713","nu":"\u1708\u1713","pu":"\u1709\u1713",
        "bu":"\u170A\u1713","mu":"\u170B\u1713","yu":"\u170C\u1713","ru":"\u170D\u1713",
        "lu":"\u170C\u1713","wu":"\u170F\u1713","su":"\u1710\u1713","hu":"\u1711\u1713",
        ".":".",",":",","?":"?","!":"!"
        }

baybayed=""
while True:
    word=input("word: ")
    hyp_word=hyp(word)
    print(hyp_word)
    

    for element in hyp_word:
        baybayed=baybayed+baybay[element]

    print (baybayed)
    baybayed=""
