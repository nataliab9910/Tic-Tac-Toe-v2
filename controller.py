import view
import model


class Controller:

    def __init__(self):
        self.window = view.Window(self)
        self.logic = model.Logic()

    def run(self):
        self.window.run()
