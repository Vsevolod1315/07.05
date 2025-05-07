def setup():
    size(600,600)
def draw():
    rect(300,300,100,50)
    background(random(0,255),random(0,255),random(0,255))
    if mousePressed :
        rect(mouseX,mouseY,100,50)
    
