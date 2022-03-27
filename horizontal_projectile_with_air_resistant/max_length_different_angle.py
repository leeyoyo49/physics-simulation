import math
from vpython import *

size = 1
m = 0.0012
v = 13.9
L = 10
g = -9.8
dt = 0.0001
k = 0.00077
t = 0
max_length = 0

scene = canvas(title="Projectile", width=800, height=600, x=0, y=0, center=vec(0, 0, 0), background=vec(0, 0.6, 0.6))
floor = box(pos=vec(0, -size, 0), size=vec(L, 0.01, 10), texture=textures.metal)

for x in range(90):
    angle = x*(math.pi/180)
    ball = sphere(pos=vec(-L/2, 0, 0), radius=size, texture=textures.wood, make_trail=True, v=vec(math.cos(angle)*v, math.sin(angle)*v, 0), a=vec(0, g, 0))
    
    while ( ball.pos.y > 0 ) or ( ball.pos.x==-L/2 ):
        rate(10000)
        Fk = -1/2 * k * (ball.v.x*ball.v.x+ball.v.y*ball.v.y)
        if (ball.pos.y>=0):
            ball.a.x = (Fk / m)*math.cos(angle)
            ball.a.y = (Fk / m)*math.sin(angle) + g
            ball.v += ball.a*dt
            ball.pos += ball.v*dt

    length = ball.pos.x+L/2

    if length > max_length :
        max_length = length
        biggest_angle = angle

        print(max_length)
        if x == 0:
            big = ball
            continue
        big.visible = False
        big.clear_trail()
        del big
        big = ball
    elif length < max_length :
        ball.visible = False
        ball.clear_trail()
        del ball
        break

print(f"ball's max displacement:{max_length} \nand the angle is {biggest_angle*180/math.pi}" )
