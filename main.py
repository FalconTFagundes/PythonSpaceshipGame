import random
import pygame

pygame.init()

pygame.mixer.init()
pygame.mixer.music.load('musicas/TopGearVegas.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)


""" Altura e largura da janela """
x = 1280  #Horizontal
y = 720   #Vertical


screen = pygame.display.set_mode((x,y)) #Setando minha altura e largura na janela 
pygame.display.set_caption('Meu jogo em python') #Nome janela 

bgImg = pygame.image.load('img/ceuEstrelado.jpg').convert_alpha()
bg = pygame.transform.scale(bgImg, (x, y))

playerImg = pygame.image.load('img/navePixel.png').convert_alpha()
player = pygame.transform.scale(playerImg, (100, 100))
player = pygame.transform.rotate(player, -90)

missilImg = pygame.image.load('img/bolaDeEnergia.png').convert_alpha()
missil = pygame.transform.scale(missilImg, (34.375, 34.375))
""" missil = pygame.transform.rotate(missil, -25) """

inimigo = pygame.image.load('img/spaceship.png').convert_alpha()
inimigo = pygame.transform.scale(inimigo, (70, 70))

font = pygame.font.SysFont('fonts/PixelGameFont.ttf', 50)
gameOverFont = pygame.font.SysFont('fonts/PixelGameFont.ttf', 80)

lifeImg = pygame.image.load('img/life.jpg').convert_alpha()
lifeImg = pygame.transform.scale(lifeImg, (25, 25))

boss = pygame.image.load('img/boss.png').convert_alpha()
boss = pygame.transform.scale(boss, (700, 700))
boss = pygame.transform.rotate(boss, -44 )

missilBoss = pygame.image.load('img/missilBoss.png').convert_alpha()
missilBoss = pygame.transform.scale(missilBoss, (64, 64))

fraseGamerOver = 'Você perdeu!'

position_player_x = 200
position_player_y = 300

velocidade_missil_x = 0
position_missil_x = 260
position_missil_y = 300

position_inimigo_x = 1280
position_inimigo_y = 360

position_boss_x = 750
position_boss_y = -130

velocidade_missil_boss_x = 0
position_missil_boss_x = 1200
position_missil_boss_y = 320


boss_rect = boss.get_rect()
player_rect = player.get_rect()
inimigo_rect = inimigo.get_rect()
missil_rect = missil.get_rect()
missil_boss_rect = missilBoss.get_rect()

""" altura e largura do rect do boss """
boss_rect.width = 300  
boss_rect.height = 1000


""" VARIÁVEIS """
lifePlayer = 3

lifeBoss = 10

pontos = 0

triggered = False

rodando = True #Se tiver como 'True' está funcionando


# FUNCS

def gameOver():
    gamerOver = gameOverFont.render(fraseGamerOver, True, (255,255,255))
    screen.blit(gamerOver, (350, 300))


def respaw():
    x = 1350
    y = random.randint(1, 640)
    return [x, y]

def respaw_missil():
    triggered = False
    respaw_missil_x = position_player_x
    respaw_missil_y = position_player_y
    velocidade_missil_x = 0
    return [(respaw_missil_x + (60)), (respaw_missil_y + 0), triggered, velocidade_missil_x]

def ataque_boss():
    global position_missil_boss_x
    global position_missil_boss_y

    position_missil_boss_x -= 12 #velocidade missil do boss
    screen.blit(missilBoss, (position_missil_boss_x, position_missil_boss_y)) 
    print(missilBoss)

    if position_missil_boss_x <= 10:
        position_missil_boss_x = respaw()[0]
        position_missil_boss_y = respaw()[1]


def colisaoMissilBoss():
    global lifePlayer
    global position_missil_boss_x
    global position_missil_boss_y

    if player_rect.colliderect(missil_boss_rect): #Verificando Colisão
        position_missil_boss_x = respaw()[0] #Respawnando Missil Boss
        position_missil_boss_y = respaw()[1]
        lifePlayer -= 2 #perde 2 de HP
        return True
    else:
        return False





""" função de colisão """
def colisaoInimigo():
    global lifePlayer
     
    if player_rect.colliderect(inimigo_rect) or inimigo_rect.x <= 20:
        lifePlayer -=1

        return True
    else:
        return False
    
    
    
    
def colisaoMissil():
    global pontos
    global position_inimigo_x
    global position_inimigo_y
    global position_missil_x
    global position_missil_y
    global triggered
    global velocidade_missil_x


    if missil_rect.colliderect(inimigo_rect):
        position_inimigo_x = respaw()[0]
        position_inimigo_y = respaw()[1]    

        """ PONTUAÇÃO """

        pontos +=100

        return True
    

def colisaoBoss():
    global lifeBoss
    global position_missil_x
    global position_missil_y

    if missil_rect.colliderect(boss_rect):
        position_missil_x = respaw()[0]
        position_missil_y = respaw()[1]
        lifeBoss -= 1
        return True
    else: 
        return False


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
        position_player_y -= 2
        if not triggered:
            position_missil_y -= 2

    if tecla[pygame.K_DOWN] and position_player_y < 665:
        position_player_y += 2
        if not triggered:
            position_missil_y += 2

    if tecla[pygame.K_SPACE]:
        triggered = True
        velocidade_missil_x = 4


    """ rect recebendo a posição de seu específico elemento """
    player_rect.x = position_player_x
    player_rect.y = position_player_y

    missil_rect.x = position_missil_x
    missil_rect.y = position_missil_y
    
    inimigo_rect.x = position_inimigo_x
    inimigo_rect.y = position_inimigo_y

    boss_rect.x = 1100
    boss_rect.y = 10
    
    missil_boss_rect.x = position_missil_boss_x
    missil_boss_rect.y = position_missil_boss_y

    x -= 1

    position_inimigo_x -= 0.75
    position_missil_x += velocidade_missil_x
    print(position_missil_y)


    """ adicionando desenho da área de contato entre os elementos """
    pygame.draw.rect(screen, (255,0,0), boss_rect, 4)
    pygame.draw.rect(screen, (255,0,0), player_rect, 4)
    pygame.draw.rect(screen, (255,0,0), inimigo_rect, 4)
    pygame.draw.rect(screen, (255,0,0), missil_rect, 4)
    pygame.draw.rect(screen, (255,0,0), missil_boss_rect, 4)

  

    
    
    # PARTE QUE IMPRIEME AS IMG

    score = font.render(str(pontos), True, (255, 255, 255)) 
    screen.blit(score, (1150, 50)) # IMPRIMINDO SCORE

    
    screen.blit(player, (position_player_x, position_player_y)) 
    screen.blit(inimigo, (position_inimigo_x, position_inimigo_y))
    screen.blit(missil, (position_missil_x, position_missil_y))
    
    if pontos >= 100: #CONDIÇÃO PARA IMPRIMIR O BOSS NA TELA

        """ inimigo some da tela "1800" """
        position_inimigo_x = 1800 
        position_inimigo_y = 1800
        
        
        #IMPRIMINDO O BOSS NA TELA
        screen.blit(boss, (position_boss_x, position_boss_y)) 


        #IMPRIMINDO MISSIL DO BOSS
        ataque_boss() #Invoco a função dos misseis do boss
        colisaoMissilBoss() #Faço o teste de colisão
        colisaoBoss()
      

    for i in range(lifePlayer):
        screen.blit(lifeImg, (50 + i * 30, 50))
    


    pygame.display.update()

    if position_inimigo_x <= 10 or colisaoInimigo():
        position_inimigo_x = respaw()[0]
        position_inimigo_y = respaw()[1]

    if position_missil_x >= 1300 or colisaoMissil():
        position_missil_x = respaw_missil()[0]
        position_missil_y = respaw_missil()[1]
        triggered = respaw_missil()[2]
        velocidade_missil_x = respaw_missil()[3]
    

 
 


pygame.quit()    