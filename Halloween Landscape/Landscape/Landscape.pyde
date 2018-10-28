x = 0

def setup():
    global gallo_pic
    size(640, 580)
    gallo_pic = loadImage("https://www.clipartmax.com/png/middle/8-86302_free-to-use-public-domain-zombie-clip-art-zombie-clipart-transparent-background.png")
    imageMode(CENTER)
    
def draw():
    global x
    if x >= 0:
        x -= 10
    background(87, 82, 100)
    noStroke()
    
    #Land at back
    fill(58, 72, 63)
    ellipse(523, 431, 500, 200)
    
    #Land at middle
    fill(72, 90, 78)
    ellipse(120, 458, 550, 200)
    
    #Land in front
    fill(81, 100, 87)
    ellipse(140, 571, 600, 300)
    ellipse(509, 488, 700, 200)
    
    #Test zombie
    gallo_pic.resize(150, 0)
    image(gallo_pic, 435, 459)
    
    #Lightning effect on click
    if mousePressed:
        x = 220
    rectMode(CORNERS)
    fill(255, x)
    rect(0, 0, width, height)
