import turtle
import time
import random

posponer = 0.1

score = int()
high_score = int()

wn = turtle.Screen()
wn.title("Proyecto para Conversion y Reparacion de datos")
wn.bgcolor("black")
wn.setup(width = 600, height = 600)
wn.tracer(0)

cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("circle")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"

comida = turtle.Turtle()
comida.speed(0)
comida.shape("square")
comida.color("blue")
comida.penup()
comida.goto(0,100)

veneno = turtle.Turtle()
veneno.speed(0)
veneno.shape("square")
veneno.color("purple")
veneno.penup()
veneno.goto(100,0)

seg=[]

puntaje=turtle.Turtle()
puntaje.speed(0)
puntaje.color("white")
puntaje.penup()
puntaje.hideturtle()
puntaje.goto(0,260)
puntaje.write("score:0     high score: 0", align = "center", font =("Courier", 24, "normal"))


def arriba():
    cabeza.direction = "up"
def abajo():
    cabeza.direction = "down"
def izquierda():
    cabeza.direction = "left"
def derecha():
    cabeza.direction = "right"


def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")


while True:
    wn.update()

    if cabeza.xcor() > 280 or cabeza.xcor() < -290 or cabeza.ycor() > 290 or cabeza.ycor() < -290:
        time.sleep(0.5)
        cabeza.goto(0,0)
        cabeza.direction="stop"
        
        for seg in seg:
            seg.goto(1500,1500)
            
            seg.clear()

            score = 0
            puntaje.clear()
            puntaje.write("Score:{}     High Score:{}".format(score, high_score), 
                align = "center", font =("Courier", 24, "normal"))


    if cabeza.distance(comida) < 20: 
        x=random.randint(-12,12)*20
        y=random.randint(-12,12)*20
        comida.goto(x,y)
        
        x=random.randint(-12,12)*20
        y=random.randint(-12,12)*20
        veneno.goto(x,y)
        
        
        n_seg = turtle.Turtle()
        n_seg.speed(0)
        n_seg.shape("circle")
        n_seg.color("grey")
        n_seg.penup()
        seg.append(n_seg)



        score += 10

        if score > high_score:
            high_score = score
        
        puntaje.clear()
        puntaje.write("Score:{}     High Score:{}".format(score, high_score), 
            align = "center", font =("Courier", 24, "normal"))
    
    if cabeza.distance(veneno) < 20:
        x=random.randint(-12,12)*20
        y=random.randint(-12,12)*20
        veneno.goto(x,y)
        
        x=random.randint(-12,12)*20
        y=random.randint(-12,12)*20
        comida.goto(x,y)
        
        seg.remove(n_seg)

        for seg in seg:
            seg.goto(1500,1500)
        

        score -= 10
        puntaje.clear()
        puntaje.write("Score:{}     High Score:{}".format(score, high_score), 
            align = "center", font =("Courier", 24, "normal"))
        

    ttl_seg = len(seg)
    for i in range(ttl_seg -1, 0, -1):
        x = seg[i - 1].xcor()
        y = seg[i - 1].ycor()
        seg[i].goto(x, y)
    
    if ttl_seg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        seg[0].goto(x, y)

        
    mov()

    for segmento in seg:
        if segmento. distance(cabeza) < 20:
            time. sleep(1)
            cabeza. goto(0,0)
            cabeza. direction = "stop"

            for segmento in seg:
                segmento. goto(1500, 1500)
    
            seg.clear()

            score = 0
            puntaje.clear()
            puntaje.write("Score:{}     High Score:{}".format(score, high_score), 
                align = "center", font =("Courier", 24, "normal"))

    time.sleep(posponer)