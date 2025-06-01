from UI import components
from Translates import change

def setup(app):
    global user, trans

    user = components.TextBox(app.scene, 25, 25, 502.5, 600, "", ("Arial", 12), "normal")
    trans = components.TextBox(app.scene, 540, 25, 502.5, 600, "", ("Arial", 12), "disabled")

    components.combo(app.scene, 25, 650, "Languages", ("Binary", "Mors"), "readonly")

    components.btn(app.scene, 75, 650, 25, 75, "Translate", "grey",
                   lambda: change.change(app), "black", "green", "red", "Arial", "hand2")
