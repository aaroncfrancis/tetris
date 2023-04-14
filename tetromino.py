from settings import *
import random

class Block(pg.sprite.Sprite):
    def __init__(self, tetromino, pos):
        self.tetromino = tetromino
        self.pos = vec(pos) + init_pos_offset
    
        """to draw block pass it to parent of constructor"""
        super().__init__(tetromino.tetris.spriteGroup)
        self.image = pg.Surface([tileSize, tileSize])
        self.image.fill('orange')
        self.rect = self.image.get_rect()
        
    def set_rect_pos(self):
        self.rect.topleft = self.pos * tileSize
    
    def update(self):
        self.set_rect_pos()

class Tetromino:
    def __init__(self, tetris):
        self.tetris = tetris
        self.shape = random.choice(list(tetrominoes.keys()))
        self.blocks = [Block(self, pos) for pos in tetrominoes[self.shape]]

    def move(self, direction):
        moveDirection = moveDirections[direction]
        for block in self.blocks:
            block.pos += moveDirection

    def update(self):
        self.move(direction='down')