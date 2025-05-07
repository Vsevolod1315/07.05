x=0
def setup():
    size(600,600)
def draw():
    global x
    background(255)
    fill(random(0,255))
    ellipse(300,300,170,170)
    textSize(20)
    fill(0)
    text(u"кликни меня",250,300)
    text(x,550,50)
def mouseClicked():
    global x
    xDif = 300 - mouseX
    yDif = 300 - mouseY
    
    if sqrt(xDif*xDif + yDif*yDif) < 85:
        x=x+1
        
