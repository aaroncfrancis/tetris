from settings import *
from tetris import Tetris
import sys

class App:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Tetris')
        self.screen = pg.display.set_mode(fieldRes)
        self.clock = pg.time.Clock()
        self.tetris = Tetris(self)

    def update(self):
        self.tetris.update()
        self.clock.tick(fps)

    def draw(self):
        self.screen.fill(color=fieldColor)
        self.tetris.draw()
        pg.display.flip()

    def checkEvents(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.QUIT()
                sys.exit()
    
    def run(self):
        while True:
            self.checkEvents()
            self.update()
            self.draw()

if __name__ == '__main__':
    app = App()
    app.run()
