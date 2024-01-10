#import and install all required modules
#IMPORANT DISCLAIMER: EDIT LINE 110 & 201 TO YOUR OWN DEVICE-SPECIFIC IMAGE PATH IF DIFFERENT
import pygame as pg
import sys, random, math
import pygame
import time

#Screen settings
WIDTH  = 768 #24 32-px tiles
HEIGHT = 768 #24 32-px tiles
TILE   =  32
FPS    =  60

#Colors
BLUE = (0 ,0 ,255)
RED= (255, 0 , 0)
TEAL =(0,128,128)
BLACK = (0,0,0)
WHITE= (255,255,255)

#global variables
MAX_OBSTACLE_SPEED = 7
MIN_OBSTACLE_SPEED = 2
LEVEL_TIME = 5000
MAX_HEIGHT = 0
MIN_HEIGHT = 23
JUMP_TIME = 325 #In milliseconds

#text function to display text on screen
def draw_text(text, surface, size, x, y, fg_color, bg_color):
    '''
    Draws text (String) on surface (Surface) using a default font in size (Int)
    Positions the center left of the bounding box at x, y (Int, Int)
    Foreground color and Background color are color tuples (R, G, B)
    '''
    font = pg.font.Font('freesansbold.ttf', size) #what type of font the user wants for text
    textSurf = font.render(text, True, fg_color, bg_color)
    textRect = textSurf.get_rect()#text gets intilaized in .rect for it to display onto the screen
    textRect.midright = (x, y) #where it should be situated
    surface.blit(textSurf, textRect) #bilting = drawing on the screen

class Game:
    
    def __init__(self):     
        pg.init() #Initialize the pygame module
        self.screen = pg.display.set_mode((WIDTH, HEIGHT)) #Initialize the window/screen
        self.clock = pg.time.Clock() #Initilize the clock
        self.isJump = False
        self.jump_pressed = False     
        
    def new(self):
        self.total_time = 0        
        self.timer = 0
        self.all_sprites = pg.sprite.Group() #Create a group for all sprites
        self.obstacle = pg.sprite.Group()
        self.a = Archibald(self, 3, 20)
        self.walls = pg.sprite.Group()
        for i in range(3):#3 obstacles in game, to increase obstacles in game at a time increase the value of 3
            Obstacle0(self, 26, random.randrange(MAX_HEIGHT, MIN_HEIGHT)) #max height and max range indicate how long or short the object must be

        
    def run(self):     
        self.playing = True
        #Game loop
        while self.playing:   
            self.dt = self.clock.tick(FPS) #Capture time elapsed each frame and keep game running < FPS.
            self.timer += self.dt
            self.total_time += self.dt
            if self.playing is False: #if game is not playing or it restars it sets the stopwatch to 0
                self.total_time = 0
            self.events()
            self.update()
            self.draw()


    def events(self):                    
        for event in pg.event.get():
            #Close application when "X" is clicked.
            if event.type == pg.QUIT:                
                pg.quit()
                sys.exit()
            #keyboard controls for archie
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.a.jump()
                if event.key == pg.K_DOWN:
                    self.a.fallDown()

    def update(self):
        global MIN_OBSTACLE_SPEED
        if self.timer >= LEVEL_TIME:   #speeds up obstacles the longer the time passes in game without Archibald dying
            self.timer = 0
            for obstacle in self.obstacle:
                obstacle.vx += 1
                MIN_OBSTACLE_SPEED += 1           
        self.all_sprites.update() #Run the update() method for each sprite in all_sprites group.
        
    def draw(self):
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps())) #FPS in window caption (for testing).
        self.screen.fill(BLACK) #background color
        self.all_sprites.draw(self.screen)#Run the draw() method for each sprite in all_sprites group.
        draw_text(str(round(self.total_time / 1000,1)), self.screen, 30, WIDTH-10,20,WHITE,BLACK) #display text on screen
        pg.display.flip() #Display updated screen on computer screen.
        

class Archibald(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.game = game
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = pg.image.load("archie_0.png") #loads image
        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = x * TILE, y * TILE
        self.vx, self.vy = 0, 0
         #when game stars, archie would not be jumping nor falling
        self.jumping = False 
        self.falling = False
   
    def archibaldRotate():
       self.image = pg.transform.rotate(self.image,1)

    def update(self):
        global MIN_OBSTACLE_SPEED
        if pg.sprite.spritecollide(self, self.game.obstacle, False): #what to do when the obstacle collides with the object
            print("Game Over!")
            MIN_OBSTACLE_SPEED = 2
            self.game.new()#restarts the game

        if self.jumping:  #if condition for archibald to jump
            self.jumping_for += self.game.dt
            if self.jumping_for > JUMP_TIME: 
                self.jumping = False
            self.rect.y -= 13 * math.sin(math.pi * self.jumping_for / (JUMP_TIME / 2))#to jump up

        if self.falling:
            self.falling_for += self.game.dt
            if self.falling_for > JUMP_TIME:
                self.falling = False
            self.rect.y += 14 * math.sin(math.pi * self.falling_for / (JUMP_TIME / 2))#to jump down

        self.rect.x += self.vx * self.game.dt
        self.rect.y += self.vy * self.game.dt

        wall_hit = pg.sprite.spritecollideany(self, self.game.walls)
        if wall_hit: #if conditions on what qualifies as hitting the wall for Archibald
            if self.vx < 0:
                self.rect.x = wall_hit.rect.x + TILE
            if self.vx > 0:
                self.rect.x = wall_hit.rect.x - TILE
            if self.vy < 0:
                self.rect.y = wall_hit.rect.y + TILE
            if self.vy > 0:
                self.rect.y = wall_hit.rect.y - TILE
            self.vx, self.vy = 0, 0
            

        if self.rect.x < -TILE:
            self.rect.x = WIDTH
        if self.rect.x > WIDTH:
            self.rect.x = -TILE
        if self.rect.y < -TILE:
            self.rect.y = HEIGHT
        if self.rect.y > HEIGHT:
            self.rect.y = -TILE
            
    def jump(self): #jump function whenever archibald starts to jump 
        self.jumping_for = 0
        self.jumping = True
        print("I'm jumping.")

    def fallDown(self):#func to go down and print a bunch of strings whenever archibald starts to go down
        self.falling_for = 0 
        self.falling = True
        print("I'm Falling")        

class Wall(pg.sprite.Sprite):#Intiializing wall class
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups) #wall is now part of pg.sprite

        self.image = pg.Surface((TILE, TILE))
        self.rect = self.image.get_rect() 
        pg.draw.rect(self.image, TEAL, self.rect)#color for wall

        self.rect.x, self.rect.y = x * TILE, y * TILE
        self.vx, self.vy = 0, 0

    def check_collision(x, y):#func to check collision
        if self.rect.colliderect(wall.rect):
            if x > 0: #The players x value is increasing (to the right)
                self.rect.right = wall.rect.left
        
class Obstacle0(pg.sprite.Sprite): #intilaizing class for the obstacle in-game
    
    def __init__(self,game,x,y):
        self.game = game        
        self.groups = game.all_sprites, game.obstacle
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = pg.image.load("obstacle0.png") #load image
        self.rect = self.image.get_rect() #used to display image on screen 
        self.rect.x, self.rect.y = x * TILE + random.randint(0, 750), y * TILE #obstacle will spawn on these coordinates
        self.vx = MIN_OBSTACLE_SPEED #obstacle will spawn with the value of the most minimum speed intilaized 


    def update(self):#object func to watch for events like going beyond the wall
        self.rect.x -= self.vx
        if self.rect.right < 0:
            self.kill()
            Obstacle0(self.game, 26, random.randrange(MAX_HEIGHT, MIN_HEIGHT))
   
    def obstacle0Rotate():
       self.image = pg.transform.rotate(self.image,1)



g = Game() #Create a game object.
while True:
    g.new() #Start a new game.
    g.run() #Begin the game loop.
