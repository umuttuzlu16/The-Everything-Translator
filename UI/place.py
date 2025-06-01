from UI import components


def test(app):
    text = components.TextBox(app.scene, 25,25, 100, 100,("Arial",12), "normal")

def user_text(app):
    user = components.TextBox(app.scene, 25, 25, 502.5, 450, ("Arial", 12), "normal")
def translate_text(app):
    user = components.TextBox(app.scene, 540, 25, 502.5, 450, ("Arial", 12), "normal")
    user.disable()