from cocos.text import Label
from cocos.scene import Scene
from cocos.layer import ColorLayer
from pack.GameObj import GameObj


class HelloScene(Scene):
    def __init__(self):
        super(HelloScene, self).__init__()
        my_layer = ColorLayer(171, 75, 100, 1000)
        text = Label('Hello Everyone',
            font_name = 'Times New Roman',
            font_size = 32,
            anchor_x = 'center',
            anchor_y = 'center'
        )

        text.position = GameObj.my_director._window_virtual_width / 2, GameObj.my_director._window_virtual_height / 2
        my_layer.add(text)