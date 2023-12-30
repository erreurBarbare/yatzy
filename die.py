import random

class Die:
    def __init__(self, name):
        self.name = name
        self.pips =  -1
        self.freeze = False

    def toss(self):
        if not self.freeze:
            self.pips = random.randint(1,6)
