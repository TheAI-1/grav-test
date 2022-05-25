import tkinter as tk
import random
import time
level = 0
right = 0
left = 0
gravity_strength = 5
cornerofblock = 40
topoffblock = 100
bottomoffblock = topoffblock + 10
xvelocity = 10
yvelocity = 5
dashcooldown = 0
movecooldown = 0
heldbox = 0
platform_list = []
jpad_list = []
deathpad_list = []
dashpad_list = []
box_list = []
square = None
window = tk.Tk()
window.title("grav test")
window.geometry("850x500")
window.configure(bg="gray")
canvas = tk.Canvas(window, width=600, height=400, bg="lightblue")
canvas.grid(column=1, row=1)
square = canvas.create_rectangle(10, 10, 20, 20, fill="#FFB1F9",tag="player")
endpad = canvas.create_rectangle(580, 110, 590, 120, fill="gold")
def levels(event=None):
    global platform_list, jpad_list, endpad_list, dashpad_list, deathpad_list, box_list
    canvas.delete("level")
    if level == 1:
        platform1 = canvas.create_rectangle(0, topoffblock, cornerofblock, bottomoffblock,
                                            fill="gray",tag="level")
        platform2 = canvas.create_rectangle(100, 150, 60, 160, fill="gray", tag="level")
        platform3 = canvas.create_rectangle(140, 190, 180, 200, fill="gray", tag="level")
        platform4 = canvas.create_rectangle(250, 140, 200, 150, fill="gray", tag="level")
        platform5 = canvas.create_rectangle(260, 130, 250, 140, fill="gray", tag="level")
        platform6 = canvas.create_rectangle(270, 120, 260, 130, fill="gray", tag="level")
        platform7 = canvas.create_rectangle(280, 110, 270, 120, fill="gray", tag="level")
        platform8 = canvas.create_rectangle(310, 100, 280, 110, fill="gray", tag="level")
        platform9 = canvas.create_rectangle(340, 80, 370, 90, fill="gray", tag="level")
        platform10 = canvas.create_rectangle(370, 120, 380, 130, fill="gray", tag="level")
        platform11 = canvas.create_rectangle(430, 130, 420, 140, fill="gray", tag="level")
        platform12 = canvas.create_rectangle(450, 110, 440, 120, fill="gray", tag="level")
        platform13 = canvas.create_rectangle(480, 110, 800, 120, fill="gray", tag="level")

        jpad1 = canvas.create_rectangle(170, 190, 180, 200, fill="lightgreen", tag="level")
        jpad2 = canvas.create_rectangle(310, 100, 300, 110, fill="lightgreen", tag="level")

        platform_list = [platform1, platform2, platform3, platform4, platform5, platform6,
                         platform7, platform8, platform9, platform10, platform11, platform12,
                         platform13]
        dashpad_list = []
        deathpad_list = []
        jpad_list = [jpad1, jpad2]
        box_list = []

    if level == 2:
        platform1 = canvas.create_rectangle(0, topoffblock,cornerofblock,bottomoffblock,fill="gray",tag="level")
        platform2 = canvas.create_rectangle(100, 100, 140, 110, fill="gray", tag="level")
        platform3 = canvas.create_rectangle(250, 290, 280, 300, fill="gray", tag="level")
        platform4 = canvas.create_rectangle(280, 290, 300, 300, fill="gray", tag="level")
        platform5 = canvas.create_rectangle(350, 260, 370, 270, fill="gray", tag="level")
        platform6 = canvas.create_rectangle(410, 230, 450, 240, fill="gray", tag="level")
        platform7 = canvas.create_rectangle(440, 170, 450, 180, fill="gray", tag="level")
        platform8 = canvas.create_rectangle(440, 110, 450, 120, fill="gray", tag="level")
        platform9 = canvas.create_rectangle(530, 110, 590, 120, fill="gray", tag="level")
        
        jpad1 = canvas.create_rectangle(360, 260, 370, 270, fill="lightgreen", tag="level")
        jpad2 = canvas.create_rectangle(440, 110, 450, 120, fill="lightgreen", tag="level")

        deathpad1 = canvas.create_rectangle(260, 290, 290, 300, fill="red", tag="level")
        
        platform_list = [platform1, platform2, platform3, platform4, platform5, platform6, platform7, platform8, platform9]
        dashpad_list = []
        deathpad_list = [deathpad1]
        jpad_list = [jpad1, jpad2]
        box_list = []
    if level == 3:
        platform1 = canvas.create_rectangle(0, topoffblock, cornerofblock, bottomoffblock, fill="gray", tag="level")
        platform2 = canvas.create_rectangle(110, 90, 150, 100, fill="gray", tag="level")
        platform3 = canvas.create_rectangle(200, 90, 260, 100, fill="gray", tag="level")
        platform4 = canvas.create_rectangle(240, 80, 270, 90, fill="gray", tag="level")
        platform5 = canvas.create_rectangle(400, 140, 410, 150, fill="gray", tag="level")
        platform6 = canvas.create_rectangle(360, 140, 420, 150, fill="gray", tag="level")
        platform7 = canvas.create_rectangle(480, 110, 800, 120, fill="gray", tag="level")
        
        dash_pad1 = canvas.create_rectangle(130, 90, 150, 100, fill="blue", tag="level")
        dash_pad2 = canvas.create_rectangle(260, 80, 270, 90, fill="blue", tag="level")
        dash_pad3 = canvas.create_rectangle(400, 120, 410, 130, fill="blue", tag="level")
        
        jpad1 = canvas.create_rectangle(400, 140, 410, 150, fill="lightgreen", tag="level")
        
        platform_list = [platform1, platform2, platform3, platform4, platform5, platform6, platform7]
        dashpad_list = [dash_pad1, dash_pad2, dash_pad3]
        deathpad_list = []
        jpad_list = [jpad1]
        box_list = []
    if level == 4:
        platform1 = canvas.create_rectangle(0, topoffblock, cornerofblock+100, bottomoffblock, fill="gray", tag="level")
        box1 = canvas.create_rectangle(40, 90, 50, 100, fill="#7D4C00",outline="orange",tag="level")
        platform_list = [platform1,box1]
        dashpad_list = []
        deathpad_list = []
        jpad_list = []
        box_list = [box1]
    if level >= 5:
        platform1 = canvas.create_rectangle(0, topoffblock, cornerofblock, bottomoffblock, fill="gray", tag="level")
        
        platform_list = [platform1]
        dashpad_list = []
        deathpad_list = []
        jpad_list = []
        box_list = []
    endpad = canvas.create_rectangle(580, 110, 590, 120, fill="gold")

label_blank = tk.Label(window,  textvariable = "\n   \n ", bg="gray")
label_blank.grid(column=1, row=0)
label = tk.Label(window, text = "press s or w to jump, \ne to dash, \nq to backwards dash, \nd to go forwards \nand a to go back\n\nIf your player is white,\n you cannot dash.\n If your player is pink,\n you can.", bg="gray")
label.grid(column=1, row=2)
sun = canvas.create_rectangle(570, 10, 590, 30, fill="gold")
floor = canvas.create_rectangle(0, 600, 800, 300, fill="cyan", outline="purple")
def do_dashpad(event=None):
    global left, right
    if left == 1:
        for i in range(30, 180, 3):
          canvas.after(i, dashpad_left)
    if right == 1:
        for i in range(30, 180, 6):
          canvas.after(i, dashpad_right)
def grav_change1(event=None):
    global gravity_strength
    gravity_strength = 5
def grav_change2(event=None):
    global gravity_strength
    gravity_strength = 0
def dashpad_right(event=None):
    xvelocity = 1
    canvas.move(square, xvelocity, 0)
def dashpad_left(event=None):
    xvelocity = -1
    canvas.move(square, xvelocity, 0)
def death(event=None):
    canvas.coords(square, 10, 10, 20, 20)
    dashcooldown = 0
def jpad_up(event=None):
    yvelocity = -20
    canvas.move(square, 0, yvelocity, )
def grav(event=None):
    canvas.move(square, 0, yvelocity, )

def end(event=None):
    exit()
def start(event=None):
    global square, yvelocity, square_pos, platform_pos, dashcooldown, level, endpad, movecooldown, right, left, gravity_strength, interacted, heldbox

    if level == 0:
        level = 1
        levels()
    yvelocity = gravity_strength
    square_pos = canvas.coords(square)
    if square == None:
        print("square does not exist - exiting the loop")
        return
    for platform in platform_list:
        platform_pos = canvas.coords(platform)
#        if platform_pos[3] >= platform_pos[1] - 1:
#            yvelocity = 0

        if (square_pos[0] < platform_pos[2] - 1 and square_pos[3] >= platform_pos[1]
            and square_pos[2] > platform_pos[0] and square_pos[3] <= platform_pos[1]):
            yvelocity = 0

        if (square_pos[1] >= platform_pos[1] and square_pos[1] <= platform_pos[1] and
            square_pos[0] < platform_pos[2] - 1 and square_pos[2] > platform_pos[0]):
            canvas.coords(square, square_pos[0], platform_pos[1] - 10, square_pos[2], platform_pos[1])
            yvelocity = 0

    for box in box_list:
        box_pos = canvas.coords(box)
        if (square_pos[0] < box_pos[2] - 1 and square_pos[3] >= box_pos[1]
            and square_pos[2] > box_pos[0] and square_pos[3] <= box_pos[1]):
            if interacted == 1:
                if heldbox == 0:
                    heldbox = 1
                    print(heldbox)
            if interacted == 1:
                if heldbox == 1:
                    heldbox = 0
                    print(heldbox)

    for jpad in jpad_list:
        jpad_pos = canvas.coords(jpad)
        if (square_pos[0] < jpad_pos[2] - 1 and square_pos[3] >= jpad_pos[1]
            and square_pos[2] > jpad_pos[0] and square_pos[3] <= jpad_pos[1]):
            if interacted == 1:
                for i in range(0, 100, 20):
                    canvas.after(i, jpad_up)
    for dashpad in dashpad_list:
        dashpad_pos = canvas.coords(dashpad)
        if (square_pos[0] < dashpad_pos[2] - 1 and square_pos[3] >= dashpad_pos[1]
            and square_pos[2] > dashpad_pos[0] and square_pos[3] <= dashpad_pos[1]):
            do_dashpad()
    for deathpad in deathpad_list:
        deathpad_pos = canvas.coords(deathpad)
        if (square_pos[0] < deathpad_pos[2] - 1 and square_pos[3] >= deathpad_pos[1]
            and square_pos[2] > deathpad_pos[0] and square_pos[3] <= deathpad_pos[1]):
            death()

    #end of level
    end_pos = canvas.coords(endpad)
    if (square_pos[0] < end_pos[2] - 1 and square_pos[3] >= end_pos[1]
            and square_pos[2] > end_pos[0] and square_pos[3] <= end_pos[1]):
        if interacted == 1:
            dashcooldown = 0
            print(level)
            level += 1
            canvas.coords(square, 10, 10, 20, 20)
            print(level)
            canvas.after(0, levels)
    if square_pos[2] <= 0:
        canvas.coords(square, -80, -80, -70, -70)
        #death
    if square_pos[3] >= 350:
        death()
    if square_pos[3] <= 0:
        canvas.coords(square, 10, 10, 20, 20)
    canvas.after(5, func=start)
    dashcooldown -= 1
    movecooldown -= 1
    if dashcooldown >= 1:
        canvas.itemconfig(square, fill='#FFE7FD')
    else:
        canvas.itemconfig(square, fill='#FFB1F9')
    interacted = 0
    grav()

def right(event=None):
    global movecooldown, left, right
    left = 0
    right = 1
    if movecooldown <= 0:
        movecooldown = 2
        for i in range(0, 100, 1):
            canvas.after(i, right_move)
def right_move(event=None):
    canvas.move(square, 0.1, 0)
#    square_pos = canvas.coords(square)
#    for platform in platform_list:
#        platform_pos = canvas.coords(platform)
#        if square_pos[0] == platform_pos[2] - 1 and square_pos[3] >= platform_pos[1]:
#            return

def left(event=None):
    global movecooldown, left, right
    left = 1
    right = 0
    if movecooldown <= 0:
        movecooldown = 2
        for i in range(0, 100, 1):
            canvas.after(i, left_move)
def left_move(event=None):
    canvas.move(square, -0.1, 0)
#def rightspace(event=None):
#    global square,yvelocity,canvas
#    if yvelocity != 0:
#        return
#    yvelocity = 30
#    canvas.move(square,xvelocity,-yvelocity)
#    yvelocity = 5

def jump(event=None):
    if yvelocity != 0:
        return
    for i in range(0, 210, 3):
          canvas.after(i, jump_move)
def jump_move(event=None):
    global square, yvelocity, xvelocity, canvas
    yvelocity = 1
    canvas.move(square, 0, -yvelocity)
#    xvelocity = 30
#    canvas.move(square,xvelocity,0)
#    xvelocity = 10
#    yvelocity = 5

def dash(event=None):
    global dashcooldown
    if dashcooldown <= 0:
        dashcooldown = 20
        for i in range(0, 240, 6):
            canvas.after(i, dash_move)
def dash_move(event=None):
    xvelocity = 1
    canvas.move(square, xvelocity, 0)

def backdash(event=None):
    global dashcooldown
    if dashcooldown <= 0:
        dashcooldown = 20
        for i in range(0, 240, 6):
            canvas.after(i, backdash_move)
def backdash_move(event=None):
    xvelocity = -1
    canvas.move(square, xvelocity, 0)
#def backsuperjump(event=None):
#    global square,yvelocity,xvelocity,canvas
#    if yvelocity != 0:
#        return
#    yvelocity = 50
#    xvelocity = 30
#    canvas.move(square,-xvelocity,-yvelocity)
#    xvelocity = 10
#    yvelocity = 5


#button = tk.Button(window, text = "start", bg="white")
#button.grid(column=1,row=1,)
#button.bind("<Button-1>",start)

#dev cheat, remove when decently done
def dev_cheat(event=None):
    canvas.coords(square, 580, 90, 590, 100)
window.bind("<K>", dev_cheat)

def interact(event=None):
    global interacted
    interacted = 1

def reset(event=None):
    global level, dashcooldown
    dashcooldown = 0
    print(level)
    level = 0
    canvas.coords(square, 10, 10, 20, 20)
    print(level)
    levels()
window.bind("i", reset)

label.grid(column=0, row=1, )
window.bind("<d>", right)
window.bind("<a>", left)
window.bind("<s>", jump)
window.bind("<w>", interact)
window.bind("<space>", jump)
window.bind("<e>", dash)
window.bind("<q>", backdash)
window.bind("<u>", do_dashpad)
window.bind("<g>", grav_change1)
window.bind("<h>", grav_change1)

if __name__=="__main__":
    start()
    #input()



# Added a space after every comma, not necessary, but looks nicer.
# Added "dashpad_list" to global variables, this fixed the bug with dashpads not being checked
# renamed "dashpad" function to "do_dashpad" as it was clashing with "dashpad" object in list call
