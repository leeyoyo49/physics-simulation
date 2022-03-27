import math
from vpython import *

size = 1
m = 5
v = 5
L = 50
g = -9.8
dt = 0.0001
k = 1
t = 0
angle = math.asin(4/5) #水平夾角53度

scene = canvas(title="Projectile", width=800, height=600, x=0, y=0, center=vec(0, 0, 0), background=vec(0, 0.6, 0.6))
floor = box(pos=vec(0, -size, 0), size=vec(L, 0.01, 10), texture=textures.metal)
ball = sphere(pos=vec(-L/2, 0, 0), radius=size, texture=textures.wood, make_trail=True, v=vec(9, 12, 0), a=vec(0, g, 0))
ball2 = sphere(pos=vec(-L/2, 0, 0), radius=size, texture=textures.wood, make_trail=True, v=vec(9, 12, 0), a=vec(0, g, 0))

while ( ball2.pos.y > 0 ) or ( ball.pos.x==-L/2 ):
    print(t,"sec passed")
    rate(10000)
    Fk = -1/2 * k * v * v
    if (ball.pos.y>=0):
        ball.a.x = (Fk / m)*math.cos(angle)
        ball.a.y = (Fk / m)*math.sin(angle) + g
        ball.v += ball.a*dt
        ball.pos += ball.v*dt

    ball2.v += ball2.a*dt
    ball2.pos += ball2.v*dt
    t+=dt
print(f"ball1's deltax:{ball.pos.x+L/2} \nball2's deltax:{ball2.pos.x+L/2}")
