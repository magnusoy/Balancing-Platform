from vpython import *

scene.title = "Faces example"
scene.width = 600
scene.height = 400

a = vertex(pos=vec(0, 0, 0))
b = vertex(pos=vec(1, 0, 0))
c = vertex(pos=vec(1, 1, 0))

T = triangle(vs=[a, b, c])

while True:
    rate(100)

