from UI import place

def change(app):
    text = place.user.get()

    place.trans.enable()
    place.trans.set(text)
    place.trans.disable()

    print("Debug")
    print(text)
