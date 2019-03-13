import arcade
import constants as const
import utils
import math


class Cog:
    """Holds a cog for the cogs game"""

    _y = 0
    _x = 0
    _r = 0

    _y_pix = utils.grid_to_pix(_y)
    _x_pix = utils.grid_to_pix(_x)
    _r_pix = utils.grid_to_pix(_r)
    _color = arcade.color.DARK_BLUE

    def __init__(self, x=0, y=0, r=0, color=arcade.color.DARK_BLUE):
        self._y_pix = utils.grid_to_pix(y)
        self._x_pix = utils.grid_to_pix(x)
        self._r_pix = utils.grid_to_pix(r)

        self.y = y
        self.x = x
        self.r = r
        self._color = color

    def draw(self):
        arcade.draw_circle_outline(self._x_pix, self._y_pix, self._r_pix,
                                   self._color, const.DIST_BETWEEN_DOTS / 20)
        arcade.draw_text(str(self.r),
                         self._x_pix, self._y_pix, arcade.color.BLACK, 14, width=200, align="center",
                         anchor_x="center", anchor_y="center")

    def is_touching(self, o_cog):
        x_dist = (self.x - o_cog.x)
        y_dist = (self.y - o_cog.y)
        dist = math.sqrt(x_dist**2 + y_dist**2)
        r_sum = self.r + o_cog.r + 2

        print(dist-r_sum)
        return (dist - r_sum <= 0) and (dist - r_sum >= -0.18)

    # <editor-fold desc="Getters and setters">
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x_pix = utils.grid_to_pix(x)
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y_pix = utils.grid_to_pix(y)
        self._y = y

    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, r):
        self._r_pix = utils.grid_to_pix(r)
        self._r = r
    # </editor-fold>
