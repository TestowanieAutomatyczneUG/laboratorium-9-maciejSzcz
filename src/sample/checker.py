from sample.env import Env

class Checker(object):
    def __init__(self):
        self.env = Env()

    def remainder(self, file):
        time = self.env.getTime()

        if time > 17:
            self.env.playWavFile(file)
