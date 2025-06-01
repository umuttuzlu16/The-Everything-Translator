from UI import scene
from UI import place

app = scene.Scene()

place.user_text(app)
place.translate_text(app)

place.lang(app)

for i in range(0,10):
    print(place.liste)

app.run()