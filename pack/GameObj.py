from cocos.tiles import load
from cocos.layer import ScrollingManager
from cocos.director import director
from pyglet.window import key

class GameObj:
    my_director = director
    my_director.init()
    map_layer = load('map01.tmx')['solid']
    scroller = ScrollingManager()
    keyboard = key.KeyStateHandler()
