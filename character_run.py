import math

from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def run_circle():
    cx, cy, r = 400, 300, 200
    for deg in range(0, 360, 5):
        x = cx + r * math.cos(deg / 360 * 2 * math.pi)
        y = cy + r * math.sin(deg / 360 * 2 * math.pi)
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        delay(0.01)

# test_need_time : 길수록 시간이 낭비 되는 것
        
def run_rectangle():
    print('REACTANGLE')
    
    pass

while True:
    run_circle()
    run_rectangle()
    break

close_canvas()