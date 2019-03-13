import griddot
import constants as const
import arcade
import cog
import utils
import copy
import math

""""
cog game main
"""


class Game(arcade.Window):
    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        # self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.BLACK)
        self.dots = [[griddot.GridDot(i, j) for j in range(const.DOTS_Y)] for i in
                     range(const.DOTS_X)]  # fucking black magic

        self.dots[2][3].held_obj = cog.Cog()
        self.mouse = cog.Cog(color=arcade.color.AIR_FORCE_BLUE)

    def on_draw(self):
        """ Use this function to draw everything to the screen. """
        # draw background, processing style. may be a better way to to do this built into arcade, but I couldn't find it
        arcade.draw_rectangle_filled(const.SCREEN_X / 2, const.SCREEN_Y / 2, const.SCREEN_X, const.SCREEN_Y,
                                     arcade.color.BLACK)

        # draw everything by iterating over dots
        for i in self.dots:
            for j in i:
                j.draw()

        # draw obj held by mouse
        if self.mouse is not None:
            self.mouse.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects. Happens approximately 60 times per second."""
        x, y = utils.pix_to_grid(x), utils.pix_to_grid(y)
        self.mouse.x = x
        self.mouse.y = y

        if self.mouse.is_touching(self.dots[2][3].held_obj):
            self.mouse._color = arcade.color.AFRICAN_VIOLET
        else:
            self.mouse._color = arcade.color.AIR_FORCE_BLUE

    def on_mouse_press(self, x, y, button, modifiers):
        x, y = utils.pix_to_grid(x), utils.pix_to_grid(y)
        """
        Called when the user presses a mouse button.
        """
        if button == arcade.MOUSE_BUTTON_LEFT:
            c = copy.copy(self.mouse)
            c._color = arcade.color.DARK_BLUE
            self.dots[x][y].held_obj = c

    def on_mouse_scroll(self, x: int, y: int, scroll_x: int, scroll_y: int):
        self.mouse.r += scroll_y


def main():
    window = Game(const.SCREEN_X, const.SCREEN_Y, const.SCREEN_TITLE)
    # Run the program
    arcade.run()
    # When done running the program, close the window.
    arcade.close_window()


if __name__ == "__main__":
    main()
