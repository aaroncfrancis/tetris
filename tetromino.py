from settings import *
import random

class Block(pg.sprite.Sprite):
    def __init__(self, tetromino, pos):
        self.tetromino = tetromino
        self.pos = vec(pos) + init_pos_offset
        self.alive = True
    
        """to draw block pass it to parent of constructor"""
        super().__init__(tetromino.tetris.spriteGroup)
        self.image = tetromino.image
        # self.image = pg.Surface([tileSize, tileSize])
        # pg.draw.rect(self.image, 'orange', (1,1, tileSize - 2, tileSize - 1), border_radius =8)
        self.rect = self.image.get_rect()
    
    def isAlive(self):
        if not self.alive:
            self.kill() #removes sprite from groups its contained in

    def rotate(self, pivotPos):
        translated = self.pos - pivotPos
        rotated = translated.rotate(90)
        return rotated + pivotPos
        
    def set_rect_pos(self):
        self.rect.topleft = self.pos * tileSize
    
    def update(self):  
        self.isAlive()
        self.set_rect_pos()

    def collision(self, pos):
        """check if block is in the field. if yes, no collision"""
        x,y = int(pos.x), int(pos.y)
        if 0 <= x <field_w and y < field_h and (y < 0 or not self.tetromino.tetris.fieldArray[y][x]):
            return False
        return True

class Tetromino:
    def __init__(self, tetris):
        self.tetris = tetris
        self.shape = random.choice(list(tetrominoes.keys()))
        self.images = random.choice(tetris.app.images)
        self.blocks = [Block(self, pos) for pos in tetrominoes[self.shape]]
        self.landing = False

    def rotate(self):
        pivotPos = self.blocks[0].pos
        newBlockPositions = [block.rotate(pivotPos) for block in self.blocks]

        if not self.collision(newBlockPositions):
            for i, block in enumerate(self.blocks):
                block.pos = newBlockPositions[i]

    def collision(self, blockPositions):
        """checks if any blocks have collisions"""
        return any(map(Block.collision, self.blocks, blockPositions))

    def move(self, direction):
        moveDirection = moveDirections[direction]
        newBlockPositions = [block.pos + moveDirection for block in self.blocks]
        collision = self.collision(newBlockPositions)

        if not collision:
            for block in self.blocks:
                block.pos += moveDirection
        elif direction == 'down': # if the collision is down (landing)
            self.landing = True

    def update(self):
        self.move(direction='down')