import turtle
speed=[10,20,30,40,50]
colors=["orange","red","green","blue","yellow"]
def draw_star(c,s,size,x,y):
    for i in c:
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        turtle.fillcolor(i)
        turtle.begin_fill()
        c.pop()
        colors.append("cyan")
        for i in range(5):
            turtle.fd(size)
            turtle.right(144)
            turtle.speed(s[i])
        turtle.end_fill()
        turtle.ht()
draw_star(colors,speed,10,0,20)
draw_star(colors,speed,30,15,30)
draw_star(colors,speed,40,50,40)
draw_star(colors,speed,50,100,50)
draw_star(colors,speed,70,160,70)