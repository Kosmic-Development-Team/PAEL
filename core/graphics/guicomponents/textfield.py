from core.graphics.guicomponents import component
from core import screen
from core.graphics import font
from core.graphics.guicomponents.component import defaultrun


class Textfield(component.Component):
    def __init__(self, pos, text, fontcode, backcols, forecols, inrun=defaultrun):  # font, back cols are 1D arrays/text is just string now : )
        super(self.__class__, self).__init__(pos, (len(backcols), 1))
        self.text = text
        self.prevselec = False
        self.startind = 0
        self.back = backcols[:]
        self.fore = forecols
        self.fontcode = fontcode
        self.inputrun = inrun

    def keyin(self, k):
        if self.selected != self.prevselec:
            self.container.arrownav = not self.selected
        self.prevselec = self.selected
        print('Textfield not actually a textfield yet, please fix')

    def draw(self):
        f = font.fonts[self.fontcode]
        ct = self.text[self.startind:]
        if len(ct) > self.dim[0]:
            ct = ct[:self.dim[0]]
        endind = self.dim[0] - len(self.text)
        if screen.fancy:
            f.drawblend(screen.screen, ct, self.back, self.fore, self.pos)
        else:
            f.draw(screen.screen, ct, self.back, self.fore, self.pos)
        f.drawindent(screen.screen, endind, self.back[self.dim[0] - endind:], (self.pos[0] + self.dim[0] - endind, self.pos[1]))
