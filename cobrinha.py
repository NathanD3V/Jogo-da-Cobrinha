import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)  
green = (0, 255, 0)
blue = (50, 153, 213)

largura = 800
altura = 600
tamanho_bloco = 20
velocidade = 15

fonte = pygame.font.SysFont("bahnschrift", 25)

janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Cobrinha")

def mostrar_pontuacao(pontuacao):
    valor = fonte.render("Pontuação: " + str(pontuacao), True, yellow)
    janela.blit(valor, [0, 0])

def desenhar_cobrinha(tamanho_bloco, lista_cobrinha):
    for bloco in lista_cobrinha:
        pygame.draw.rect(janela, red, [bloco[0], bloco[1], tamanho_bloco, tamanho_bloco])

def jogo():
    fim_de_jogo = False
    fim_de_jogo_perdeu = False

    x = largura // 2
    y = altura // 2

    x_mudanca = 0
    y_mudanca = 0

    lista_cobrinha = []
    comprimento_cobrinha = 1

    comida_x = round(random.randrange(0, largura - tamanho_bloco) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura - tamanho_bloco) / 20.0) * 20.0

    relogio = pygame.time.Clock()

    while not fim_de_jogo:

        while fim_de_jogo_perdeu:
            janela.fill(blue)
            mensagem = fonte.render("Você perdeu! Pressione Q-Quit ou C-Continuar", True, red)
            janela.blit(mensagem, [largura / 6, altura / 3])
            mostrar_pontuacao(comprimento_cobrinha - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        fim_de_jogo = True
                        fim_de_jogo_perdeu = False
                    if event.key == pygame.K_c:
                        jogo()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fim_de_jogo = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_mudanca = -tamanho_bloco
                    y_mudanca = 0
                elif event.key == pygame.K_RIGHT:
                    x_mudanca = tamanho_bloco
                    y_mudanca = 0
                elif event.key == pygame.K_UP:
                    y_mudanca = -tamanho_bloco
                    x_mudanca = 0
                elif event.key == pygame.K_DOWN:
                    y_mudanca = tamanho_bloco
                    x_mudanca = 0

        x += x_mudanca
        y += y_mudanca

        if x >= largura or x < 0 or y >= altura or y < 0:
            fim_de_jogo_perdeu = True

        janela.fill(black)

        pygame.draw.rect(janela, white, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])

        cabeca_cobrinha = []
        cabeca_cobrinha.append(x)
        cabeca_cobrinha.append(y)
        lista_cobrinha.append(cabeca_cobrinha)
        if len(lista_cobrinha) > comprimento_cobrinha:
            del lista_cobrinha[0]

        for bloco in lista_cobrinha[:-1]:
            if bloco == cabeca_cobrinha:
                fim_de_jogo_perdeu = True

        desenhar_cobrinha(tamanho_bloco, lista_cobrinha)
        mostrar_pontuacao(comprimento_cobrinha - 1)

        pygame.display.update()

        if x == comida_x and y == comida_y:
            comida_x = round(random.randrange(0, largura - tamanho_bloco) / 20.0) * 20.0
            comida_y = round(random.randrange(0, altura - tamanho_bloco) / 20.0) * 20.0
            comprimento_cobrinha += 1

        relogio.tick(velocidade)

    pygame.quit()
    quit()

jogo()
