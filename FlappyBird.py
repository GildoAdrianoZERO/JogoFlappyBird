import pygame  # type: ignore
import os
import random

TELA_LARGURA = 500
TELA_ALTURA = 800

IMAGEM_CANO = pygame.transforme.sacle2x(pygame.imagem.load(os.path.join('imags','pipe.png')))
IMAGEM_CHAR = pygame.transforme.sacle2x(pygame.imagem.load(os.path.join('imags','base.png')))
IMAGEM_BACKGROUD = pygame.transforme.sacle2x(pygame.imagem.load(os.path.join('imags','bg.png')))
IMAGENS_PASSARO = [ 
    pygame.transforme.sacle2x(pygame.imagem.load(os.path.join('imags','bird1.png'))),
    pygame.transforme.sacle2x(pygame.imagem.load(os.path.join('imags','bird2.png'))),
    pygame.transforme.sacle2x(pygame.imagem.load(os.path.join('imags','bird3.png')))
]

pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial', 50)


class Passaro:
    IMGS = IMAGENS_PASSARO
    #animações da rotação
    ROTACAO_MAXIMA = 25
    VELOCIADE_ROTACAO = 20
    TEMPO_ANIMACAO = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velociade = 0
        self.altura = self.y
        self.tempo = 0
        self.contagem_imagem = 0
        self.imagem = self.IMGS[0]

    def pular(self):
        self.velocidade = -10.5
        self.tempo = 0
        self.altura = self.y
    
    def mover(self):
        #calcular o deslocamento
        self.tempo += 1
        deslocamento =  1.5 * (self.tempo**2) + self.velocidade * self.tempo

        #restringir o deslocamento
        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento < 0:
            deslocamento -= 2

        self.y += deslocamento

        #angulo do passaro
        if deslocamento < 0 or self.y < (self.altura + 50):
            if self.angulo < self.ROTACAO_MAXIMA:
                self.angulo = self.ROTACAO_MAXIMA
        else:
            if self.angulo > -90:
                self.angulo -= self.VELOCIADE_ROTACAO
    
    def desenhar(self, tela):
        #definir qual imagem do passsaro vai usar
        self.contagem_imagem += 1

        if self.contagem_imagem < self.TEMPO_ANIMACAO:
            self.imagem = self.IMGS[0]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*2:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*3:
            self.imagem = self.IMGS[2]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*4:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem >= self.TEMPO_ANIMACAO*4 + 1:
            self.imagem = self.IMGS[0]
            self.contagem_imagem = 0

        #se o passaro tiver caindo nao vai bater asa
        if self.angulo <= -80:
            self.imagem = self.IMGS[1]
            self.contagem_imagem = self.TEMPO_ANIMACAO*2

        #desenhar a imagem
        imagem_rotacionada = pygame.transform.rotate(self.imagem, self.angulo)
        posicao_centro_imagem = self.imagem.get_rect(topleft= (self.x, self.y)).center
        retangulo = imagem_rotacionada.get_rect(center = posicao_centro_imagem )
        tela.blit(imagem_rotacionada, retangulo.topleft)

    def get_mask(self):
        pygame.mask.from_surface(self.imagem)




class Cano:
    pass


class Chao:
    pass


