#Hirad Showghi Sarkhosh
#101272774

import pygame

#Making the background
win_sz = (500,600)
win_sfc = pygame.display.set_mode(win_sz)
background = pygame.color.Color(white)
win_sfc.fill(background)

#Defining colours used
white = (255,255,255)
yellow = (255,255,84)
black = (0,0,0)
red = (195,53,49)
grey = (86,80,77)
l_green = (144,238,144)
green = (82,166,58)  

#Determining the size of the mouth
x = int(input("Enter how wide you want the mouth to be:"))
y = int(input("Enter how long you want the mouth to be:"))

#Drawing Eyes
def draw_eyes():
    #Outline for the eyes
    pygame.draw.circle(win_sfc, (black), (125,202), 26) 
    pygame.draw.circle(win_sfc, (black), (175,202), 26)
    #Eyes themselves
    pygame.draw.circle(win_sfc, (white), (125,200), 24) 
    pygame.draw.circle(win_sfc, (white), (175,200), 24)
    #Outer pupil
    pygame.draw.circle(win_sfc, (green), (135,200), 10)  
    pygame.draw.circle(win_sfc, (green), (165,200), 10)
    #Inner pupil
    pygame.draw.circle(win_sfc, (l_green), (135,200), 5)
    pygame.draw.circle(win_sfc, (l_green), (165,200), 5)
    #Shine on the pupils
    pygame.draw.circle(win_sfc, (white), (133,204), 2)
    pygame.draw.circle(win_sfc, (white), (163,204), 2)
    #Rectangle that cuts the eyes into half
    pygame.draw.rect(win_sfc, (yellow), [98,175,104,25])
    #Top outline of the eyes
    pygame.draw.line(win_sfc, (black), (100,198), (200,198), 2) 
    #Eyebrows
    pygame.draw.polygon(win_sfc, (black), [(112,191), (119,181), (132,178), (136,186), (119,187)])
    pygame.draw.polygon(win_sfc, (black), [(163,196), (163,187), (175,186), (188,193), (173,192)])
    pygame.display.update()

#Drawing the Christmas Hat 
def draw_hat():
    #Outline of top part of hat
    pygame.draw.circle(win_sfc, (black), (250,275), 65)
    #Top part of the hat
    pygame.draw.circle(win_sfc, (green), (250,275), 62)
    #Outline of bottom part of hat
    pygame.draw.ellipse(win_sfc, (black), [182,249,136,40])
    #Bottom part of hat
    pygame.draw.ellipse(win_sfc, (red), [185,252,130,35])
    #Rectangle to clean hat edges
    pygame.draw.rect(win_sfc, (yellow), [185,275,130,65])
    #Bottom outline of the bottom part of hat
    pygame.draw.line(win_sfc, (black), (185,275), (314,275), 2)
    #Outline of ball
    pygame.draw.circle(win_sfc, (black), (250,205), 18)
    #Ball
    pygame.draw.circle(win_sfc, (white), (250,205), 15)
    pygame.display.update()
    return "Christmas Hat"

#Drawing the Mouth   
def draw_mouth(x,y):
    #Outline of the mouth
    pygame.draw.circle(win_sfc, (black), (x,y+50), 42)
    #Mouth
    pygame.draw.circle(win_sfc, (red), (x,y+50), 40)
    #Bottom outline of the teeth 
    pygame.draw.circle(win_sfc, (black), (x,y+25), 47)
    #teeth
    pygame.draw.circle(win_sfc, (white), (x,y+25), 45)
    #Top outline of teeth
    pygame.draw.circle(win_sfc, (black), (x,y+5), 57)
    #Circle that covers the rest of the teeth outline circle
    pygame.draw.circle(win_sfc, (white), (x,y+5), 55)
    #Rectangle that covers the protruding circles
    pygame.draw.rect(win_sfc, (yellow), [x-58,y-52,116,96])
    #Left cheek dimple
    pygame.draw.line(win_sfc, (black), (x-52,y+48), (x-32,y+35), 2)
    #Right cheek dimple
    pygame.draw.line(win_sfc, (black), (x+52,y+48), (x+32,y+35), 2)
    pygame.display.update()
