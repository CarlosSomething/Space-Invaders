#Importando libreria pygame
import pygame
import random
import math
from pygame import mixer



#Tamaño de la ventana
pygame.init()
screen_width = 800 
screen_height = 600

size= (screen_width, screen_height)
#Definir el tamaño de la ventana con pygame
screen= pygame.display.set_mode(size)

#Agregando el fondo de pantalla
background= pygame.image.load ("Espacio.jpg")

#Musica de fondo
mixer.music.load("Background.wav")
mixer.music.play(-1)



#Definir el titulo
pygame.display.set_caption ("Space Invaders")

#Icono
icon = pygame.image.load("alien.png")
pygame.display.set_icon(icon)


go_font= pygame.font.Font("SpaceGOD.ttf", 64)
go_x= 200
go_y= 250

#Coordenadas del jugador
player_x = 370
player_y = 480
player_img = pygame.image.load("space-invaders.png")
player_x_change= 0

#Lista de parametros para multiples enemigos
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []

score = 0
score_font= pygame.font.Font ("SpaceGOD.ttf", 32)

text_x= 10
text_y= 10

def show_text (x,y):
    score_text = score_font.render ("Score : " + str (score), True, (255,255,255))
    screen.blit(score_text, (x,y))

#Funcion para llamar al pj en game loop
def player(x,y): 
    screen.blit(player_img, (x, y))

numer_enemies= 10

for item in range ( numer_enemies ):
    enemy_img.append(pygame.image.load ("Enemigo.png"))
    enemy_x.append(random.randint (0,735))
    enemy_y.append(random.randint (50, 150)) 
    enemy_x_change.append (1)
    enemy_y_change.append (30)

#Bullets

bullet_img= pygame.image.load ("bullet.png")
bullet_x=0
bullet_y=480
bullet_x_change=0
bullet_y_change=2
bullet_state="ready"

def fire(x,y):
    global bullet_state
    bullet_state= "fire"
    screen.blit(bullet_img, (x + 16, y + 10))

def is_collision (enemy_y, enemy_x, bullet_x, bullet_y):
    distance =math.sqrt ((enemy_x-bullet_x)**2 + (enemy_y-bullet_y)**2 )
    if distance <27:
        return True
    else:
        return False


def enemy (x,y):
     screen.blit(enemy_img[item], (x,y))

    

def game_over (x,y):
    go_text = go_font.render("GAME OVER!", True, (255, 255, 255))
    screen.blit(go_text, (x,y))

#Game loop

running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

 #Movimiento al presionar tecla izquierda y derecha
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -1
            if event.key == pygame.K_RIGHT:
                player_x_change = 1
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound ("Shot.wav")
                    bullet_sound.play()

                    explosion_sound = mixer.Sound ("Collision.wav") 
                               
                    bullet_x = player_x
                fire (bullet_x, bullet_y)
            
#Que se detenga el movimiento al dejar de presionar
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0 
#Agregando al enemigo

    
    
    #Color de fondo
    rgb=(255, 255, 255)
    screen.fill(rgb)
    
    screen.blit (background, (0,0))
    player_x += player_x_change
        
    if player_x <=0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    for item in range ( numer_enemies ):
        if enemy_y[item] >440:
            for j in range (numer_enemies):
                enemy_y[j]= 2000
            game_over(go_x, go_y)
            break
        enemy_x[item] += enemy_x_change[item]    
      
        if enemy_x[item] <= 0:
            enemy_x_change[item]= 1
            enemy_y[item] += enemy_y_change[item]
        elif enemy_x[item] >=736:
                enemy_x_change[item]= -1
                enemy_y[item] += enemy_y_change[item]

        collision = is_collision (enemy_y[item], enemy_x[item], bullet_x, bullet_y)
        
        if collision:

            explosion_sound.play()
            bullet_y = 480
            bullet_state = "ready"
            score += 1
            print (score)
            enemy_x[item]= random.randint (0,735)
            enemy_y[item] = random.randint (50 , 150)
        enemy (enemy_x[item], enemy_y[item])
        
        
    if bullet_y <=0:
            bullet_y= 480
            bullet_state = "ready"

    if bullet_state == "fire":
        fire (bullet_x, bullet_y)
        bullet_y -= bullet_y_change
    
    player(player_x, player_y)
    
    show_text(text_x, text_y)
    
    pygame.display.update()
