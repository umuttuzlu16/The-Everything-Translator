# Translates\translator.py

from UI import place
from Translates import binary
from Translates import morse

to_ascii = False

def exchange():
    global to_ascii
    if to_ascii == False:
        to_ascii = True
        return True
    else:
        to_ascii = False
        return False

def language(app):
    opt = place.option.get()
    asci = to_ascii

    print(opt)
    print(asci)
    if opt == "Binary":
        if asci == False:
            binary.binary(app)
        else:
            binary.ascii(app)
    elif opt == "Mors":
        if asci == False:
            morse.morse(app)
        else:
            morse.ascii(app)