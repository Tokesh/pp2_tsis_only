import pygame,math
#pylint: disable=no-member


pygame.init()
pygame.font.init()
all_fonts = pygame.font.get_fonts()


black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
lime = (0,255,0)
yellow = (255,255,0)
silver = (192,192,192)
purple = (128,0,128)
golden = (255,223,0)
sin_color = (181, 0, 0)
cos_color = (10, 113, 255)


height = 750
width = 800
dlina = 250
chastota = 3
size = (1000,780)
run = True
font = pygame.font.SysFont("arial",30)
font_for_bottom_panel = pygame.font.SysFont("arial",20)
font_for_text_in_square = pygame.font.SysFont("arial",24)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("tsis 9 week")
help_i = 0
help_bot=0
left_points=[" 1.00",' 0.75',' 0.50',' 0.25',' 0.00','-0.25','-0.50','-0.75','-1.00']
bottom_points=["-3п", "-5п", '  -2п', '  -3п', '      -п', '     -п','        0 ','        п','          п', '         3п', '            2п','           5п','     3п']


while run:
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False

    
    #sin line
    my_xy= []
    for x in range(0,800):
        y = int((height/2)+dlina*math.sin(chastota*((float(x)/width)*(2*math.pi))))
        my_xy.append([x+150,y])
    pygame.draw.lines(screen, sin_color, False, my_xy, 5)


    #cos line
    my_xy_cos = []
    for x in range(0,800,2):
        y = int((height/2) + dlina*math.cos(chastota*((float(x)/width)* (2*math.pi))))
        my_xy_cos.append([x+150,y])
    for i in range(0,len(my_xy_cos)-1,3):
        pygame.draw.line(screen, cos_color, (my_xy_cos[i][0],my_xy_cos[i][1]), (my_xy_cos[i+2][0],my_xy_cos[i+2][1]),3)


    #all lines in graph

    #horizontal
    for iq in range(122,689,63):
        pygame.draw.line(screen, black, (115,iq),(990,iq), 2)
    #vertical
    for iq in range(150,950,140):
        if iq ==710: pygame.draw.line(screen, black, (iq,185),(iq,650),2)
        else: pygame.draw.line(screen, black, (iq,100),(iq,650), 2)
    pygame.draw.line(screen, black, (950,100),(950,650),2)


    #left text
    for iq in range(105,665,63):
        screen.blit(font.render(left_points[help_i], True, black),(35,iq)) # text 0
        help_i += 1
    help_i = 0
    #bot text
    for iq in range(135,950, 65):
        screen.blit(font_for_bottom_panel.render(bottom_points[help_bot], True, black),(iq,650)) # text 0
        help_bot += 1
    help_bot = 0


    #left 3 small lines
    for iq in range(122,600,63):
        pygame.draw.line(screen, black, (115,iq+15),(122,iq+15), 1)
        pygame.draw.line(screen, black, (115,iq+30),(130,iq+30), 1)
        pygame.draw.line(screen, black, (115,iq+45),(122,iq+45), 1)
    #right 3 small lines
    for iq in range(122,600,63):
        pygame.draw.line(screen, black, (990,iq+15),(983,iq+15), 1)
        pygame.draw.line(screen, black, (990,iq+30),(975,iq+30), 1)
        pygame.draw.line(screen, black, (990,iq+45),(983,iq+45), 1)


    help_range = 0
    #bottom 3 small lines
    for iq in range(160,935,70):
        if(help_range % 2 == 0): pygame.draw.line(screen, black, (iq+53,650),(iq+53,635), 1)
        pygame.draw.line(screen, black, (iq,650),(iq,643), 1)
        pygame.draw.line(screen, black, (iq+15,650),(iq+15,640), 1)
        pygame.draw.line(screen, black, (iq+30,650),(iq+30,643), 1)
        help_range += 1
    help_range = 0
    
    #top 3 small lines
    for iq in range(160,932,70):
        if(help_range % 2 == 0): pygame.draw.line(screen, black, (iq+53,100),(iq+53,115), 1)
        pygame.draw.line(screen, black, (iq,100),(iq,107), 1)
        pygame.draw.line(screen, black, (iq+15,100),(iq+15,110), 1)
        pygame.draw.line(screen, black, (iq+30,100),(iq+30,107), 1)
        help_range += 1


    #drobi   
    for iq in range(210, 980,140):
        screen.blit(font_for_bottom_panel.render('--', True, black),(iq,659)) # drob
    for iq in range(210, 980,140):
        screen.blit(font_for_bottom_panel.render('2', True, black),(iq,672)) # 2

    #x in the bottom
    screen.blit(font_for_bottom_panel.render('X', True, black),(565,690))


    #text in graph, with lines
    screen.blit(font_for_text_in_square.render('sin x', True, black),(660,120)) # sin x
    screen.blit(font_for_text_in_square.render('cos x', True, black),(660,145)) # cos x
    pygame.draw.line(screen, sin_color, (710,135),(750,135),3)
    pygame.draw.line(screen, cos_color, (710,160),(720,160),3)
    pygame.draw.line(screen, cos_color, (725,160),(735,160),3)
    pygame.draw.line(screen, cos_color, (740,160),(750,160),3)
    pygame.draw.rect(screen,black, (115,100,875,550), 4)



    pygame.display.flip()
pygame.quit()