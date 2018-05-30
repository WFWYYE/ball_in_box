import math
import random
from .validate import validate

__all__ = ['ball_in_box']


def ball_in_box(m=5, blockers=[(0.5, 0.5), (0.5, -0.5), (0.5, 0.3)]):
    """
    m is the number circles.
    n is the list of coordinates of tiny blocks.
    
    This returns a list of tuple, composed of x,y of the circle and r of the circle.
    """

    # The following is an example implementation.

    return find_radius(blockers, m)


def find_radius(blockers, m):
    circles = []
    circle_index = 0
    inc = 1e-2
    # 圆环的信息

    for i in range(m):

        tmp_y = -1 + inc
        x = tmp_y
        y = tmp_y
        r = inc

        while tmp_y + r <= 1:
            tmp_x = -1 + inc
            while tmp_x + r <= 1:

                max_radius = 1 - abs(tmp_y)
                mid_radius = (max_radius + r) / 2

                # 二分法求最大的圆环半径
                while max_radius - r > 1e-3:
                    if tmp_y > 0.5 and tmp_x > 0.5:
                        a = 0
                    circles.append((tmp_x, tmp_y, mid_radius))
                    if validate(circles, blockers):
                        x = tmp_x
                        y = tmp_y
                        r = mid_radius
                    else:
                        max_radius = mid_radius
                    mid_radius = (max_radius + r) / 2
                    circles.pop()

                tmp_x += inc
            tmp_y += inc

        circles.append((x, y, r))
        #print(x, y, r)
        circle_index += 1

    return circles

def min_radius(x,y,circles,blockers):
    pass
