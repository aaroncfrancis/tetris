import pygame as pg

vec = pg.math.Vector2

spriteDirPath = 'assets\sprites'

fps = 60
fieldColor = (33,33,33)

animationTimeInterval = 150 # in milliseconds
fastAnimationTimeInterval = 15 

tileSize = 50
fieldSize = field_w, field_h = 10,20
fieldRes = field_w * tileSize, field_h * tileSize

init_pos_offset = vec(field_w // 2 - 1, 0)
moveDirections = {
    'left': vec(-1,0),
    'right': vec(1,0),
    'down': vec(0,1)
}

tetrominoes = {
    'T': [(0,0), (-1,0), (1,0), (0,-1)],
    'O': [(0,0), (0,-1), (1,0), (1,-1)],
    'J': [(0,0), (-1,0), (0,-1), (0,-2)],
    'L': [(0,0), (-1,0), (0,-1), (0,-2)],
    'I': [(0,0), (0,1), (0,-1), (0,-2)],
    'S': [(0,0), (-1,0), (0,-1), (1,-1)],
    'Z': [(0,0), (1,0), (0,-1), (-1,-1)]
}