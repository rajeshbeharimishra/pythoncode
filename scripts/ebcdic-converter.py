import codecs

with open("c:\\Users\\rbmishra\\downloads\\FLEXCAB_DEFLIST_20220801050204_2940.dat", "rb") as ebcdic:
    ascii_txt = codecs.decode(ebcdic.read(), "cp500")
    print(ascii_txt)
