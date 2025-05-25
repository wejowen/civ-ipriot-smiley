import time
from smiley import Smiley


class Angry(Smiley):
    def __init__(self):
        super().__init__(complexion=self.RED)
        self.draw_mouth()
        self.draw_eyebrows()
        self.draw_eyes()

    def draw_mouth(self):
        """
       Renders a mouth by blanking the pixels that form that object.
        """
        mouth = [50, 43, 44, 53]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyebrows(self):
        """
       Renders eyebrows by blanking the pixels that form that object.
        """
        eyebrows = [9, 10, 11, 12, 13, 14]
        for pixel in eyebrows:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        """
       Draws the eyes (open or closed) on the standard smiley.
        :param wide_open (bool): eyes open or closed.
        """
        eyes = [18, 21]
        for pixel in eyes:
            self.pixels[pixel] = self.BLANK if wide_open else self.complexion()

    def blink(self, delay=0.25):
        """
        Blinks the Angry smiley's eyes once

        :param delay: Delay between blinks (in seconds)
        """
        self.draw_eyes(wide_open=False)
        self.show()
        time.sleep(delay)
        self.draw_eyes(wide_open=True)
        self.show()

