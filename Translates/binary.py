# Translates\binary.py

from UI import place

def binary(app):
    text = text = place.user.get()
    translated = ' '.join(format(ord(char), '08b') for char in text)

    place.trans.enable()
    place.trans.set(translated)
    place.trans.disable()

def ascii(app):
    text = place.user.get()
    text = text.replace(" ", "")
    translated = ''.join(chr(int(text[i:i+8], 2)) for i in range(0, len(text), 8))

    place.trans.enable()
    place.trans.set(translated)
    place.trans.disable()