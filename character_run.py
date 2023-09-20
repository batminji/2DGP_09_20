import math

from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def render_all(x, y):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    delay(0.01)

def run_circle():
    cx, cy, r = 400, 300, 200
    for deg in range(0, 360, 5):
        x = cx + r * math.cos(deg / 360 * 2 * math.pi)
        y = cy + r * math.sin(deg / 360 * 2 * math.pi)
        render_all(x,y)

# test_need_time : 길수록 시간이 낭비 되는 것
# 주석처리를 해서 이미 내가 처리한 코드에 대해서 또 테스트할 필요가 없다.

def run_rectangle():
    print('REACTANGLE')
    # while 문보다는 for문이 가독성이 좋고 편하다
    for x in range (50, 750, 10):
        render_all(x, 90)
    for x in range (750, 50, -10):
        render_all(x, 540)

while True:
    # run_circle()
    run_rectangle()
    break

close_canvas()
