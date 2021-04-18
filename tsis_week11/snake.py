import pygame,random,time,json, pickle
#pylint: disable=no-member
"""
v 1. Add food

v 2. Add walls

v 3. Add levels (speed and walls)

v 4. Add save game state to file

v 5. Two snake in one game (with different control buttons)
"""

pygame.init()
pygame.font.init()

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
random_color_for_snake = [white,blue,green,red,lime,yellow,silver,purple,golden]
pygame.mixer.music.load("background_music.mp3")
pygame.mixer.music.play(-1)

class walls_objects:
    def __init__(self, walls = None):
        self.walls=[[random.randint(50,750),random.randint(50,550)]]
    def draw_me(self):
        for wall_x,wall_y in self.walls:
            pygame.draw.line(screen, red, (wall_x, wall_y), (wall_x+30,wall_y),10)
    def generate_wall(self,x,y):
        first_random_x=random.randint(50,x)
        second_random_x = random.randint(x,750)
        first_random_y = random.randint(50,y)
        second_random_y = random.randint(y,550)
        correct_x = max(abs(first_random_x-x), abs(second_random_x-x))
        correct_y = max(abs(first_random_y-y), abs(second_random_y-y))
        self.walls.append([correct_x, correct_y])

    
class food:
    def __init__(self):
        self.image=pygame.image.load("apple.png")
        self.image.set_colorkey(white)
        self.x = random.randint(50,750)
        self.y = random.randint(50,550)
        self.lasteaten = None
        self.size = 1
    def gen(self):
        self.x = random.randint(50,750)
        self.y = random.randint(50,550)
        self.size += 1
    def draw(self):
        screen.blit(self.image,(self.x, self.y))



class Snake:
    def __init__(self,x,y, size = None, dx=None, dy = None, is_grow = None,elements=None):
        self.size = 1
        self.color = random_color_for_snake[random.randint(0,8)]
        self.elements = [[x,y]]
        self.radius = 12
        self.dx = 5
        self.dy = 0
        self.is_grow = False
    def draw_circle(self):
        for element in self.elements:
            pygame.draw.circle(screen, self.color, element, 12)
    def add_to_snake(self):
        self.elements.append([0,0])
        self.size += 1
        self.is_grow = False
    def move(self):
        if self.is_grow:
            self.add_to_snake()
        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]

        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy
    def check_collision_with_main(self): 
        for i in range(1,len(self.elements)):
            if self.elements[0][0] == self.elements[i][0] and self.elements[0][1] == self.elements[i][1]:
                return True
        return False
                
    def check_food(self,apple_x,apple_y):
        x = self.elements[0][0]
        y = self.elements[0][1]
        if x in range(apple_x-22,apple_x+22) and y in range(apple_y-22,apple_y+22):
            return True
        else:
            return False


font_for_player_win = pygame.font.SysFont("arial", 25)
apple = food()
walling = walls_objects()
apple.image.set_colorkey(white)
size = (800,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
run = False
restart = False
main_menu = True
game = True
FPS = 30
d=5
last_win = 0 # 1 first player, 2 second player
current_level = 1
snake1=Snake(100,100)
snake2=Snake(500,500)

while game:
    while main_menu:
        screen.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: 
                    game = False
                    restart = False
                if event.key == pygame.K_s: 
                    apple = food()
                    walling = walls_objects()
                    apple.image.set_colorkey(white)
                    current_level = 1
                    snake1=Snake(100,100)
                    snake2=Snake(500,500)
                    run = True
                    main_menu = False
                if event.key == pygame.K_q:
                    with open("savegame", "rb") as f:
                        snake1 = pickle.load(f)
                        snake2 = pickle.load(f)
                        walling = pickle.load(f)
                    """ file = open("saves.txt", 'r')
                    cnt = 0
                    for i in file:
                        massive = i.split(',')
                        if(cnt == 0):
                            snake1 = Snake(100,100, massive[0],massive[1],massive[2],massive[3],str(new_elements))
                        if(cnt == 1):
                            new_elements = []
                            for i in massive[4]:
                                new_elements.append(i)
                            snake2 = Snake(500,500, massive[0],massive[1],massive[2],massive[3],new_elements)
                        if(cnt == 2):
                            new_elements = []
                            for i in massive[0]:
                                new_elements.append(i)
                            walling = walls_objects(massive[0])
                        #{snake1.size},{snake1.dx},{snake1.dy},{snake1.is_grow},{snake1.elements}
                        cnt += 1 """
                    apple = food()
                    apple.image.set_colorkey(white)
                    current_level = 1
                    run = True
                    main_menu = False
                
        screen.blit(font_for_player_win.render("Start new game(S)", True, golden), (320,150))
        screen.blit(font_for_player_win.render("Continue last game(Q)", True, golden), (320,200))
        screen.blit(font_for_player_win.render("Exit game (ESC)", True, golden), (320,250))
        pygame.display.flip()
    while restart:
        screen.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: 
                    game = False
                    restart = False
                if event.key == pygame.K_r: 
                    apple = food()
                    walling = walls_objects()
                    apple.image.set_colorkey(white)
                    current_level = 1
                    snake1=Snake(100,100)
                    snake2=Snake(500,500)
                    run = True
                    restart = False
        if last_win == 2: screen.blit(font_for_player_win.render("Player 2 won", True, golden), (320,150))
        else: screen.blit(font_for_player_win.render("Player 1 won", True, golden), (320,150))
        screen.blit(font_for_player_win.render("Restart game (R)", True, golden), (320,200))
        screen.blit(font_for_player_win.render("Exit game (ESC)", True, golden), (320,250))
        pygame.display.flip()

    while run:
        screen.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and snake1.dx != d:
                    snake1.dx = -d
                    snake1.dy = 0
                if event.key == pygame.K_d and snake1.dx != -d:
                    snake1.dx = d
                    snake1.dy = 0
                if event.key == pygame.K_s and snake1.dy != -d:
                    snake1.dx = 0
                    snake1.dy = d
                if event.key == pygame.K_w and snake1.dy != d:
                    snake1.dx = 0
                    snake1.dy = -d
                
                if event.key == pygame.K_LEFT and snake2.dx != d:
                    snake2.dx = -d
                    snake2.dy = 0
                if event.key == pygame.K_RIGHT and snake2.dx != -d:
                    snake2.dx = d
                    snake2.dy = 0
                if event.key == pygame.K_DOWN and snake2.dy != -d:
                    snake2.dx = 0
                    snake2.dy = d
                if event.key == pygame.K_UP and snake2.dy != d:
                    snake2.dx = 0
                    snake2.dy = -d
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                with open("savegame", "wb") as f:
                    pickle.dump(snake1, f)
                    pickle.dump(snake2, f)
                    pickle.dump(walling, f)
                """ file = open("saves.txt",'w')
                file.write(f"{snake1.size},{snake1.dx},{snake1.dy},{snake1.is_grow},{snake1.elements}")
                file.write('\n')
                file.write(f"{snake2.size},{snake2.dx},{snake2.dy},{snake2.is_grow},{snake2.elements}")
                file.write('\n')
                file.write(f"{walling.walls}")
                """
                time.sleep(1)
                #file.close()
                #size = None, dx=None, dy = None, is_grow = None,elements=None
                run = False
                restart = False
                pygame.quit()

        if(snake1.check_food(apple.x,apple.y)):
            snake1.is_grow = True
            apple.lasteaten = 'snake1'
            apple.gen()
        if(snake2.check_food(apple.x,apple.y)):
            snake2.is_grow = True
            apple.lasteaten = 'snake2'
            apple.gen()
        if(apple.size % 5 == 0):
            if(apple.lasteaten == 'snake1'): walling.generate_wall(snake1.elements[0][0], snake1.elements[0][1])
            else: walling.generate_wall(snake2.elements[0][0], snake2.elements[0][1])
            apple.size += 1
            FPS += 1
        for x,y in walling.walls:
            if(snake1.elements[0][0] in range(x-13,x+44) and snake1.elements[0][1] in range(y-18,y+16)):
                time.sleep(2)
                last_win = 2
                restart = True
                run = False
            if(snake2.elements[0][0] in range(x-13,x+44) and snake2.elements[0][1] in range(y-18,y+16)):
                time.sleep(2)
                last_win = 1
                restart = True
                run = False
        walling.draw_me()
        snake1.move()
        snake2.move()
        if(snake1.check_collision_with_main() == True):
            time.sleep(2)
            last_win = 2
            restart = True
            run = False
        if(snake2.check_collision_with_main() == True):
            time.sleep(2)
            last_win = 1
            restart = True
            run = False
        for i in range(1,snake1.size):
            if(snake2.elements[0][0] in range(snake1.elements[i][0], snake1.elements[i][0]+10) and snake2.elements[0][1] in range(snake1.elements[i][1], snake1.elements[i][1]+10) and snake1.size != 1 and snake2.size != 1):
                time.sleep(2)
                last_win = 1
                restart = True
                run = False
        for i in range(1,snake2.size):
            if(snake1.elements[0][0] in range(snake2.elements[i][0], snake2.elements[i][0]+10) and snake1.elements[0][1] in range(snake2.elements[i][1], snake2.elements[i][1]+10) and snake1.size != 1 and snake2.size != 1):
                time.sleep(2)
                last_win = 2
                restart = True
                run = False
        apple.draw()
        snake1.draw_circle()
        snake2.draw_circle()
        clock.tick(FPS)
        pygame.display.flip()
pygame.quit()