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
        self.speedUp = False
    
    def checkFullLines(self):
        row = field_h - 1
        for y in range(field_h - 1, -1, -1):
            for x in range(field_w):
                self.fieldArray[row][x] = self.fieldArray[y][x]

                if self.fieldArray[y][x]:
                    self.fieldArray[row][x].pos = vec(x,y)

            if sum(map(bool, self.fieldArray[y])) < field_w:
                row -= 1 # drop row 
            else: 
                for x in range(field_w):
                    self.fieldArray[row][x].alive = False
                    self.fieldArray[row][x] = 0

    def putTetrominoBlocksInArray(self):
        """storing pointer that we will use to calculate collisions when called"""
        for block in self.tetromino.blocks:
            x,y = int(block.pos.x), int(block.pos.y)
            self.fieldArray[y][x] = block
    
    def getFieldArray(self):
        return [[0 for x in range(field_w)] for y in range(field_h)]

    def checkTetrominoLanding(self): #new method that will be called in update
        if self.tetromino.landing:
            self.speedUp = False
            self.putTetrominoBlocksInArray()
            self.tetromino = Tetromino(self)

    def control(self, keyPress):
        if keyPress == pg.K_LEFT:
            self.tetromino.move(direction='left')
        elif keyPress == pg.K_RIGHT:
            self.tetromino.move(direction='right')
        elif keyPress == pg.K_UP:
            self.tetromino.rotate()
        elif keyPress == pg.K_DOWN:
            self.speedUp = True

    def draw_grid(self):
        for x in range(field_w):
            for y in range (field_h):
                pg.draw.rect(self.app.screen, 'black', (x * tileSize, y * tileSize, tileSize, tileSize),1)

    def update(self):
        trigger = [self.app.anim_trigger, self.app.fast_anim_trigger][self.speedUp]
        if trigger:
            self.checkFullLines()  
            self.tetromino.update()
            self.checkTetrominoLanding()
        self.spriteGroup.update()

    def draw(self):
        self.draw_grid()
        self.spriteGroup.draw(self.app.screen)
