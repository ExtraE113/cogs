import arcade
import constants as const


class GridDot:
    """encapsulate grid dots"""

    r_pix = const.DIST_BETWEEN_DOTS / 10  # the radius in pixels
    _held_obj = None

    def __init__(self, x=0, y=0, obj=None):
        self.x_pix = (x + 1) * const.DIST_BETWEEN_DOTS
        self.y_pix = (y + 1) * const.DIST_BETWEEN_DOTS

        self.x = x
        self.y = y
        self.held_obj = obj

    def draw(self):
        arcade.draw_circle_filled(self.x_pix, self.y_pix, self.r_pix,
                                  arcade.color.ASH_GREY)

        if self.held_obj is not None:
            self.held_obj.draw()

    @property
    def held_obj(self):
        return self._held_obj

    @held_obj.setter
    def held_obj(self, held_obj):
        if held_obj is not None:
            held_obj.x = self.x
            held_obj.y = self.y
        self._held_obj = held_obj
