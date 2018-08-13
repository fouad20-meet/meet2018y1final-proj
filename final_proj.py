import turtle
import random
import time

turtle.penup()
turtle.hideturtle()
turtle.speed(4)
turtle.tracer(1,0)

SIZE_X=550
SIZE_Y=550

SQUARE_SIZE = 20

turtle.penup()
turtle.speed(100)
turtle.goto(0,300)
turtle.write("CATCH ME IF YOU CAN" , font=("fantasy",60,"normal"), align="center")
turtle.setup(800, 800)

border = turtle.clone()
border.hideturtle()
border.speed(0)
border.pensize(8)
border.penup()
border.goto(300,300)
border.pendown()
border.goto(300, -300)
border.goto(-300,-300)
border.goto(-300, 300)
border.goto(300,300)

poacher = turtle.Turtle()
poacher.penup()

farmer = turtle.Turtle()
farmer.penup()
farmer.goto(280, 280)

tree = turtle.Turtle()
tree.penup()

cut = turtle.Turtle()
cut.penup()

turtle.register_shape("tree.gif")
turtle.register_shape('poacher.gif')
turtle.register_shape("farmer.gif")
#turtle.register_shape('.gif')

poacher.shape('poacher.gif')
tree.shape('tree.gif')
farmer.shape("farmer.gif")
#cut.shape('.gif')

tree_stamps = []
tree_pos = []

score = 0

UP_EDGE = 300
DOWN_EDGE = -300
RIGHT_EDGE = 300
LEFT_EDGE = -300

direction_poacher = None

TIME_STEP = 120

UP_POACHER = 0
DOWN_POACHER = 1
LEFT_POACHER = 2
RIGHT_POACHER = 3

poacher_pos = None
tree_pos_list = []

def W():
    global direction_poacher
    global UP_POACHER
    global poacher_pos
    direction_poacher = UP_POACHER
    poacher_pos = poacher.pos()
    #move_poacher()
    print("You pressed W")

def S():
    global direction_poacher
    global DOWN_POACHER
    global poacher_pos
    direction_poacher = DOWN_POACHER
    poacher_pos = poacher.pos()
    #move_poacher()
    print("You pressed S")

def A():
    global direction_poacher
    global LEFT_POACHER
    global poacher_pos
    direction_poacher = LEFT_POACHER
    poacher_pos = poacher.pos()
    #move_poacher()
    print("You pressed A")

def D():
    global direction_poacher
    global RIGHT_POACHER
    global poacher_pos
    direction_poacher = RIGHT_POACHER
    poacher_pos = poacher.pos()
    #move_poacher()
    print("You pressed D")

turtle.onkeypress(W , "w")
turtle.onkeypress(S , "s")
turtle.onkeypress(A , "a")
turtle.onkeypress(D , "d")


direction_farmer = None
farmer_pos = None

UP_FARMER = 0
DOWN_FARMER = 1
LEFT_FARMER = 2
RIGHT_FARMER = 3

def UP():
    global direction_farmer
    global UP_FARMER
    global farmer_pos
    direction_farmer = UP_FARMER
    farmer_pos = farmer.pos()
    #move_farmer
    print("You pressed UP")

def DOWN():
    global direction_farmer
    global DOWN_FARMER
    global farmer_pos
    direction_farmer = DOWN_FARMER
    farmer_pos = farmer.pos()
    #move_farmer
    print("You pressed DOWN")

def LEFT():
    global direction_farmer
    global LEFT_FARMER
    global farmer_pos
    direction_farmer = LEFT_FARMER
    farmer_pos = farmer.pos()
    #move_farmer
    print("You pressed LEFT")

def RIGHT():
    global direction_farmer
    global RIGHT_FARMER
    global farmer_pos
    direction_farmer = RIGHT_FARMER
    farmer_pos = farmer.pos()
    #move_farmer
    print("You pressed RIGHT")

turtle.onkeypress(UP , "Up")
turtle.onkeypress(DOWN , "Down")
turtle.onkeypress(LEFT , "Left")
turtle.onkeypress(RIGHT , "Right")

turtle.listen()

def move_poacher():
    my_pos = poacher.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    
    if direction_poacher==RIGHT_POACHER:
        poacher.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    elif direction_poacher==LEFT_POACHER:
        poacher.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
    elif direction_poacher==DOWN_POACHER:
        poacher.goto(x_pos, y_pos - SQUARE_SIZE)
        print("You moved down!")
    elif direction_poacher==UP_POACHER:
         poacher.goto(x_pos, y_pos + SQUARE_SIZE)
         print("You moved up!")

    new_pos = poacher.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    if new_x_pos >= RIGHT_EDGE:
        print("You hit the right edge! Game over!")
        border.penup()
        border.goto(0,0)
        border.pencolor("red")
        border.write("GAME OVER", font = ("arial", 57, "normal"), align = "center")
        time.sleep(5)
        quit()
    elif new_x_pos <= LEFT_EDGE:
        print("You hit the left edge! Game over!")
        border.penup()
        border.goto(0,0)
        border.pencolor("red")
        border.write("GAME OVER", font = ("arial", 57, "normal"), align = "center")
        time.sleep(5)
        quit()
    elif new_y_pos >= UP_EDGE:
        print("You hit the up edge! Game over!")
        border.penup()
        border.goto(0,0)
        border.pencolor("red")
        border.write("GAME OVER", font = ("arial", 57, "normal"), align = "center")
        time.sleep(5)
        quit()
    elif new_y_pos <= DOWN_EDGE:
        print("You hit the down edge! Game over!")
        border.penup()
        border.goto(0,0)
        border.pencolor("red")
        border.write("GAME OVER", font = ("arial", 57, "normal"), align = "center")
        time.sleep(5)
        quit()
    
    global tree_stamps, tree_pos
   
    if poacher.pos() in tree_pos:
        tree_ind=tree_pos.index(poacher.pos()) 
        tree.clearstamp(tree_stamps[tree_ind])               
                                               
        tree_pos.pop(tree_ind) 
        a = tree_stamps.pop(tree_ind)
        tree.clearstamp(a)
        '''
        cut.goto(tree_ind)
        cut.clear()
        '''
        
        print("the poacher has cut the tree")
    
##        score1.penup()
##        score1.goto(-50,-340)
##        global score
##        score += 1
##        score1.clear()
##        score1.write("poacher score:" + str(score), font=("Arial", 20, "normal"))
##    
    if len(tree_stamps) <= 7 :
        make_tree()
    turtle.ontimer(move_poacher,TIME_STEP)

def move_farmer():
    my_pos = farmer.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    
    if direction_farmer==RIGHT_FARMER:
        farmer.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    elif direction_farmer==LEFT_FARMER:
        farmer.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
    elif direction_farmer==DOWN_FARMER:
        farmer.goto(x_pos, y_pos - SQUARE_SIZE)
        print("You moved down!")
    elif direction_farmer==UP_FARMER:
         farmer.goto(x_pos, y_pos + SQUARE_SIZE)
         print("You moved up!")

    new_pos = farmer.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    if new_x_pos >= RIGHT_EDGE:
        print("You hit the right edge! Game over!")
        border.penup()
        border.goto(0,0)
        border.pencolor("red")
        border.write("GAME OVER", font = ("arial", 57, "normal"), align = "center")
        time.sleep(5)
        quit()
    elif new_x_pos <= LEFT_EDGE:
        print("You hit the left edge! Game over!")
        border.penup()
        border.goto(0,0)
        border.pencolor("red")
        border.write("GAME OVER", font = ("arial", 57, "normal"), align = "center")
        time.sleep(5)
        quit()
    elif new_y_pos >= UP_EDGE:
        print("You hit the up edge! Game over!")
        border.penup()
        border.goto(0,0)
        border.pencolor("red")
        border.write("GAME OVER", font = ("arial", 57, "normal"), align = "center")
        time.sleep(5)
        quit()
    elif new_y_pos <= DOWN_EDGE:
        print("You hit the down edge! Game over!")
        border.penup()
        border.goto(0,0)
        border.pencolor("red")
        border.write("GAME OVER", font = ("arial", 57, "normal"), align = "center")
        time.sleep(5)
        quit()

    if farmer.pos() == poacher.pos():
        quit()

    turtle.ontimer(move_farmer,TIME_STEP)

def make_tree():
    min_x=-int(250/2/SQUARE_SIZE)+1
    max_x=int(250/2/SQUARE_SIZE)-1
    min_y=-int(250/2/SQUARE_SIZE)-1
    max_y=int(250/2/SQUARE_SIZE)+1
     
    tree_x = random.randint(min_x,max_x)*SQUARE_SIZE
    tree_y = random.randint(min_y,max_y)*SQUARE_SIZE

    tree.goto(tree_x,tree_y)

    tree_pos.append((tree_x,tree_y))
    tree_stamp = tree.stamp()
    tree_stamps.append(tree_stamp)
    
for this_tree_pos in tree_pos :
    tree.goto(tree_pos[this_tree_pos])
    tree_stamp=tree.stamp()
    tree_stamps.append(tree_stamp)


move_poacher()
move_farmer()

