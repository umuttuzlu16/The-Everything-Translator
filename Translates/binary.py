from UI import place

def binary(app):
    text = text = place.user.get()
    translated = ' '.join(format(ord(char), '08b') for char in text)

    place.trans.enable()
    place.trans.set(translated)
    place.trans.disable()