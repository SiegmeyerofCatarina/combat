import random
import pyglet
pyglet.options['debug_gl'] = False

class GameWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super(GameWindow, self).__init__(*args, **kwargs)
        pyglet.clock.schedule_interval(self.update, 1.0/60.0)
        self.labelList = []
        # self.fps_display = pyglet.clock.Clock()
        self.fps_display = pyglet.window.FPSDisplay(window=self)
        self.labelBatch = pyglet.graphics.Batch()
        bunny = pyglet.image.load('bunny.png')
        for i in range(20):
            # label = pyglet.text.Label('Hello, world',
            # font_name='Times New Roman',
            # font_size=36,
            label = pyglet.sprite.Sprite(bunny,
            x=self.width//2, y=self.height//2,
            # anchor_x='center', anchor_y='center',
            batch = self.labelBatch)
            self.labelList.append(label)

    def update(self, dt):
        for la in self.labelList:
            la.x += random.randint(0, 10)-5
            la.y += random.randint(0, 10)-5

    def on_draw(self):
        self.clear()
        self.labelBatch.draw()
        self.fps_display.draw()

if __name__ == "__main__":
    
    game = GameWindow(width=800, height=600)
    pyglet.app.run()