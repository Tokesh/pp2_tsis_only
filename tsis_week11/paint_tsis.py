import pygame
#pylint: disable=no-member
pygame.init()
pygame.font.init()
"""
v 1. Draw rectangle
v 2. Draw circle
v 3. Eraser
v 4. Color selection
v 5. Saving painted picture to file 
"""

def Draw_Without_Intervals(screen, start, end, width, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for x in range(x1, x2):
            y = (-C - A * x) / B
            pygame.draw.circle(screen, color, (x, y), width)
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1, y2):
            x = (-C - B * y) / A
            pygame.draw.circle(screen, color, (x, y), width)


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


application = True
font = pygame.font.SysFont("arial", 25)
size = (1100,800)
radius = 10
mode = 0
color = white
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Paint")
clock = pygame.time.Clock()
run = True
settings=True
FPS = 30
draw_status = False
last_pos = (0, 0)
screen.fill(white)
hide_radius = True
tools_image = pygame.image.load('colors.png')
tools = pygame.image.load('tools_v2.png')
#mode = 0 - classic, 1 - circle, 2 rectangle
x1_rect = 0
y1_rect = 0
x2_rect = 0
y2_rect = 0


while application:
    """ while settings:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: application = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                run = True
                screen.fill(white)
                settings = False
        screen.blit(font.render('To choose color press:Golden(T), Red(R), Green(G)', True, black), (50,50))
        screen.blit(font.render('Draw rectangle(O), Draw circle(C), Back to classic(CAPS_LOCK), Eraser(E), Screenshot(ESC)', True, black),(50,100))
        pygame.display.flip() """
    while run:
        screen.blit(tools_image,(0,0))
        screen.blit(tools, (352,0))
        if hide_radius: screen.blit(font.render(f"current radius: {radius}", True, black),(20,65))
        for event in pygame.event.get():
            if event.type == pygame.QUIT: application = False
            if event.type == pygame.KEYDOWN:
                if(event.key == pygame.K_ESCAPE): pygame.image.save(screen, 'screenshot.jpeg')
                if(event.key == pygame.K_r): color = red
                if(event.key == pygame.K_g): color = green
                if(event.key == pygame.K_t): color = golden
                if(event.key == pygame.K_UP): radius += 1
                if(event.key == pygame.K_DOWN): radius -= 1
                if(event.key == pygame.K_e): color = white
                if(event.key == pygame.K_h): hide_radius = not hide_radius
                if(event.key== pygame.K_CAPSLOCK): mode = 0
                if(event.key == pygame.K_c): mode = 1
                if(event.key == pygame.K_o): mode = 2
            if event.type == pygame.MOUSEBUTTONDOWN:
                xxx,yyy = event.pos # 65:60
                if(xxx in range(0,65) and yyy in range(0,60)): color = golden
                if(xxx in range(66, 139) and yyy in range(0,60)): color = red
                if(xxx in range(141, 208) and yyy in range(0,60)): color = green
                if(xxx in range(210,278) and yyy in range(0,60)): color = purple
                if(xxx in range(280,347) and yyy in range(0,60)): color = silver
                if(xxx in range(353,417) and yyy in range(0,60)): mode = 1
                if(xxx in range(424,492) and yyy in range(0,60)): mode = 2
                if(xxx in range(497,561) and yyy in range(0,60)): 
                    mode = 0
                    color = white
                if(xxx in range(562,629) and yyy in range(0,60)): radius += 5
                if(xxx in range(633,700) and yyy in range(0,60)): radius -= 5
            if(mode == 0):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.circle(screen, color, event.pos, radius)
                    draw_status = True
                if event.type == pygame.MOUSEBUTTONUP:
                    draw_status = False
                if event.type == pygame.MOUSEMOTION:
                    if draw_status:
                        Draw_Without_Intervals(screen, last_pos, event.pos, radius, color)
                    last_pos = event.pos
            if(mode == 1):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.circle(screen, color, event.pos, radius,1)
            if(mode == 2):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    xxx,yyy = event.pos
                    if event.button == 1:
                        x1_rect = xxx
                        y1_rect = yyy
                    if event.button == 3:
                        x2_rect = xxx
                        y2_rect = yyy
        if(x1_rect != x2_rect and y1_rect != y2_rect and y2_rect != 0 and x1_rect != 0): 
            pygame.draw.rect(screen, color, [x1_rect, y1_rect, x2_rect-x1_rect, y2_rect-y1_rect], radius)
            x1_rect = 0
            y1_rect = 0
            x2_rect = 0
            y2_rect = 0
                    
                
        pygame.display.flip()

pygame.quit()
