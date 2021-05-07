import pygame
from random import randint
pygame.init()


x = 325 
y = 300
x1 = 250
y1 = 800
x2 = 400
y2 = 800
timer = 0
tempo_s = 0

velocidade = 15

velocidade_ot = 30


fundo = pygame.image.load('/opt/Vscode/PYgames/Data/lago.png')
carro = pygame.image.load('/opt/Vscode/PYgames/Data/ator.png')
carro1 = pygame.image.load('/opt/Vscode/PYgames/Data/ator.png')
carro2 = pygame.image.load('/opt/Vscode/PYgames/Data/ator.png')
#c_pista = pygame.image.load('/opt/Vscode/PYgames/Data/carro.png')

font = pygame.font.SysFont('arial black', 30)
texto = font.render("Tempo",True,(255,255,255),(0,0,0))
posicao = texto.get_rect()
posicao.center=(30,10)

janela = pygame.display.set_mode((800,600))
pygame.display.set_caption("Game Retro")

janela_aberta = True

while janela_aberta :
    
    pygame.time.delay(50)
    
    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            janela_aberta = False
    
    comandos = pygame.key.get_pressed()
    #if comandos[pygame.K_UP]:
     #   y-=velocidade
    #if comandos[pygame.K_DOWN]:
      #  y+=velocidade
    if comandos[pygame.K_RIGHT] and (x<=450):
        x+=velocidade
    if comandos[pygame.K_LEFT] and (x>=215):
        x-=velocidade
        #uso de comandos do teclado nas teclas w(Up),s(Down),a(Left),d(Right)
    #if comandos[pygame.K_w]:
    # y-=velocidade
    #if comandos[pygame.K_s]:
    #    y+=velocidade
    if comandos[pygame.K_d] and (x<=450):
        x+=velocidade
    if comandos[pygame.K_a] and (x>=215):
        x-=velocidade
    
    if(y <= -100):
        y = 520

    if(y1 <= -100):
        y1 = 520
    
    if(y2 <= -100):
        y2 = 520

    #alternancia dos carros
    if(y<= -180):
        y = randint(800,200)
    if((y1 <= -100)):
        y1 = randint(900,1000)
    if((y2<=-100)):
        y2 = randint(2000,2100)
    
    #limite ede colizao
    if ((x - 85 > x1 and y + 110 > y1)):
        y = 1200

    #if ((x - 80 < x1 - 300 and y + 180 > y1)):
      #  y = 1200

    #if ((x + 80 > x1 - 136 and y + 180 > y2))and((x - 80 < x1 - 136 and y + 180 > y2)):
     #   y = 1200
    

    if(timer < 20):
        timer+=1
    else:
        tempo_s +=1
        texto = font.render("Tempo: "+str(tempo_s),True,(255,255,255),(0,0,0))
        timer = 0
    
    y1 -= velocidade_ot +3
    y2 -= velocidade_ot +5

    janela.blit(fundo, (0,0))
    janela.blit(carro, (x,y))
    #janela.blit(carro1, (x1,y1))
    janela.blit(carro2, (x2,y2))
    janela.blit(texto,posicao)

    

    pygame.display.update()
pygame.quit()
