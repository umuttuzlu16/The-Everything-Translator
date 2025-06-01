from UI import scene
from UI import place

app = scene.Scene()

place.user_text(app)
place.translate_text(app)

place.lang(app)

app.run()