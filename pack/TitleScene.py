from cocos.text import Label
from cocos.scene import Scene
from cocos.layer import ColorLayer
from cocos.scenes import FlipX3DTransition
from pack.GameScene import GameScene
from pack.HelloScene import HelloScene
from pack.GameObj import GameObj


class TitleScene(Scene):
    def __init__(self):
        super(TitleScene, self).__init__()
        my_layer = ColorLayer(171, 75, 100, 1000)
        text = Label('super dude', font_size = 32, anchor_x = 'center', anchor_y = 'center')
        text.position = GameObj.my_director._window_virtual_width / 2, GameObj.my_director._window_virtual_height / 2
        my_layer.add(text)
        my_layer.is_event_handler = True

        def new_on_key_press(self, key):
            GameObj.my_director.replace(FlipX3DTransition(GameScene(), duration = 2))

        my_layer.on_key_press = new_on_key_press
        self.add(my_layer)