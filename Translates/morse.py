# Translates\morse.py

import json
from UI import place
import os

file_path = os.path.join(os.path.dirname(__file__), "morse.json")
with open(file_path, "r", encoding="utf-8") as f:
    morse_dict = json.load(f)

reverse_morse_dict = {v: k for k, v in morse_dict.items()}

def morse(app):
    try:
        message = place.user.get()
        translated = ''
        for letter in message:
            if letter in morse_dict:
                translated += morse_dict[letter.upper()] + ' '
            elif letter == ' ':
                translated += '  '
            else:
                translated += '? '
        
        place.trans.enable()
        place.user_text.config("Ascii", "White", "Arial 12")
        place.trans_text.config("Morse", "white", "Arial 12")
        place.trans.set(translated)
        place.trans.disable()
    except Exception as e:
        place.trans.set(f"Invalid Text {e}")
        place.user_text.config("Ascii", "red", "Arial 12")
        place.trans_text.config("Morse", "red", "Arial 12")

def ascii(app):
    try:
        message = place.user.get()
        message += ' '
        translated = ''
        citext = ''
        space_count = 0

        for letter in message:
            if letter != ' ':
                space_count = 0
                citext += letter
            else:
                space_count += 1
                if space_count == 1:
                    translated += reverse_morse_dict.get(citext, '?')
                    citext = ''
                elif space_count == 2:
                    translated += ' '

        place.trans.enable()
        place.user_text.config("Morse", "white", "Arial 12")
        place.trans_text.config("Ascii", "white", "Arial 12")
        place.trans.set(translated)
        place.trans.disable()
    except Exception as e:
        place.trans.set(f"Invalid Text: {e}")
        place.user_text.config("Morse", "red", "Arial 12")
        place.trans_text.config("Ascii", "red", "Arial 12")