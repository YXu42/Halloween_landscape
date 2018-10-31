width = 720
height = 540
import random
x_one = random.randint(10, width - 10)
y_one = random.randint(10, height - 10)
x_two = random.randint(10, width - 10)
y_two = random.randint(10, height - 10)
x_three = random.randint(10, width - 10)
y_three = random.randint(10, height - 10)

def setup():
    global img
    size(720, 540)
    img = loadImage("background.JPG")

  
def draw():
    global img, x_one, y_one, x_two, y_two, x_three, y_three
    background(0)
    image(img, 0, 0)
    
    #Ghost one
    noStroke()
    fill(220)
    arc(x_one, y_one, 90, 200, -PI, 0)
    arc(x_one - 30, y_one, 30, 40, radians(0), radians(180))
    arc(x_one, y_one, 30, 40, radians(0), radians(180))
    arc(x_one + 30, y_one, 30, 40, radians(0), radians(180))
    fill(0)
    ellipse(x_one - 15, y_one - 70, 10, 20)
    ellipse(x_one + 15, y_one - 70, 10, 20)
    #Ghost coming down
    if y_one < 720:
        y_one += 10
    else:
        y_one = 0
        x_one = random.randint(10, width - 10)

    #Ghost two
    noStroke()
    fill(220)
    arc(x_two + 100, y_two + 100, 90, 200, -PI, 0)
    arc(x_two + 70, y_two + 100, 30, 40, radians(0), radians(180))
    arc(x_two + 100, y_two + 100, 30, 40, radians(0), radians(180))
    arc(x_two + 130, y_two + 100, 30, 40, radians(0), radians(180))
    fill(0)
    ellipse(x_two + 85, y_two + 30, 10, 20)
    ellipse(x_two + 115, y_two + 30, 10, 20)
    #Ghost coming down
    if y_two < 720:
        y_two += 10
    else:
        y_two = 0
        x_two = random.randint(10, width - 10)
        
    #Ghost three
    noStroke()
    fill(220)
    arc(x_three + 100, y_three + 100, 90, 200, -PI, 0)
    arc(x_three + 70, y_three + 100, 30, 40, radians(0), radians(180))
    arc(x_three + 100, y_three + 100, 30, 40, radians(0), radians(180))
    arc(x_three + 130, y_three + 100, 30, 40, radians(0), radians(180))
    fill(0)
    ellipse(x_three + 85, y_three + 30, 10, 20)
    ellipse(x_three + 115, y_three + 30, 10, 20)
    #Ghost coming down
    if y_three < 720:
        y_three += 10
    else:
        y_three = 0
        x_three = random.randint(10, width - 10)

    #PERSON
    fill(255)
    rect(mouseX, mouseY, 50, 50)
    
    #SCORE
    fill(255)
    rect(10, 10, 100, 50)
    textAlign(CENTER, CENTER)
    fill(0)
    textSize(25)
    text("Score:", 50, 25)
    textSize(15)
    text(second() + (minute()*60), 45, 45)

    if (mouseX > x_one - 50 and mouseX < x_one + 50 and mouseY > y_one - 150 and mouseY < y_one + 20) or (mouseX > x_two and mouseX < x_two + 100 and mouseY > y_two - 50 and mouseY < y_two + 100) or (mouseX > x_three and mouseX < x_three + 150 and mouseY > y_three - 50 and mouseY < y_three + 100):
        textAlign(CENTER, CENTER)
        background(0)
        fill(255)
        textSize(150)
        text('YOU LOSE', width/2, height/2)
