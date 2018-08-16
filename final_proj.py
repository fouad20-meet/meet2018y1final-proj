import turtle
import random
import time

turtle.bgpic("background.gif")

turtle.penup()
turtle.hideturtle()
turtle.tracer(1,0)

SIZE_X=550
SIZE_Y=550

SQUARE_SIZE = 20
catch = turtle.clone()
catch.penup()
catch.speed(0)
catch.goto(0,300)
catch.write("CATCH ME IF YOU CAN" , font=("fantasy",60,"normal"), align="center")

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

points = 0

score = 0
score_points = turtle.clone()
score_points.hideturtle()
score_points.penup()
score_points.goto(-300,-350)
score_points.write(score , font = ("fantasy", 24, "normal"))

poacher = turtle.Turtle()
poacher.penup()

farmer = turtle.Turtle()
farmer.penup()
farmer.goto(280, 280)

tree = turtle.Turtle()
tree.penup()

cut = turtle.Turtle()
cut.hideturtle()
cut.penup()

cow = turtle.Turtle()
cow.hideturtle()
cow.penup()

turtle.register_shape("tree.gif")
turtle.register_shape('poacher.gif')
turtle.register_shape("farmer.gif")
turtle.register_shape('cut.gif')
turtle.register_shape("cow.gif")

poacher.shape('poacher.gif')
tree.shape('tree.gif')
farmer.shape("farmer.gif")
cut.shape('cut.gif')
cow.shape("cow.gif")

tree_stamps = []
tree_pos = []
trees = []

cut_stamps = []

clear_stamps = []
time_stamps = []

cow_pos = []
cow_stamps = [] 

UP_EDGE = 300
DOWN_EDGE = -300
RIGHT_EDGE = 300
LEFT_EDGE = -300

TIME_STEP_POACHER = 120
TIME_STEP_FARMER = 180

UP_POACHER = 0
DOWN_POACHER = 1
LEFT_POACHER = 2
RIGHT_POACHER = 3

direction_poacher = UP_POACHER
poacher_pos = None

def make_tree():
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)-1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)+1
     
    tree_x = random.randint(min_x,max_x)*SQUARE_SIZE
    tree_y = random.randint(min_y,max_y)*SQUARE_SIZE

    tree.goto(tree_x,tree_y)

    tree_pos.append((tree_x,tree_y))
    tree_stamp = tree.stamp()
    tree_stamps.append(tree_stamp)
    trees.append(tree)
    
for this_tree_pos in tree_pos :
    tree.goto(tree_pos[this_tree_pos])
    tree_stamp=tree.stamp()
    tree_stamps.append(tree_stamp)

def make_cow():
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)-1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)+1
     
    cow_x = random.randint(min_x,max_x)*SQUARE_SIZE
    cow_y = random.randint(min_y,max_y)*SQUARE_SIZE

    cow.goto(cow_x,cow_y)

    cow_pos.append((cow_x,cow_y))
    cow_stamp = cow.stamp()
    cow_stamps.append(cow_stamp)
    cow_pos.append(cow.pos())
    
for this_cow_pos in cow_pos :
    cow.goto(cow_pos[this_cow_pos])
    cow_stamp=cow.stamp()
    cow_stamps.append(cow_stamp)

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



farmer_pos = None

UP_FARMER = 0
DOWN_FARMER = 1
LEFT_FARMER = 2
RIGHT_FARMER = 3

direction_farmer = DOWN_FARMER

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
        print("You teleported!")
        poacher.hideturtle()
        poacher.goto(new_x_pos-600,new_y_pos)
        poacher.showturtle()
        
    elif new_x_pos <= LEFT_EDGE:
        print("You teleported!")
        poacher.hideturtle()
        poacher.goto(new_x_pos+600,new_y_pos)
        poacher.showturtle()
    elif new_y_pos >= UP_EDGE:
        print("You teleported!")
        poacher.hideturtle()
        poacher.goto(new_x_pos,new_y_pos - 600)
        poacher.showturtle()
    elif new_y_pos <= DOWN_EDGE:
        print("You teleported!")
        poacher.hideturtle()
        poacher.goto(new_x_pos,new_y_pos+600)
        poacher.showturtle()
    
    global tree_stamps, tree_pos, cow_pos
    global score
    if poacher.pos() in tree_pos:
        tree_ind=tree_pos.index(poacher.pos()) 
        tree.clearstamp(tree_stamps[tree_ind])

        cut.goto(poacher.pos())
        cut_stamp = cut.stamp()
        clear_stamps.append(cut_stamp)

        t = time.time()
        time_stamps.append(t)
        
        tree_pos.pop(tree_ind) 
        a = tree_stamps.pop(tree_ind)
        tree.clearstamp(a)
        score += 1
        score_points.clear()
        score_points.write(score , font = ("fantasy", 24, "normal"))
        if score == 20:
            score_points.pencolor("red")
            score_points.goto(0,0)
            score_points.write("THE POACHER WON" , font = ("fantasy", 57, "normal"), align = "center")
            time.sleep(3)
            quit()
        print("The poacher has cut the tree")
        
    if poacher.pos() in cow_pos:
        score_points.pencolor("red")
        score_points.goto(0,0)
        score_points.write("THE POACHER HIT THE COW" , font = ("fantasy", 40, "normal"), align = "center")
        time.sleep(3)
        quit()

    if len(time_stamps) > 0:
        if time_stamps[0] - time.time() < -3:
            time_stamps.pop(0)
            cut_stamp = clear_stamps.pop(0)
            cut.clearstamp(cut_stamp)
             
    if len(tree_stamps) <= 5 :
        make_tree()
        
    if len(cow_stamps) <= 2 :
        make_cow()
        
    turtle.ontimer(move_poacher,TIME_STEP_POACHER)

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
    print(new_pos)
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    if new_x_pos >= RIGHT_EDGE:
        print("You hit the right edge! Game over!")
        border.penup()
        border.goto(0,0)
        border.pencolor("red")
        border.write("THE FARMER HIT THE EDGE", font = ("arial", 33, "normal"), align = "center")
        time.sleep(5)
        quit()
    elif new_x_pos <= LEFT_EDGE:
        print("You hit the left edge! Game over!")
        border.penup()
        border.goto(0,0)
        border.pencolor("red")
        border.write("THE FARMER HIT THE EDGE", font = ("arial", 35, "normal"), align = "center")
        time.sleep(5)
        quit()
    elif new_y_pos >= UP_EDGE:
        print("You hit the up edge! Game over!")
        border.penup()
        border.goto(0,0)
        border.pencolor("red")
        border.write("THE FARMER HIT THE EDGE", font = ("arial", 35, "normal"), align = "center")
        time.sleep(5)
        quit()
    elif new_y_pos <= DOWN_EDGE:
        print("You hit the down edge! Game over!")
        border.penup()
        border.goto(0,0)
        border.pencolor("red")
        border.write("THE FARMER HIT THE EDGE", font = ("arial", 35, "normal"), align = "center")
        time.sleep(5)
        quit()
    if abs(farmer.pos()[0] - poacher.pos()[0]) < 25 and abs(farmer.pos()[1] - poacher.pos()[1]) < 25:
        score_points.pencolor("red")
        score_points.goto(0,0)
        score_points.write("THE FARMER WON" , font = ("fantasy", 35, "normal"), align = "center")
        time.sleep(3)
        quit()
    global TIME_STEP_FARMER
    global score
    global points
    if score == points + 5:
        TIME_STEP_FARMER = TIME_STEP_FARMER - 20
        points = points + 5
        
        
            
    turtle.ontimer(move_farmer,TIME_STEP_FARMER)


move_poacher()
move_farmer()

