from random import *
from turtle import *
from freegames import path
import turtle
from tkinter import PhotoImage

images = ["rayo1.gif", "sol.gif", "abeja.gif", "americano.gif", "arbol.gif", "basket.gif", "balonfutbol.gif", "calabaza.gif",
          "cerdo.gif", "estrella.gif", "luna.gif", "m.gif", "manzana.gif", "pera.gif", "planta.gif", "sombrero.gif", "pay.gif",
          "mano.gif", "reloj.gif"]
smaller = []
for i in range(len(images)):
    turtle.register_shape(images[i])
    smaller.append(PhotoImage(file=images[i]).subsample(8, 8))
    addshape(("%d" % i), Shape("image", smaller[i]))
    

car = path('car.gif')
tiles = list(range(18)) * 2
state = {'mark': None}
hide = [True] * 36
veces = 0
abiertas = 0


def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 150) // 50 + ((y + 150) // 50) * 6)


def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 6) * 50 - 150, (count // 6) * 50 - 150


def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        global abiertas
        abiertas += 2
        print(abiertas)
        if abiertas == len(tiles):
            print("Has ganado")
            goto(240, 100)
            write("Has ganado", font=('Arial', 15, 'normal'))
    global veces
    veces = veces + 1


def draw():  # dibuja los numeros y la imagen
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(36):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 26, y + 9)
        s = Turtle(str(int(tiles[mark])))
        s.setposition(x+26,y+25)
        #write(tiles[mark], font=('Arial', 25, 'normal'), align="center")
    goto(240, 130)
    write(veces, font=('Arial', 25, 'normal'))

    update()
    ontimer(draw, 100)

            

shuffle(tiles)
setup(600, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()