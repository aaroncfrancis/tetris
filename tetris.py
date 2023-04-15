from settings import *
import math
from tetromino import Tetromino

class Tetris:
    def __init__(self, app): 
        """input of the constructor is an application instance"""
        self.app = app
        self.spriteGroup = pg.sprite.Group()
        self.fieldArray = self.getFieldArray()
        self.tetromino = Tetromino(self)

    def putTetrominoBlocksInArray(self):
        """storing pointer that we will use to calculate collisions when called"""
        for block in self.tetromino.blocks:
            x,y = int(block.pos.x), int(block.pos.y)
            self.fieldArray[y][x] = block
    
    def getFieldArray(self):
        return [[0 for x in range(field_w)] for y in range(field_h)]

    def checkTetrominoLanding(self): #new method that will be called in update
        if self.tetromino.landing:
            self.putTetrominoBlocksInArray()
            self.tetromino = Tetromino(self)

    def control(self, keyPress):
        if keyPress == pg.K_LEFT:
            self.tetromino.move(direction='left')
        elif keyPress == pg.K_RIGHT:
            self.tetromino.move(direction='right')

    def draw_grid(self):
        for x in range(field_w):
            for y in range (field_h):
                pg.draw.rect(self.app.screen, 'black', (x * tileSize, y * tileSize, tileSize, tileSize),1)

    def update(self):
        if self.app.anim_trigger:  
            self.tetromino.update()
            self.checkTetrominoLanding()
        self.spriteGroup.update()

    def draw(self):
        self.draw_grid()
        self.spriteGroup.draw(self.app.screen)
