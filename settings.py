import pygame as pg

vec = pg.math.Vector2

spriteDirPath = 'assets\sprites'

fps = 60
fieldColor = (33,33,33)
bkgColor = (73,73,73)

animationTimeInterval = 150 # in milliseconds
fastAnimationTimeInterval = 15 

tileSize = 40
fieldSize = field_w, field_h = 10,20
fieldRes = field_w * tileSize, field_h * tileSize

winRes = win_w, win_h = fieldRes[0] *field_w, fieldRes[1] * field_h

init_pos_offset = vec(field_w // 2 - 1, 0)
next_pos_offset = vec(field_w * 1.4, field_h * 0.4)
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
    'Z': [(0,0), (1,0), (0,-1), (-1,-1)], 
    }