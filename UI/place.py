from UI import components
from Translates import change
from Translates import translator

def setup(app):
    global user, trans, option

    user = components.TextBox(app.scene, 25, 25, 502.5, 600, "", ("Arial", 12), "normal")
    trans = components.TextBox(app.scene, 540, 25, 502.5, 600, "", ("Arial", 12), "disabled")

    option = components.combo(app.scene, 25, 650, "Languages", ("Binary", "Mors"), "readonly")

    components.btn(app.scene, 75, 650, 25, 75, "Translate", "grey", lambda: translator.language(app), "black", "green", "red", "Arial", "hand2")
