def setup():
    size(640, 580)

def draw():
    background(100, 100, 100)
    fill(255, 255, 255)
    if mousePressed and mouseX > 100 and mouseX < 300 and mouseY > 50 and mouseY < 200:
        fill(255, 0, 0)
    rect(100, 50, 200, 150)
    
    fill(0, 0, 255)
    textSize(10)
    text(str(mouseX) + ", " + str(mouseY), mouseX, mouseY)
    
def mousePressed():
    print("poop")
