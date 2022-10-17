import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 640
altura = 480

Player_y = int(largura/2)
Player_x = int(altura/2)

speed = 10
Controle_y = speed
Controle_x = 0

Maça_y = randint(50,640)
Maça_x = randint(50,450)

Pontos = 0
Fonte_m = pygame.font.SysFont('arial', 40, bold =True, italic=False)
Fonte = pygame.font.SysFont('arial', 40, bold=True, italic=False)

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('NOKIA_COBRINHA.PY')
clock = pygame.time.Clock()
lista_Corpo = list()
comprimento_inicial = 5
morreu = False

Lista_Corpo = list()
def estica(Lista_Corpo):
    for YeX in Lista_Corpo:
#        pygame.draw.rect(tela, (randint(0,255),randint(0,255),randint(0,255)), (YeX[0],YeX[1],20,20))
        pygame.draw.rect(tela, (0,255,0), (YeX[0],YeX[1],20,20))


def reset():
    global Pontos, comprimento_inicial, Player_y, Player_x, Lista_Cabeça, Lista_Corpo, Maça_y, Maça_x, morreu
    Pontos = 0 
    comprimento_inicial = 5
    Player_y = largura/2
    Player_x = altura/2
    Lista_Cabeça = list()
    Lista_Corpo = list()
    Maça_y = randint(50,640)
    Maça_x = randint(50,450)
    morreu = False


while True:
    tela.fill((0,0,0))
    clock.tick(30)

    mensagem = f'Maças Pegas:{Pontos}'
    texto = Fonte.render(mensagem, True, (255,255,255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                if Controle_y == speed:
                    pass
                else:
                    Controle_y = -speed
                    Controle_x = 0
            if event.key == K_d:
                if Controle_y == -speed:
                    pass
                else:
                    Controle_y = speed
                    Controle_x = 0
            if event.key == K_w:
                if Controle_x == speed:
                    pass
                else:
                    Controle_x = -speed
                    Controle_y = 0
            if event.key == K_s:
                if Controle_x == -speed:
                    pass
                else:
                    Controle_x = speed
                    Controle_y = 0

    Player_y += Controle_y
    Player_x += Controle_x

    Player = pygame.draw.rect(tela, (0,255,0), (Player_y,Player_x,20,20))
    Maça = pygame.draw.circle(tela, (200,0,0), (Maça_y,Maça_x), 10)

    if Player.colliderect(Maça):
        Maça_y = randint(50,640)
        Maça_x = randint(50,450)
        Pontos += 1
        comprimento_inicial += 1

    Lista_Cabeça = list()
    Lista_Cabeça.append(Player_y)
    Lista_Cabeça.append(Player_x)
    Lista_Corpo.append(Lista_Cabeça)

    if Lista_Corpo.count(Lista_Cabeça) > 1:
        morreu = True
        while morreu:
            tela.fill((0,0,0))
            mensagem_m = 'GAME OVER(press R for restart)'
            texto_m = Fonte.render(mensagem_m, True, (255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reset()

            tela.blit(texto_m, (10,240))
            pygame.display.update()
            
    if Player_y > largura:
        Player_y = 0
    if Player_y < 0:
        Player_y = largura
    if Player_x < 0:
        Player_x = altura
    if Player_x > altura:
        Player_x = 0


    if len(Lista_Corpo) > comprimento_inicial:
        del Lista_Corpo[0]
    estica(Lista_Corpo)

    tela.blit(texto, (300,40))
    pygame.display.update()
