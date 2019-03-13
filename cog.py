import arcade
import constants as const
import utils


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

    def is_touching(self, o_cog):
        print(abs((self.x - o_cog.x)**2 + (self.y - o_cog.y)**2 - (self.r + o_cog.r + 2)**2))
        return abs((self.x - o_cog.x)**2 + (self.y - o_cog.y)**2 - (self.r + o_cog.r + 2)**2) <= 2**2

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
