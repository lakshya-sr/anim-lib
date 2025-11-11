import animation
from animation import Circle, Animation, Rect, Image
from functions import *
import easings
import time
from math import *


def rotate_shift_point(point, angle, offset):
    x, y = point
    x_rot = x * cos(angle) - y * sin(angle)
    y_rot = x * sin(angle) + y * cos(angle)
    return (offset[0] + x_rot, offset[1] + y_rot)	

animation.init((800, 600))

anim = Animation()

center = (400,300)
start = (400,600)
body = Circle(start, 0, 1, 20, "white", True)
trails = [Circle(start, 0, 1, 5, "red", True) for i in range(20)]

for i, trail in enumerate(trails):
	anim.add(trail, goto_pos(trail, center, easings.linear), start_time=0, duration=3)
	anim.add(trail, goto_pos(trail, rotate_shift_point((500,0),i/len(trails)*2*pi, center), easings.out_cubic), start_time=3, duration=5)

anim.add(body, goto_pos(body, center, easings.linear), start_time=0, duration=3)
anim.add(body, scale(body, 3, easings.inout_quad), start_time=3, duration=3)

animation.run(anim)
