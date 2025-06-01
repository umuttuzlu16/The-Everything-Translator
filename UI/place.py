from UI import components


def test(app):
    text = components.TextBox(app.scene, 25,25, 100, 100,("Arial",12), "normal")

def user_text(app):
    user = components.TextBox(app.scene, 25, 25, 515, 60, ("Arial", 12), "normal")