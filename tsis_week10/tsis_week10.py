import pygame,random, time
#pylint: disable=no-member

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

class main_car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 160
        self.y = 500
        self.image = pygame.image.load("Player.png")
        self.surface = pygame.Surface((40,80))

class enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = random.randint(10,345)
        self.y = -80
        self.image = pygame.image.load("Enemy.png")
        self.surface = pygame.Surface((40,80))
        self.speed = random.randint(1,5)
    
class coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = random.randint(10,345)
        self.y = -120
        self.image = pygame.image.load("coint.png")
        self.surface = pygame.Surface((35,35))
        self.speed = random.randint(3,8)

coins_collection=[]
coins_collection.append(coins())
enemies = []
total_score = 0
size=(400,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Cars")
background = pygame.image.load("AnimatedStreet.png")
run = True
clock = pygame.time.Clock()
my_car = main_car()
first_enemy = enemy()
font = pygame.font.SysFont("arial",30)
pygame.mixer.music.load("background.wav")
pygame.mixer.music.play(-1)

while run:
    screen.blit(background,(0,0))
    screen.blit(my_car.image, (my_car.x, my_car.y))
    screen.blit(font.render(f"Score:{total_score}",True,black),(300,30,100,100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False
        check_keyboard = pygame.key.get_pressed()
        if check_keyboard[pygame.K_a] == True or check_keyboard[pygame.K_d] == True:
            if(check_keyboard[pygame.K_a] == True and my_car.x > 10):
                my_car.x -= 8
            if(check_keyboard[pygame.K_d] == True and my_car.x < 345):
                my_car.x += 8
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and my_car.x > 40:
                my_car.x -= 3
            if event.key == pygame.K_d and my_car.x <345:
                my_car.x += 3
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            enemies.append(enemy())
    for cars in enemies:
        screen.blit(cars.image, (cars.x,cars.y))
        if(cars.y in range(my_car.y-80,580) and my_car.x in range(cars.x - 38, cars.x + 38)):
            pygame.mixer.music.stop()
            pygame.mixer.Sound('crash.wav').play()
            time.sleep(5)
            run = False
        if(cars.y < 650):
            cars.y += cars.speed
        else:
            cars.x = random.randint(10,345)
            cars.y = -20
        
    for coinz in coins_collection:
        screen.blit(coinz.image, (coinz.x,coinz.y))
        coinz.y += 3
        if(coinz.y in range(my_car.y-32,580) and my_car.x in range(coinz.x-32, coinz.x+32)):
            total_score += 1
            coinz.y = -80
            coinz.x = random.randint(10,345)
            enemies.append(enemy())
        if(coinz.y > 600):
            coinz.y = -80
            coinz.x = random.randint(10,345)
    clock.tick(60)
    pygame.display.flip()
pygame.quit()