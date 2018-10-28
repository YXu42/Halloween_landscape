def setup():
    global gallo_pic
    size(640, 580)
    gallo_pic = loadImage("https://www.clipartmax.com/png/middle/8-86302_free-to-use-public-domain-zombie-clip-art-zombie-clipart-transparent-background.png")
    imageMode(CENTER)
    
def draw():
    background(87, 82, 100)
    noStroke()
    
    fill(58, 72, 63)
    ellipse(523, 431, 500, 200)
    
    fill(72, 90, 78)
    ellipse(120, 458, 550, 200)
    
    fill(81, 100, 87)
    ellipse(140, 571, 600, 300)
    ellipse(509, 488, 700, 200)
    
    gallo_pic.resize(150, 0)
    image(gallo_pic, 435, 459)
    
    fill(255, 255, 255)
    textSize(10)
    text(str(mouseX) + ", " + str(mouseY), mouseX, mouseY)
