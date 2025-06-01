import components


def test(app):
    text = components.TextBox(app.scene, 25,25, 100, 100,("Arial",12), "normal")