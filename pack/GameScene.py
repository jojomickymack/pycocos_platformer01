from cocos.mapcolliders import RectMapCollider
from cocos.layer import ScrollableLayer, ColorLayer
from cocos.scene import Scene
from cocos.actions import Action
from pyglet.window import key
from pack.GameObj import GameObj
from pack.Player import Player


class GameScene(Scene):
    def __init__(self):
        super(GameScene, self).__init__()
        GameObj.my_director.window.push_handlers(GameObj.keyboard)
        GameObj.scroller.add(GameObj.map_layer, z = 0)
        GameObj.scroller.add(SpriteLayer(), z = 1)
        bg_color = ColorLayer(155, 155, 255, 1000)
        self.add(GameObj.scroller, z = 1)
        self.add(bg_color)


class GameAction(Action, RectMapCollider):
    gravity = 25000
    jump_vel = 4000
    move_vel = 600
    on_ground = False

    def start(self):
        self.target.velocity = 0, 0

    def on_bump_handler(self, vx, vy):
        return (vx, vy)

    def step(self, dt):
        vx, vy = self.target.velocity

        vx = (GameObj.keyboard[key.RIGHT] - GameObj.keyboard[key.LEFT]) * self.move_vel
        if GameObj.keyboard[key.SPACE] and self.on_ground:
            vy += self.jump_vel

        vy -= self.gravity * dt

        dx = vx * dt
        dy = vy * dt

        last = self.target.get_rect()
        new = last.copy()
        new.x += dx
        new.y += dy

        self.target.velocity = self.collide_map(GameObj.map_layer, last, new, dy, dx)
        self.on_ground = (new.y == last.y)
        self.target.position = new.center
        GameObj.scroller.set_focus(*new.center)


class SpriteLayer(ScrollableLayer):
    player = Player()

    def __init__(self):
        super(SpriteLayer, self).__init__()

        self.add(self.player.sprite)
        self.player.sprite.do(GameAction())