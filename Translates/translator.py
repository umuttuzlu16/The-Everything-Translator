from UI import place
from Translates import binary

def language(app):
    opt = place.option.get()
    print(opt)

    if opt == "Binary":
        binary.binary(app)
    elif opt == "Mors":
        pass