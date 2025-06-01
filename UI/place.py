from UI import components


def user_text(app):
    user = components.TextBox(app.scene, 25, 25, 502.5, 600, "",("Arial", 12), "normal")
    return user.get()

def translate_text(app):
    trans = components.TextBox(app.scene, 540, 25, 502.5, 600, user_text(app), ("Arial", 12), "normal")
    trans.disable()

def lang(app):
    langs = components.combo(app.scene, 25, 650, "Languages", ("Binary", "Mors"), "readonly")