from system.core.controller import *

class Uwheres(Controller):
    def __init__(self, action):
        super(Uwheres, self).__init__(action)

    def index(self):
        return self.load_view('index.html')
