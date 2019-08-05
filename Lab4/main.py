# Ismael Carreno
# Lab 4
# July 31, 2019

# Imports the turtle graphics module **
import turtle
 
# creates a turtle (pen) an sets the speed (where 0 is fastest and 10 is slowest)
# The colors can be set through their names or through hexadecimal codes, use hex for accuracy
turtle.screensize(200, 200, bg="#FFFFFF")
myPen = turtle.Turtle()
myPen.color("#800000")
myPen.speed(0)
# If you would like to slow down the animation, uncomment the next line. Higher delay, the slower it will be
#turtle.delay(100)

# setting out box sizes to the n sq pixels per box
normalSize = 14


# myPen.setheading(n) points pen to given angle direction.
# where n queals the angle (think unit circle).
# 0 points to the right, 90 to go up, 180 to go to the left 270 to go down

# Positions myPen in top left area of the screen
# This canvas is currently set to 200*200 pixels or a 20x20 box of 10 sq pixels each
# Places the pen on the top left corner instead of the middle
def goto_origin(myPen):
    myPen.penup()
    myPen.forward(-200)
    myPen.setheading(90)
    myPen.forward(200)
    myPen.setheading(0)
    myPen.pendown()
    # myPen.home()

# This function draws a box by drawing each side of the square and using the fill function
def box(intDim):
    # Can also be done with a for loop - Can you rewrite thise function as such?
    myPen.begin_fill()
    # myPen.forward(90)
    for i in range(4):
        myPen.forward(intDim)
        myPen.left(90)

    myPen.end_fill()  

# Here is an example of how to draw a box using the box function      
# Comment these two lines out when you draw your own images
# box(boxSize)
# turtle.done()


# myPen.color("#000000")
# myPen.speed(10)
def triangle(intLength):
    myPen.begin_fill()
    for i in range(3):
        myPen.forward(intLength)
        myPen.left(120)

    myPen.end_fill()  

def circle(intRadius):
    myPen.begin_fill()
    myPen.circle(intRadius)
    myPen.end_fill()

# triangle(triangleSize)
# turtle.done()


# Challenge functions (2 bonus pts each) 
# def save_image(): # saves the screen to an image/vector file
# You have a function for boxes, can you make functions for circles and triangles?
# def circle(intRadius):
# def triangle(intLength): #This can be an equilateral triangle, or not


# These are the instructions on how to move "myPen" around after drawing a box.
# penup() lifts the pen so it doesn't draw anything and can be moved freely
# pendown() puts the pen down and it draws as it moves, e.g.:
# myPen.penup()
# myPen.forward(boxSize)
# myPen.pendown()
 
# You will save your drawings in text files, which you will read from the art folder.
# You have two sample art pieces already saved. The first line will be a list of colors, and the 
# rest of the lines will be rows of pixels, which you should read and save as a list of lists.
# This first list stores the color values, e.g.:
# #FFFFFF,#FFFF00,#000000,#61380B,#F4FA58
# The drawings are stored using a "list of lists" structure where each value within every list
# element is the index of the color in the pallet list for that pixel

# This function will take in a filename path and load the art piece stored in that file.
# You are to parse the art into two lists, one for the color palette (first line of file),
# and a second with the pixel values (list of lists).
# The function returns both lists
def load_art(path):
    with open(path, "r") as picture:
        picture_split = picture.read().splitlines()
        colorz = picture_split[0]
        color_split = colorz.split(',')
        pixels = picture_split[1:]

    pixel_list = []
    for line in pixels:
        sub_list = line.split(',')
        pixel_list.append(sub_list)
    return color_split, pixel_list

    
    # raise NotImplementedError

# This function takes a pallet and pixel list (matrix) to draw the picture
# You are to write this function
def draw(pallet, pixels):
    turtle.tracer(1000)
    turtle.resetscreen()
    goto_origin(myPen)
    print("================================================================================")
    shape = input("\nWhat shape would you like for your image?\n[1] Box [2] Triangle [3] Circle\nType the #: ")
    print("================================================================================")
    try: 
        shape = int(shape)
    except ValueError:
        exit(1)
    if shape == 1:
        shape = box
    elif shape == 2:
        shape = triangle
    elif shape == 3:
        shape = circle
    else:
        exit(1)

    for line in pixels:
        for pixel in line:
            turtle.tracer(1000)
            int_pixel = int(pixel)
            box_color = pallet[int_pixel]   
            myPen.color(box_color)
            shape(normalSize)
            myPen.forward(normalSize)
        myPen.right(90)
        myPen.forward(normalSize)
        myPen.right(90)
        myPen.forward(normalSize*len(line))
        myPen.right(180)
    
    
	# raise NotImplementedError
# def decision():
#     Yes = True 
#     No = False
#     choice = input("Would you like to be to keep going? [Yes] or [No]\n")        
#     if decision == True:
#         return image
#     elif decision == False:
#         exit(1)


# draw(load_art())
# Should give the user a list of the possible drawing pieces you have and ask which one to draw
# After drawing the piece, ask the if they would like to draw a different piece until they quit the program.
if __name__ == '__main__':
    # sample for loading art and calling draw
    banana = 'art/banana.txt'
    mario = 'art/mario.txt'
    mushroom = 'art/mushroom.txt'
    yoshi = 'art/yoshi.txt'
    pac_ghost = 'art/pac_ghost.txt'
    alien = 'art/alien.txt' 
    smile = 'art/smile.txt'
    spiderman = 'art/spiderman.txt'
    print("================================================================================")
    image = input("What image do you want?\n[1] Mario [2] Banana [3] Mushroom [4] Yoshi [5] Pac-Man Ghost\n[6] Space Invader [7] Smiley [8] Spiderman\nTo quit type ':q'\nType the #: ")
    print("================================================================================")
    if image == ':q':
        exit(1)
    try:
        image = int(image)
    except ValueError:
        exit(1)
    else:
        while image != ':q':
            # image = int(image)
            if image == 1:
                pallet_1, pixels_1 = load_art(mario)
                draw(pallet_1, pixels_1)
                # return decision()
            elif image == 2:
                pallet_1, pixels_1 = load_art(banana)
                draw(pallet_1, pixels_1)
                # return decision()
            elif image == 3:
                pallet_1, pixels_1 = load_art(mushroom)
                draw(pallet_1, pixels_1)
                # return decision()
            elif image == 4:
                pallet_1, pixels_1 = load_art(yoshi)
                draw(pallet_1, pixels_1)
                # return decision()
            elif image == 5:
                pallet_1, pixels_1 = load_art(pac_ghost)
                draw(pallet_1, pixels_1)
            elif image == 6:
                pallet_1, pixels_1 = load_art(alien)
                draw(pallet_1, pixels_1)
            elif image == 7:
                pallet_1, pixels_1 = load_art(smile)
                draw(pallet_1, pixels_1)
            elif image == 8:
                pallet_1, pixels_1 = load_art(spiderman)
                draw(pallet_1, pixels_1)
            else:
                exit(1)
            print("================================================================================")
            image = input("\nWhat other image do you want?\n[1] Mario [2] Banana [3] Mushroom [4] Yoshi [5] Pac-Man Ghost\n[6] Space Invader [7] Smiley [8] Spiderman\nTo quit type ':q'\nType the #: ")
            print("================================================================================")
            try:
                image = int(image)
            except ValueError:
                exit(1)
        
    draw(pallet_1, pixels_1)
    # You need this to prevent the window from closing after drawing
    turtle.done()
    