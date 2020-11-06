import pygame
import random
import math
from pygame import mixer
import pkg_resources.py2_warn
pygame.init()

win=pygame.display.set_mode((800,600))
pygame.display.set_caption("circus of plates")
# ___________________________________________________________________________________________________________________________
# control variables
score_value=0
run=True
lost=0
hand_1_full=False
hand_2_full=False
velocity=20
first_level=0
second_level=0
# ___________________________________________________________________________________________________________________________
#icon
icon=pygame.image.load("game icon.png")
pygame.display.set_icon(icon)
# ___________________________________________________________________________________________________________________________
#back ground
background=pygame.image.load("background.png")
if lost==0:
  mixer.music.load("circus background.mp3")
  mixer.music.play(-1)
# ___________________________________________________________________________________________________________________________
#handling the levels
star=pygame.image.load("empty_star.png")
starx=150
stary=15

def draw_star(x,y):
    win.blit(star, (x, y))

crown=pygame.image.load("empty_crown.png")
crownx=200
crowny=15

def draw_crown(x,y):
    win.blit(crown, (x, y))


# ___________________________________________________________________________________________________________________________
# Crown
clown=pygame.image.load("clown.png")
clownx=300
clowny=500
clownvel=15

def clowndraw(x,y):
    win.blit(clown,(x,y))

# ___________________________________________________________________________________________________________________________
# 3 random matching nums
def Random():
    while abs(shapesx[1] - shapesx[0]) < 100:
        shapesx[1] = random.randint(0, 730)

    while abs(shapesx[2] - shapesx[1]) < 100 or abs(shapesx[2] - shapesx[0]) < 100:
        shapesx[2] = random.randint(0, 730)


# ___________________________________________________________________________________________________________________________
# 3 plates of the same color or bomb or garbage
def handle_collosion(j,collosion1,collosion2):
    global score_value
    global lost
    global run
    global shapes

    if shapes[j]==bomb:
        bomb_sound = mixer.Sound("bomb.wav")
        bomb_sound.play()
        pygame.time.delay(1000)
        lost=1
        run=False

    if shapes[j]==garbage:
        garbage_sound = mixer.Sound("garbage_money.wav")
        garbage_sound.play()
        score_value+=1
        garbage_collosion(j)
    else:
        if collosion1:
            on_collosion1(j)
            check_3_plates(const_shapes1,collosion1,collosion2)

        if collosion2:
            on_collosion2(j)
            check_3_plates(const_shapes2,collosion1,collosion2)


def garbage_collosion(j):
    global shapesx
    global shapesy

    shapesy[j] = 900
    shapesx[j] = 900
    # ----------------------
    shapes.remove(shapes[j])
    shapes.append(Allshapes[random.randint(0, 9)])
    # -------------------------------
    shapesx.remove(shapesx[j])
    shapesx.append(900)
    # --------------------------
    shapesy.remove(shapesy[j])
    shapesy.append(900)


def check_3_plates(list,collosion1,collosion2):
    global score_value
    n=len(list)-1
    if n>=2:
        if list[n] == redplate1 or list[n] == redplate2:
            if list[n - 1] == redplate1 or list[n - 1] == redplate2:
                if list[n - 2] == redplate1 or list[n - 2] == redplate2:
                    score_value += 3
                    empty_3_plates(list,collosion1,collosion2)

    n = len(list) - 1
    if n >= 2:
        if list[n] == blueplate1 or list[n] == blueplate2:
            if list[n - 1] == blueplate1 or list[n - 1] == blueplate2:
                if list[n - 2] == blueplate1 or list[n - 2] == blueplate2:
                    score_value += 3
                    empty_3_plates(list,collosion1,collosion2)

    n = len(list) - 1
    if n >= 2:
        if list[n] == yellowplate1 or list[n] == yellowplate2:
            if list[n - 1] == yellowplate1 or list[n - 1] == yellowplate2:
                if list[n - 2] == yellowplate1 or list[n - 2] == yellowplate2:
                    score_value += 3
                    empty_3_plates(list,collosion1,collosion2)

    n = len(list) - 1
    if n >= 2:
        if list[n] == greenplate1 or list[n] == greenplate2:
            if list[n - 1] == greenplate1 or list[n - 1] == greenplate2:
                if list[n - 2] == greenplate1 or list[n - 2] == greenplate2:
                    score_value += 3
                    empty_3_plates(list,collosion1,collosion2)

def empty_3_plates(list,collosion1,collosion2):
    global const_shapesx1
    global const_shapesy1
    global const_shapesx2
    global const_shapesy2

    threePlates = mixer.Sound("39548__the-bizniss__whistle.wav ")
    threePlates.play()

    listx=[]
    listy=[]
    n = len(list) - 1

    if collosion1:
        listx=const_shapesx1
        listy=const_shapesy1

    if collosion2:
        listx = const_shapesx2
        listy = const_shapesy2

    list.remove(list[n])
    list.remove(list[n-1])
    list.remove(list[n-2])

    listx.remove(listx[n])
    listx.remove(listx[n-1])
    listx.remove(listx[n-2])

    listy.remove(listy[n])
    listy.remove(listy[n-1])
    listy.remove(listy[n-2])


# ___________________________________________________________________________________________________________________________
#shapes
#plate1
redplate1=pygame.image.load("red_plate-1.png")
blueplate1=pygame.image.load("blue_plate-1.png")
yellowplate1=pygame.image.load("yellow_plate-1.png")
greenplate1=pygame.image.load("green_plate-1.png")

#plate2
redplate2=pygame.image.load("red_plate-2.png")
blueplate2=pygame.image.load("blue_plate-2.png")
yellowplate2=pygame.image.load("yellow_plate-2.png")
greenplate2=pygame.image.load("green_plate-2.png")

#bomb
bomb=pygame.image.load("bomb.png")

#garbage
garbage=pygame.image.load("garbage.png")

#All shapes
Allshapes=[]
Allshapes.append(redplate1)
Allshapes.append(blueplate1)
Allshapes.append(yellowplate1)
Allshapes.append(greenplate1)
Allshapes.append(redplate2)
Allshapes.append(blueplate2)
Allshapes.append(greenplate2)
Allshapes.append(yellowplate2)
Allshapes.append(bomb)
Allshapes.append(garbage)


#shapes dimention
shapes=[]
shapesx=[]
shapesy=[]
shapesvel=[]
const_shapes1=[]
const_shapesx1=[]
const_shapesy1=[]
const_shapes2=[]
const_shapesx2=[]
const_shapesy2=[]
num_Of_Falling_Shapes=3

for i in range(num_Of_Falling_Shapes):
    shapesx.append(random.randint(0, 730))
    shapesy.append(0)
    shapesvel.append(velocity)
    shapes.append(Allshapes[random.randint(0, 9)])
Random()

def restart_shapes():
    global velocity
    for j in range(num_Of_Falling_Shapes):
        shapesx[j]=random.randint(0, 730)
        shapesy[j] = 0
        shapes[j] = Allshapes[random.randint(0, 9)]
        shapesvel=velocity
    Random()

def shapedraw(x,y,i):
    win.blit(shapes[i],(x,y))



def const_shape_draw1():
    global hand_1_full
    start=0
    for i in range (len(const_shapes1)):
        win.blit(const_shapes1[i], (const_shapesx1[i] + clownx, const_shapesy1[i] - 50 * start))
        if const_shapesy1[i] - 50 * start<0:
            hand_1_full=True
        start+=1


def const_shape_draw2():
    global hand_2_full
    end=0
    for i in range (len(const_shapes2)):
        win.blit(const_shapes2[i], (const_shapesx2[i] + clownx, const_shapesy2[i] - 50 * end))
        if const_shapesy2[i] - 50 * end <0:
            hand_2_full=True
        end+=1


def fully_handed():
    global hand_1_full
    global hand_2_full
    global lost
    global run
    if hand_1_full and hand_2_full:
        fully_hand_sound = mixer.Sound("platesmash.wav")
        fully_hand_sound.play()
        pygame.time.delay(2000)
        lost=1
        run=False
# ___________________________________________________________________________________________________________________________

# distance between two objects
def is_short_dis(x1,y1,x2,y2):
    dis = math.sqrt((math.pow((x1 - x2), 2)) + (math.pow((y1 - y2), 2)))
    return dis < 30
# ___________________________________________________________________________________________________________________________
#on catching an element of shapes
def on_collosion1(j):
    global shapesx
    global shapesy
    global const_shapes1
    global const_shapesx1
    global const_shapesy1

    shapesy[j] = clowny
    shapesx[j] = clownx
    # ----------------------
    const_shapes1.append(shapes[j])
    shapes.remove(shapes[j])
    shapes.append(Allshapes[random.randint(0, 9)])
    # -------------------------------
    const_shapesx1.append(0)
    shapesx.remove(shapesx[j])
    shapesx.append(900)
    # --------------------------
    const_shapesy1.append(shapesy[j])
    shapesy.remove(shapesy[j])
    shapesy.append(900)
    # -----------------------
def on_collosion2(j):
    global shapesx
    global shapesy
    global const_shapes2
    global const_shapesx2
    global const_shapesy2

    shapesy[j] = clowny
    shapesx[j] = clownx
    # ----------------------
    const_shapes2.append(shapes[j])
    shapes.remove(shapes[j])
    shapes.append(Allshapes[random.randint(0, 9)])
    # -------------------------------
    const_shapesx2.append(80)
    shapesx.remove(shapesx[j])
    shapesx.append(900)
    # --------------------------
    const_shapesy2.append(shapesy[j])
    shapesy.remove(shapesy[j])
    shapesy.append(900)
# ___________________________________________________________________________________________________________________________
#font
font=pygame.font.Font('freesansbold.ttf',32)
textx=10
texty=10
# ___________________________________________________________________________________________________________________________
#showing the score on the screen
def showscore(x,y):
    global score_value
    global velocity
    global star
    global crown
    global background
    global first_level
    global second_level
    levelup_sound = mixer.Sound("levelUp.wav")
    score=font.render("score:"+str(score_value),True,(255,255,255))
    win.blit(score,(x,y))

    if score_value>=20 and first_level==0:
        levelup_sound.play()
        first_level=1

    if score_value>=40 and second_level==0:
        levelup_sound.play()
        second_level=1

    if score_value>=20:
        background=pygame.image.load("third_choice.png")
        star=pygame.image.load("yellow_star.png")
        velocity=40

    if score_value>=40:
        background = pygame.image.load("night sky background.png")
        crown=pygame.image.load("orange_crown.png")
        velocity=80
# ___________________________________________________________________________________________________________________________
def pause():
    global font
    paused=True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_c:
                    paused=False

                elif event.key==pygame.K_q:
                    pygame.quit()
                    quit()

        win.fill((255, 255, 255))
        msg1 = font.render("paused", True, (0, 0, 0))
        msg2 = font.render("Press C to continue.... Q to quit", True, (0, 0, 0))
        win.blit(msg1, (300, 100))
        win.blit(msg2, (150, 200))
        pygame.display.update()
        pygame.time.delay(1000)


# ___________________________________________________________________________________________________________________________
while run:
    lost=0
    pygame.time.delay(100)
    win.fill((0, 128, 128))
    win.blit(background, (0, 0))

# ___________________________________________________________________________________________________________________________
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
# ___________________________________________________________________________________________________________________________
    # clown movement
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            clownx -= clownvel
        if event.key == pygame.K_RIGHT:
            clownx += clownvel
        if event.key == pygame.K_SPACE:
             pause()
    if clownx <= 0:
        clownx = 0
    elif clownx >= 716:
        clownx = 716
# ___________________________________________________________________________________________________________________________
    #shapes movement
    for j in range(num_Of_Falling_Shapes):

        if shapesy[j]>700:
            restart_shapes()

        shapesy[j] = shapesy[j] + velocity


        collosion1 = is_short_dis(shapesx[j], shapesy[j], clownx, clowny)
        collosion2 = is_short_dis(shapesx[j], shapesy[j], clownx+80, clowny)

        if collosion1 or collosion2:
            on_collosion_sound  = mixer.Sound("on collosion_correct-choice.wav")
            on_collosion_sound.play()
            handle_collosion(j,collosion1,collosion2)


        shapedraw(shapesx[j], shapesy[j], j)

# ___________________________________________________________________________________________________________________________
    clowndraw(clownx,clowny)
    showscore(textx, texty)
    draw_star(starx,stary)
    draw_crown(crownx,crowny)
    const_shape_draw1()
    const_shape_draw2()
    fully_handed()
    pygame.display.update()
#------------------------------------------------------------------------------------------------------------------------------
if lost==1:
   #pygame.mixer.Sound.set_volume(0)
   pygame.mixer.music.stop()
   win.blit(background, (0, 0))
   msg = font.render("YOU LOST", True, (255, 255, 255))
   win.blit(msg, (300, 200))
   pygame.display.update()
   losesound=mixer.Sound('you-lose-evil.wav')
   losesound.play()
   pygame.time.delay(8000)
pygame.quit()