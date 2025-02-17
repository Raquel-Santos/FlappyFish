from tupy import *

class Number(Image):
    WIDTH = 50

    def __init__(self, digit, pos, maxpos):
        self._digit = digit
        self._pos = pos
        self._maxpos = maxpos
        self.file = f'../assets/numbers/{digit}.png'
        self.x = 500 + (maxpos*Number.WIDTH)//2 - pos*Number.WIDTH + Number.WIDTH//2
        self.y = 100
    
    @property
    def digit(self):
        return self._digit
    @digit.setter
    def digit(self, value):
        self._digit = value
        self.file = f'../assets/numbers/{value}.png'
    
    @property
    def pos(self):
        return self._pos
    @pos.setter
    def pos(self, value):
        self._pos = value
        self.x = 500 + (self._maxpos*Number.WIDTH)//2 - self._pos*Number.WIDTH + Number.WIDTH//2
    
    @property
    def maxpos(self):
        return self._maxpos
    @maxpos.setter
    def maxpos(self, value):
        self._maxpos = value
        self.pos = self._pos

class Score:
    def __init__(self):
        self._score = 0        
        self._score_list = [Number(0, 1, 1)]
    
    def _increase(self, pos):
        if pos > len(self._score_list):
            self._score_list.append(Number(1, pos, 0))
            for x in self._score_list:
                x.maxpos = len(self._score_list)
        elif self._score_list[pos-1].digit == 9:
            self._score_list[pos-1].digit = 0
            self._increase(pos+1)
        else:
            self._score_list[pos-1].digit += 1

    def increase(self):
        self._increase(1)

    


    
    




