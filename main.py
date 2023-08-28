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

naveInimiga = pygame.image.load('img/spaceship.png').convert_alpha()
naveInimiga = pygame.transform.scale(naveInimiga, (70, 70))

position_player_x = 200
position_player_y = 300

position_inimigo_x = 1280
position_inimigo_y = 360




rodando = True #Se tiver como 'True' está funcionando

def respaw():
    x = 1350
    y = random.randint(1, 640)
    return [x, y]

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

    if tecla[pygame.K_DOWN] and position_player_y < 665:
        position_player_y += 1

    if tecla[pygame.K_SPACE]:
        triggered = True
        velocidade_missil_x = 1

    if position_inimigo_x <= 10:
        position_inimigo_x = respaw()[0]
        position_inimigo_y = respaw()[1]

    x -= 1
    position_inimigo_x -= 0.75
    print(position_inimigo_x)
    screen.blit(player, (position_player_x, position_player_y))
    screen.blit(naveInimiga, (position_inimigo_x, position_inimigo_y))

        



    pygame.display.update()

pygame.quit()    