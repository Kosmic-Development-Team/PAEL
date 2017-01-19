from core.graphics.guicomponents import component
import core
from core.graphics import font
from core import screen


class Label(component.Component):
    def __init__(self, pos, text, fontcode, backcols, forecols):
        super(self.__class__, self).__init__(pos, (len(backcols[0]), len(backcols)))
        self.text = text[:]
        self.back = backcols
        self.fore = forecols
        self.indents = core.guimanager.indexfromtext(self.text, self.dim)
        self.fontcode = fontcode

    def changetext(self, ntxt):
        self.text = ntxt[:]
        self.indents = core.guimanager.indexfromtext(self.text, self.dim)

    def draw(self):
        f = font.fonts[self.fontcode]
        for i in range(len(self.text)):
            f.drawindent(screen.screen, self.indents[0][i], self.back[i],
                         (self.pos[0], self.pos[1] + i))
            if screen.fancy:
                f.drawblend(screen.screen, self.text[i], self.back[i][self.indents[0][i]:], self.fore[i],
                            (self.pos[0] + self.indents[0][i], self.pos[1] + i))
            else:
                f.draw(screen.screen, self.text[i], self.back[i][self.indents[0][i]:], self.fore[i],
                       (self.pos[0] + self.indents[0][i], self.pos[1] + i))
            fo = self.indents[0][i] + len(self.text[i])
            f.drawindent(screen.screen, self.indents[1][i], self.back[i][fo:], (self.pos[0] + fo, self.pos[1] + i))
