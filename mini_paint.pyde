
def setup():
    size(600,600)
def draw():
    fill(255,176,3)
    rect(120,100,170,70)
    ellipse(400,100,150,150)
    line(mouseX,mouseY, pmouseX, pmouseY)
    textSize(20)
    fill(255)
    text(u"ластик",140,140)
    text(u"цвет",370,100)
def mouseClicked():
    if mouseX >120 and mouseX < 290 and mouseY > 100 and mouseY < 170 :
        background(250)
    xDif = 400 - mouseX
    yDif = 100 - mouseY
    
    if sqrt(xDif*xDif + yDif*yDif) < 75:
        stroke(random(0,255),random(0,255),random(0,255))
    
        
    
    
    
