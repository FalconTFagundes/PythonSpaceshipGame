import random
import pygame

pygame.init()

""" Altura e largura da tela """
x = 1280
y = 720


screen = pygame.display.set_mode((x,y)) #Setando minha altura e largura na janela 
pygame.display.set_caption('Meu jogo em python') #Nome janela 

bgImg = pygame.image.load('img/ceuEstrelado.jpg').convert_alpha()
bg = pygame.transform.scale(bgImg, (x, y))

playerImg = pygame.image.load('img/nave.png').convert_alpha()
player = pygame.transform.scale(playerImg, (100, 100))
player = pygame.transform.rotate(player, -90)

missilImg = pygame.image.load('img/missile.png').convert_alpha()
missil = pygame.transform.scale(missilImg, (25, 25))
missil = pygame.transform.rotate(missil, -45)

naveInimiga = pygame.image.load('img/spaceship.png').convert_alpha()
naveInimiga = pygame.transform.scale(naveInimiga, (70, 70))

position_player_x = 200
position_player_y = 300

velocidade_missil_x = 0
position_missil_x = 220
position_missil_y = 330

position_inimigo_x = 1280
position_inimigo_y = 360


triggered = False

rodando = True #Se tiver como 'True' está funcionando


def respaw():
    x = 1350
    y = random.randint(1, 640)
    return [x, y]

def respaw_missil():
    triggered = False
    respaw_missil_x = position_player_x
    respaw_missil_y = position_player_y
    velocidade_missil_x = 0
    return [(respaw_missil_x + 30), (respaw_missil_y + 30), triggered, velocidade_missil_x]

   

""" Loop para verificar se o jogo está rodando """
while rodando: #RODANDO = TRUE
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #Se clicar no botão de fechar, RODANDO recebe FALSE
            rodando = False

    screen.blit(bg, (0,0))
    
    relativo_x = x % bg.get_rect().width
    screen.blit(bg, (relativo_x - bg.get_rect().width, 0))

    if relativo_x < 1280:
        screen.blit(bg, (relativo_x, 0))
        tecla = pygame.key.get_pressed()

    if tecla[pygame.K_UP] and position_player_y > 1:
        position_player_y -= 1
        if not triggered:
            position_missil_y -= 1

    if tecla[pygame.K_DOWN] and position_player_y < 665:
        position_player_y += 1
        if not triggered:
            position_missil_y += 1

    if tecla[pygame.K_SPACE]:
        triggered = True
        velocidade_missil_x = 2

    if position_inimigo_x <= 10:
        position_inimigo_x = respaw()[0]
        position_inimigo_y = respaw()[1]

    if position_missil_x == 1300:
        position_missil_x = respaw_missil()[0]
        position_missil_y = respaw_missil()[1]
        triggered = respaw_missil()[2]
        velocidade_missil_x = respaw_missil()[3]


    x -= 1
    position_inimigo_x -= 0.75
    position_missil_x += velocidade_missil_x
    print(position_missil_y)
    screen.blit(player, (position_player_x, position_player_y))
    screen.blit(naveInimiga, (position_inimigo_x, position_inimigo_y))
    screen.blit(missil, (position_missil_x, position_missil_y))

    pygame.display.update()

pygame.quit()    