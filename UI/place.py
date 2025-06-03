from UI import components
from Translates import translator

def setup(app):
    global user, trans, option

    user = components.TextBox(app.scene, 25, 25, 297.5, 360, "", ("Arial", 12), "normal")
    trans = components.TextBox(app.scene, 397.5, 25, 297.5, 360, "", ("Arial", 12), "disabled")

    option = components.combo(app.scene, 25, 405, "Languages", ("Binary", "Mors"), "readonly")

    components.btn(app.scene, 200, 405, 150, 60, "Translate", "white", lambda: translator.language(app), "black", "grey", "white", "Arial", "hand2")
    components.btn(app.scene, 347.5, 60, 25, 25, "", "white", lambda: translator.exchange(), "black", "grey", "white", "Arial", "hand2")

    user_text = components.label(app.scene, "User", 25, 0, "Arial 12", "white", "black", 100)