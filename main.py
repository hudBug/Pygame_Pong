import pygame

pygame.init()
pygame.font.init()

#atributos do jogo
tela = pygame.display.set_mode((1280, 720)) # criação da tela

jogador1 = pygame.Rect(0,0,30,150) # cria o jogador como um retangulo: x,y da posição x,y do tamanho do objeto a partir da posição definida
jogador1Velocidade = 6 # o sinal dessa variável determina o movimenta será para baixo (+) ou para cima (-) devido ao ponto 0 ser o canto superior esquerdo
jog1Placar = 0

jogador2 = pygame.Rect(1250,0,30,150)
jog2Placar = 0

bola = pygame.Rect(600,350,15,15)
bolaDirX = 6
bolaDirY = 6
colisao = pygame.mixer.Sound("assets/pong.wav")

fps = pygame.time.Clock() #padroniza a taxa de FPS independente do processador

fonte = pygame.font.Font(None, 48) # fonte e tamanho, none = fonte do sistema
placarJog1 = fonte.render(str(jog1Placar), True, (255, 255, 255)) # texto padrão, antialias, cor do texto, cor de fundo(opcional)
placarJog2 = fonte.render(str(jog2Placar), True, (255, 255, 255))
fim = fonte.render("Fim de jogo", True, (255, 255, 255))
nome = fonte.render("-= Pong no Pygame! =-", True, (255, 255, 255))
texto = fonte.render("Pressione Enter para iniciar :)", True, (255, 255, 255))
texto2 = fonte.render("Pressione Enter para voltar ao menu :)", True, (255, 255, 255))

laco = True

cena = "menu"

while laco:

    if cena == "jogando":
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT: # sai ao apertar no X
                laco = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE: # sai ao apertar ESC
                    laco = False
                # movimentos se baseiam em inverter o sinal da variável jogador1Velocidade
                if evento.key == pygame.K_w:
                    jogador1Velocidade = -6
                elif evento.key == pygame.K_s:
                    jogador1Velocidade = 6
        
        # Verificação do placar para o fim
        if jog2Placar >= 3:
            cena = "fim"

        # colisões da bola com os jogadores
        if bola.colliderect(jogador1) or bola.colliderect(jogador2):
            bolaDirX *= -1
            colisao.play()    

        # limites do jogador em Y, impedindo que o jogador suma da tela
        if jogador1.y <= 0:
            jogador1.y = 0
        elif jogador1.y >= 720 - 150: # tamanho do meu y subtraido pelo y do jogador
            jogador1.y = 720 - 150

        jogador1.y += jogador1Velocidade

        #movimento da bola
        if bola.x <= 0:
            jog2Placar += 1
            placarJog2 = fonte.render(str(jog2Placar), True, (255, 255, 255))
            bola.x = 600
            bolaDirX *= -1
        elif bola.x >= 1280:
            jog1Placar += 1
            placarJog1 = fonte.render(str(jog1Placar), True, (255, 255, 255))
            bola.x = 600
            bolaDirX *= -1

        if bola.y <= 0:
            bolaDirY *= -1
        elif bola.y >= 720 - 15:
            bolaDirY *= -1

        bola.x += bolaDirX
        bola.y += bolaDirY

        #movimento do jogador 2
        jogador2.y = bola.y - 75 #faz com que o jogador acompanhe o eixo Y da bola e que a bola colida sempre no meio do jogador 2
        
        if jogador2.y <= 0:
            jogador2.y = 0
        elif jogador2.y >= 720 - 150: # tamanho do meu y subtraido pelo y do jogador
            jogador2.y = 720 - 150

        tela.fill((0, 0, 0 )) # coloca a cor preta como sendo o fundo da tela
        pygame.draw.rect(tela, (255, 255, 255), jogador1) #desenha o jogador como um retangulo: tela, cor, dimensões
        pygame.draw.rect(tela, (255, 255, 255), jogador2)
        pygame.draw.circle(tela, (255, 255, 255), bola.center, 8)#desenha um circulo: tela, cor, centro do objeto e raio
        tela.blit(placarJog1, (500, 50)) #desenha o placar, objeto, posição
        tela.blit(placarJog2, (780, 50)) #desenha o placar, objeto, posição

    elif cena == "fim":
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT: # sai ao apertar no X
                laco = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE: # sai ao apertar ESC
                    laco = False
                if evento.key == pygame.K_RETURN:
                    jog1Placar = 0
                    placarJog1 = fonte.render(str(jog1Placar), True, (255, 255, 255))
                    jog2Placar = 0
                    placarJog2 = fonte.render(str(jog2Placar), True, (255, 255, 255))
                    jogador1.y = 0
                    jogador2.y = 0
                    bola.x = 640
                    bola.y = 320
                    cena = "menu"

        tela.fill((0, 0, 0 ))
        tela.blit(fim, (430, 100))
        tela.blit(texto2, (330, 200))

    elif cena == "menu":
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT: # sai ao apertar no X
                laco = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE: # sai ao apertar ESC
                    laco = False
                if evento.key == pygame.K_RETURN:
                    cena = "jogando"

        tela.fill((0, 0, 0 ))
        tela.blit(nome, (490, 100))
        tela.blit(texto, (390, 200))

    fps.tick(60)
    pygame.display.flip() #atualiza a tela