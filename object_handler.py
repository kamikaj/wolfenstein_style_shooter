from sprite_objects import *
from npc import *

from sprite_objects import SpriteObject, AnimatedSprite


class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = 'resources/sprites/npc/'
        self.static_sprite_path = 'resources/sprites/static_sprites/'
        self.animated_sprite_path = 'resources/sprites/animated_sprites/'
        add_sprite = self.add_sprite
        add_npc = self.add_npc

        #sprite map
        add_sprite(SpriteObject(game))
        add_sprite(AnimatedSprite(game))

        #npc map
        add_npc(NPC(game))

    def update(self):
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]

    def add_npc(self, npc):
        self.npc_list.append(npc)

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)