import pyglet

# # Create a custom event class that inherits from pyglet.event.Event
class ClankingWidget(pyglet.event.EventDispatcher):
    def clank(self):
        self.dispatch_event('on_clank')

    def click(self, clicks):
        self.dispatch_event('on_clicked', clicks)

    def on_clank(self):
        print('Default clank handler.')

ClankingWidget.register_event_type('on_clank')
ClankingWidget.register_event_type('on_clicked')

# Create a sprite that dispatches the custom event when clicked
class MySprite(pyglet.sprite.Sprite, pyglet.event.EventDispatcher):
    def __init__(self, img, x, y, name):
        super().__init__(img, x, y)
        self.x = x
        self.y = y
        self.name = name

    def on_mouse_press(self, x, y, button, modifiers):
        # Check if the mouse click occurred inside the sprite
        if (x >= self.x and x < self.x + self.width and
            y >= self.y and y < self.y + self.height):
            # Dispatch the custom event
            print(self.name)
            #self.dispatch_event('on_clank')

            return True
            # self.dispatch_event('on_custom_event')

# Register the custom event with the sprite
MySprite.register_event_type('on_custom_event')

# Create a sprite and add an event handler for the custom event
sprite = MySprite(pyglet.image.load('ressources/Aubin_le_GOAT.jpg'), 50, 50,"éez")
sprite2 = MySprite(pyglet.image.load('ressources/Aubin_le_GOAT.jpg'), 60, 60,"aub2")
clank = ClankingWidget()
@sprite.event
def on_custom_event(self):
    print('Custom event occurred!')

@clank.event
def on_clank():
    pass
# Create a window and draw the sprite

window = pyglet.window.Window()
@window.event
def on_draw():
    window.clear()
    sprite.draw()
    sprite2.draw()

event_logger = pyglet.window.event.WindowEventLogger()
# window.push_handlers(event_logger)
window.push_handlers(sprite)
window.push_handlers(sprite2)
window.push_handlers(clank)
# Run the pyglet event loop
pyglet.app.run()