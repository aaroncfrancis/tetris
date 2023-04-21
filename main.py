from settings import *
from tetris import Tetris
from pygame import mixer
import sys
import pathlib

class App:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Tetris')
        self.screen = pg.display.set_mode(fieldRes)
        self.clock = pg.time.Clock()
        self.setTimer()
        self.images = self.loadImages()
        self.tetris = Tetris(self)
        self.music()
        pg.key.set_repeat()

    def music(self):
        mixer.music.load("tetrisThemeEdited.wav")
        mixer.music.play(-1)        

    def loadImages(self):
        files = [item for item in pathlib.Path(spriteDirPath).rglob('*.png') if item.is_file()]
        images = [pg.image.load(file).convert_alpha() for file in files]
        images = [pg.transform.scale(image, (tileSize, tileSize)) for image in images]
        return images 

    def setTimer(self):
        self.user_event = pg.USEREVENT + 0 
        self.fast_user_event = pg.USEREVENT + 1 
        self.anim_trigger = False
        self.fast_anim_trigger = False
        pg.time.set_timer(self.user_event, animationTimeInterval)
        pg.time.set_timer(self.fast_user_event, fastAnimationTimeInterval)

    def update(self):
        self.tetris.update()
        self.clock.tick(fps)

    def draw(self):
        self.screen.fill(color=fieldColor)
        self.tetris.draw()
        pg.display.flip()

    def checkEvents(self):
        self.anim_trigger = False
        self.fast_anim_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.QUIT()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self.tetris.control(keyPress=event.key)
            elif event.type == self.user_event:
                self.anim_trigger = True
            elif event.type == self.fast_user_event:
                self.fast_anim_trigger = True
    
    def run(self):
        while True:
            self.checkEvents()
            self.update()
            self.draw()

if __name__ == '__main__':
    app = App()
    app.run()
