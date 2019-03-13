import constants as const


def grid_to_pix(i):
    return (i + 1) * const.DIST_BETWEEN_DOTS


def pix_to_grid(i):  # todo this dosn't work really well, improve it to use %
    return int(i/const.DIST_BETWEEN_DOTS)
