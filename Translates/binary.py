# Translates\binary.py

from UI import place

def binary(app):
    try:
        text = text = place.user.get()
        translated = ' '.join(format(ord(char), '08b') for char in text)

        place.trans.enable()
        place.user_text.config("Ascii", "White", "Arial 12")
        place.trans_text.config("Binary", "white", "Arial 12")
        place.trans.set(translated)
        place.trans.disable()
    except Exception as e:
        place.trans.set(f"Invalid Text {e}")
        place.user_text.config("Ascii", "red", "Arial 12")
        place.trans_text.config("Binary", "red", "Arial 12")

def ascii(app):
    try:
        text = place.user.get()
        text = text.replace(" ", "")
        translated = ''.join(chr(int(text[i:i+8], 2)) for i in range(0, len(text), 8))

        place.trans.enable()
        place.user_text.config("Binary", "white", "Arial 12")
        place.trans_text.config("Ascii", "white", "Arial 12")
        place.trans.set(translated)
        place.trans.disable()
    except Exception as e:
        place.trans.set(f"Invalid Text: {e}")
        place.user_text.config("Binary", "red", "Arial 12")
        place.trans_text.config("Ascii", "red", "Arial 12")