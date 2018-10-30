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
    
    #Gravestones
    pushMatrix()
    rotate(PI/100)
    rectMode(CENTER)
    fill(30, 30, 30)
    rect(450, 330, 6, 60)
    rect(450, 320, 25, 5)
    rect(540, 330, 5, 60)
    rect(540, 320, 25, 5)
    rotate(PI/200)
    rect(480, 350, 5, 60)
    rect(480, 340, 25, 5)
    rect(500, 310, 5, 60)
    rect(500, 295, 25, 5)
    popMatrix()
    rect(500, 380, 8, 120)
    rect(500, 350, 40, 10)
    rect(565, 390, 7, 120)
    rect(565, 355, 30, 10)
    
    #House
    rect(200, 345, 150, 110)
    triangle(130, 310, 200, 230, 300, 310)
    rect(200, 250, 50, 100)
    triangle(150, 200, 200, 100, 250, 200)
    rect(165, 250, 20, 20)
    rect(130, 250, 20, 20)
    rect(95, 250, 10, 20)
    rect(130, 270, 80, 30)
    rect(135, 290, 40, 30)
    triangle(225, 130, 235, 100, 245, 130)
    rect(235, 130, 6, 40)
    rect(218, 150, 40, 5)
    
    #Moon
    fill(200, 255, 255, 80)
    ellipse(100, 100, 50, 50)
    
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
