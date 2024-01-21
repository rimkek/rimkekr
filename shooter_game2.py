  #Створи власний Шутер!

from pygame import *
#Створи власний Шутер!

#Створи власний Шутер!


from pygame import *
from random import randint 
from random import*

font.init()
font2 = font.Font(None, 36)
font1 =font.Font(None,80)
win=font1.render("YOU WIN",True,(255,255,255))
lose=font1.render("YOU LOSE",True,(180,0,0))

img_bullet = "nuclear-36817_1280.webp"

mixer.init()
mixer.music.load("atmosfera-okeana-27675.ogg")
mixer.music.play()
fire_sound=mixer.Sound("fire.ogg")

img_enemy="silhouette-3311636_960_720.webp"
img_back = "custom_background_by_annaza0000-d72o5s3.png"
img_hero = "space-158243_1280.webp"
img_enemy2 ="shark-3956029_1280.webp"
score = 0
lost=  0
max_lost = 3
goal =10
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x>5:
            self.rect.x-=self.speed
        if keys[K_d] and self.rect.x<win_width - 80:
            self.rect.x+=self.speed
        if keys[K_w] and self.rect.y>5:
            self.rect.y-=self.speed
        if keys[K_s] and self.rect.y<win_width - 80:
            self.rect.y+=self.speed

    def fire(self):
        bullet = Bullet(img_bullet,self.rect.centerx,self.rect.top,15,20,-15)
        bullets.add(bullet)
class Enemy(GameSprite):
    def update(self):
        self.rect.y+=self.speed
        global lost
        if self.rect.y >win_height:
            self.rect.x=randint(80,win_width-80)
            self.rect.y=0
            lost+=1
class Enemy2(GameSprite):
    def update(self):
        self.rect.y+=self.speed
        global lost
        if self.rect.x >win_width:
            self.rect.x=randint(-80,win_height =-80)
            self.rect.y=0
            lost+=1
class Bullet(GameSprite):
    def update(self): 
        self.rect.y +=self.speed
        if self.rect.y <0:
            self.kill()

win_width = 700
win_height = 500
display.set_caption("Шутер")
window = display.set_mode((win_width , win_height))
background=transform.scale(image.load(img_back),(win_width, win_height))

ship=Player(img_hero,5,win_height - 100,80,100,10)


monsters=sprite.Group() 
for i in range(1,20):
    monster = Enemy(img_enemy,randint(80,win_width-80),-40,80,50,randint(1,5))
    monsters.add(monster)

bullets=sprite.Group()
monsters2=sprite.Group()
for i in range(1,8):
    monster2 = Enemy2(img_enemy2,randint(80,win_height-80),-40,80,50,randint(1,5))
    monsters2.add(monster2)


finish = False
do_while=True
while do_while:
    for e in event.get():
        if e.type==QUIT:
            do_while =False
        elif e.type==KEYDOWN:
            if e.key == K_SPACE:
                fire_sound.play()
                ship.fire()
    if not finish: 
        window.blit(background,(0,0))
        text=font2.render("Рахунок:"+str(score),1,(255,255,255))
        window.blit(text,(10,20))
        text1=font2.render("Пропущенно:",str(lost),1,(255,255,255))
        window.blit(text1,(10,50))
        ship.update()
        collides2 = sprite.groupcollide(monsters2,bullets,True, True,)
        collides = sprite.groupcollide(monsters,bullets,True, True,)
        for c in collides:
            score+=1
            monster = Enemy(img_enemy, randint(80,win_width-80),-40,80,50,randint(1,5))
        if sprite.spritecollide(ship,monsters,False) or lost >=max_lost:
            finish=True
            window.blit(lose,(200,200))
        if score >=goal :
            finish = True
            window.blit(win,200,200)
        for c in collides2:
            monster2 = Enemy2(img_enemy2, randint(80,win_width-80),-40,80,50,randint(1,5))
        if sprite.spritecollide(ship,monsters2,False) or lost >=max_lost:
            finish=True
            window.blit(lose,(200,200))
        if score >=goal :
            finish = True
            window.blit(win,200,200)
        monsters.update()
        monsters2.update()
        bullets.update()
        ship.reset()
        monsters.draw(window)
        monsters2.draw(window)
        bullets.draw(window)
        display.update()
    time.delay(50)