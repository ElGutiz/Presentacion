import pygame
import random

class Life(object):
    def __init__(self, screen):
        self.screen = screen
        _, _, self.width, self.height = screen.get_rect()
    
    def clear(self):
        self.screen.fill((0, 0, 0))
    
    def pixel(self, x, y, color):
        self.screen.set_at((x, y), color)
    
    def copy(self):
        self.prev_generation = self.screen.copy()
    
    def render(self):
        for i in range(self.width):
            for j in range(self.height):
                celula = self.prev_generation.get_at((i, j))[0]
                vecinos = []
                vivos = 0
                muertos = 0
                try:
                    v1 = self.prev_generation.get_at((i, j + 1))[0]
                    vecinos.append(v1)                            
                except:
                    continue
                
                try:
                    v2 = self.prev_generation.get_at((i, j - 1))[0]
                    vecinos.append(v2)                            
                except:
                    continue
                
                try:
                    v3 = self.prev_generation.get_at((i + 1, j))[0]
                    vecinos.append(v3)                           
                except:
                    continue
                
                try:
                    v4 = self.prev_generation.get_at((i - 1, j))[0]
                    vecinos.append(v4)                          
                except:
                    continue
                
                try:
                    v5 = self.prev_generation.get_at((i + 1, j + 1))[0]
                    vecinos.append(v5)                          
                except:
                    continue
                
                try:
                    v6 = self.prev_generation.get_at((i + 1, j - 1))[0]
                    vecinos.append(v6)                           
                except:
                    continue
                
                try:
                    v7 = self.prev_generation.get_at((i - 1, j + 1))[0]
                    vecinos.append(v7)                         
                except:
                    continue
                
                try:
                    v8 = self.prev_generation.get_at((i - 1, j - 1))[0]
                    vecinos.append(v8)                            
                except:
                    continue
                
                for vecino in vecinos:
                    if vecino == 255:
                        vivos += 1
                    else:
                        muertos += 1
                
                if vivos < 2 and celula == 255:
                    self.pixel(i, j, (0, 0, 0))
                    
                if (vivos == 2 or vivos == 3) and celula == 255:
                    self.pixel(i, j, (255, 255, 255))
                
                if vivos > 3 and celula == 255:
                    self.pixel(i, j, (0, 0, 0))
                    
                if vivos == 3 and celula == 0:
                    self.pixel(i, j, (255, 255, 255))
    
    def blinker_h(self, x, y):
        self.pixel(x, y, (255, 255, 255))
        self.pixel(x - 1, y, (255, 255, 255))
        self.pixel(x + 1, y, (255, 255, 255))
    
    def blinker_v(self, x, y):
        self.pixel(x, y, (255, 255, 255))
        self.pixel(x, y + 1, (255, 255, 255))
        self.pixel(x, y - 1, (255, 255, 255))
    
    def glider(self, x, y):
        self.pixel(x, y, (255, 255, 255))
        self.pixel(x + 1, y + 1, (255, 255, 255))
        self.pixel(x - 1, y + 2, (255, 255, 255))
        self.pixel(x, y + 2, (255, 255, 255))
        self.pixel(x + 1, y + 2, (255, 255, 255))
    
    def glider_alt_1(self, x, y):
        self.pixel(x, y, (255, 255, 255))
        self.pixel(x - 1, y - 1, (255, 255, 255))
        self.pixel(x + 1, y - 2, (255, 255, 255))
        self.pixel(x, y - 2, (255, 255, 255))
        self.pixel(x - 1, y - 2, (255, 255, 255))
    
    def glider_alt_2(self, x, y):
        self.pixel(x, y, (255, 255, 255))
        self.pixel(x + 1, y - 1, (255, 255, 255))
        self.pixel(x - 1, y - 2, (255, 255, 255))
        self.pixel(x, y - 2, (255, 255, 255))
        self.pixel(x + 1, y - 2, (255, 255, 255))
    
    def pulsar(self, x, y):
        self.blinker_h(x + 3, y + 6)
        self.blinker_h(x + 3, y + 1)
        self.blinker_h(x + 3, y - 6)
        self.blinker_h(x + 3, y - 1)
        
        self.blinker_h(x - 3, y + 6)
        self.blinker_h(x - 3, y + 1)
        self.blinker_h(x - 3, y - 6)
        self.blinker_h(x - 3, y - 1)
        
        self.blinker_v(x + 1, y + 3)
        self.blinker_v(x + 6, y + 3)
        self.blinker_v(x - 1, y + 3)
        self.blinker_v(x - 6, y + 3)
        
        self.blinker_v(x + 1, y - 3)
        self.blinker_v(x + 6, y - 3)
        self.blinker_v(x - 1, y - 3)
        self.blinker_v(x - 6, y - 3)
    
    def penta_decathlon_h(self, x, y):
        for i in range(0, 8):
            for j in range(0, 3):
                self.pixel(x + i, y + j, (255, 255, 255))
                
        self.pixel(x + 1, y + 1, (0, 0, 0))
        self.pixel(x + 6, y + 1, (0, 0, 0))
    
    def penta_decathlon_v(self, x, y):
        for i in range(0, 8):
            for j in range(0, 3):
                self.pixel(x + j, y + i, (255, 255, 255))
                
        self.pixel(x + 1, y + 1, (0, 0, 0))
        self.pixel(x + 6, y + 1, (0, 0, 0))
    
    def block(self, x, y):
        self.pixel(x, y, (255, 255, 255))
        self.pixel(x + 1, y, (255, 255, 255))
        self.pixel(x, y + 1, (255, 255, 255))
        self.pixel(x + 1, y + 1, (255, 255, 255))
    
    def lwss(self, x, y):
        self.pixel(x, y, (255, 255, 255))
        self.pixel(x, y - 2, (255, 255, 255))
        self.pixel(x + 3, y, (255, 255, 255))
        
        for i in range(1, 5):
            self.pixel(x + i, y - 3, (255, 255, 255))
        
        self.pixel(x + 4, y - 1, (255, 255, 255))
        self.pixel(x + 4, y - 2, (255, 255, 255))
    
    def hwss(self, x, y):
        self.pixel(x, y, (255, 255, 255))
        
        for i in range(1, 7):
            self.pixel(x + i, y - 1, (255, 255, 255))
            if i == 6:
                self.pixel(x + i, y, (255, 255, 255))
                self.pixel(x + i, y + 1, (255, 255, 255))
            if i == 5:
                self.pixel(x + i, y + 2, (255, 255, 255))
    
    def hwss_r(self, x, y):
        self.pixel(x, y, (255, 255, 255))
        
        for i in range(1, 7):
            self.pixel(x - i, y - 1, (255, 255, 255))
            if i == 6:
                self.pixel(x - i, y, (255, 255, 255))
                self.pixel(x - i, y + 1, (255, 255, 255))
            if i == 5:
                self.pixel(x - i, y + 2, (255, 255, 255))
    
    def ggg(self, x, y):
        self.block(x, y)
        self.block(x + 34, y - 2)
        self.blinker_v(x + 10, y)
        self.blinker_v(x + 16, y)
        self.blinker_v(x + 20, y - 2)
        self.blinker_v(x + 21, y - 2)
        
        self.pixel(x + 11, y + 2, (255, 255, 255))
        self.pixel(x + 11, y - 2, (255, 255, 255))
        
        self.pixel(x + 12, y - 3, (255, 255, 255))
        self.pixel(x + 12, y + 3, (255, 255, 255))
        self.pixel(x + 13, y - 3, (255, 255, 255))
        self.pixel(x + 13, y + 3, (255, 255, 255))
        
        self.pixel(x + 14, y, (255, 255, 255))
        
        self.pixel(x + 15, y + 2, (255, 255, 255))
        self.pixel(x + 15, y - 2, (255, 255, 255))
        
        self.pixel(x + 17, y, (255, 255, 255))
        
        self.pixel(x + 22, y, (255, 255, 255))
        self.pixel(x + 22, y - 4, (255, 255, 255))
        
        self.pixel(x + 24, y, (255, 255, 255))
        self.pixel(x + 24, y + 1, (255, 255, 255))
        self.pixel(x + 24, y - 4, (255, 255, 255))
        self.pixel(x + 24, y - 5, (255, 255, 255))
    
    def faces(self, x, y):
        self.block(x + 1, y)
        self.pixel(x, y - 1, (255, 255, 255))
        self.pixel(x, y, (255, 255, 255))
        
        #IZQUIERDA
        for i in range(1, 5):
            self.pixel(x - i, y + 1, (255, 255, 255))
        
        self.pixel(x, y + 4, (255, 255, 255))
        self.pixel(x - 1, y + 4, (255, 255, 255))
        self.pixel(x - 2, y + 3, (255, 255, 255))
        
        self.pixel(x - 4, y - 1, (255, 255, 255))
        
        self.pixel(x - 5, y - 2, (255, 255, 255))
        self.pixel(x - 5, y - 3, (255, 255, 255))
        self.pixel(x - 6, y - 4, (255, 255, 255))
        self.pixel(x - 4, y - 4, (255, 255, 255))
        self.pixel(x - 5, y - 5, (255, 255, 255))
        self.pixel(x - 5, y - 6, (255, 255, 255))
        
        #DERECHA
        x += 3
        self.pixel(x, y - 1, (255, 255, 255))
        self.pixel(x, y, (255, 255, 255))
        for i in range(1, 5):
            self.pixel(x + i, y + 1, (255, 255, 255))
        
        self.pixel(x, y + 4, (255, 255, 255))
        self.pixel(x + 1, y + 4, (255, 255, 255))
        self.pixel(x + 2, y + 3, (255, 255, 255))
        
        self.pixel(x + 4, y - 1, (255, 255, 255))
        
        self.pixel(x + 5, y - 2, (255, 255, 255))
        self.pixel(x + 5, y - 3, (255, 255, 255))
        self.pixel(x + 6, y - 4, (255, 255, 255))
        self.pixel(x + 4, y - 4, (255, 255, 255))
        self.pixel(x + 5, y - 5, (255, 255, 255))
        self.pixel(x + 5, y - 6, (255, 255, 255))
    
    def snail(self, x, y):
        #INFERIOR
        self.pixel(x, y + 3, (255, 255, 255))
        self.pixel(x + 1, y + 2, (255, 255, 255))
        self.pixel(x + 2, y + 3, (255, 255, 255))
        self.pixel(x + 3, y + 3, (255, 255, 255))
        
        self.pixel(x + 4, y + 4, (255, 255, 255))
        self.pixel(x + 4, y + 5, (255, 255, 255))
        self.pixel(x + 5, y + 4, (255, 255, 255))
        self.pixel(x + 5, y + 5, (255, 255, 255))
        
        self.pixel(x + 6, y + 5, (255, 255, 255))
        self.pixel(x + 7, y + 5, (255, 255, 255))
        
        self.pixel(x + 8, y + 6, (255, 255, 255))
        self.pixel(x + 8, y + 7, (255, 255, 255))
        self.pixel(x + 9, y + 6, (255, 255, 255))
        self.pixel(x + 9, y + 7, (255, 255, 255))
        
        self.pixel(x + 10, y + 6, (255, 255, 255))
        self.pixel(x + 10, y + 7, (255, 255, 255))
        self.pixel(x + 11, y + 4, (255, 255, 255))
        self.pixel(x + 12, y + 5, (255, 255, 255))
        self.pixel(x + 12, y + 3, (255, 255, 255))
        self.pixel(x + 13, y + 4, (255, 255, 255))
        self.pixel(x + 14, y + 4, (255, 255, 255))
        self.pixel(x + 14, y + 7, (255, 255, 255))
        self.pixel(x + 15, y + 7, (255, 255, 255))
        self.pixel(x + 16, y + 7, (255, 255, 255))
        self.pixel(x + 17, y + 6, (255, 255, 255))
        self.pixel(x + 18, y + 4, (255, 255, 255))
        self.pixel(x + 19, y + 2, (255, 255, 255))
        self.pixel(x + 19, y + 6, (255, 255, 255))
        self.pixel(x + 20, y + 4, (255, 255, 255))
        self.pixel(x + 20, y + 5, (255, 255, 255))
        self.pixel(x + 22, y + 3, (255, 255, 255))
        self.pixel(x + 22, y + 5, (255, 255, 255))
        self.pixel(x + 23, y + 3, (255, 255, 255))
        self.pixel(x + 23, y + 5, (255, 255, 255))
        self.pixel(x + 23, y + 6, (255, 255, 255))
        self.pixel(x + 24, y + 4, (255, 255, 255))
        self.pixel(x + 25, y + 2, (255, 255, 255))
        for i in range(20, 27):
            self.pixel(x + i, y + 1, (255, 255, 255))
        
        self.pixel(x + 27, y + 3, (255, 255, 255))
        self.pixel(x + 28, y + 3, (255, 255, 255))
        self.pixel(x + 28, y + 1, (255, 255, 255))
        self.pixel(x + 29, y + 3, (255, 255, 255))
        self.pixel(x + 29, y + 3, (255, 255, 255))
        
        self.pixel(x + 31, y + 2, (255, 255, 255))
        self.pixel(x + 31, y + 3, (255, 255, 255))
        self.pixel(x + 31, y + 4, (255, 255, 255))
        
        self.pixel(x + 33, y + 2, (255, 255, 255))
        self.pixel(x + 33, y + 6, (255, 255, 255))
        self.pixel(x + 34, y + 2, (255, 255, 255))
        self.pixel(x + 34, y + 3, (255, 255, 255))
        self.pixel(x + 34, y + 7, (255, 255, 255))
        self.pixel(x + 35, y + 5, (255, 255, 255))
        self.pixel(x + 35, y + 6, (255, 255, 255))
        self.pixel(x + 35, y + 7, (255, 255, 255))
        self.pixel(x + 36, y + 6, (255, 255, 255))
        self.pixel(x + 36, y + 7, (255, 255, 255))
        self.pixel(x + 36, y + 9, (255, 255, 255))
        self.pixel(x + 36, y + 10, (255, 255, 255))
        self.pixel(x + 37, y + 8, (255, 255, 255))

        #SUPERIOR
        self.pixel(x, y - 3, (255, 255, 255))
        self.pixel(x + 1, y - 2, (255, 255, 255))
        self.pixel(x + 2, y - 3, (255, 255, 255))
        self.pixel(x + 3, y - 3, (255, 255, 255))
        
        self.pixel(x + 4, y - 4, (255, 255, 255))
        self.pixel(x + 4, y - 5, (255, 255, 255))
        self.pixel(x + 5, y - 4, (255, 255, 255))
        self.pixel(x + 5, y - 5, (255, 255, 255))
        
        self.pixel(x + 6, y - 5, (255, 255, 255))
        self.pixel(x + 7, y - 5, (255, 255, 255))
        
        self.pixel(x + 8, y - 6, (255, 255, 255))
        self.pixel(x + 8, y - 7, (255, 255, 255))
        self.pixel(x + 9, y - 6, (255, 255, 255))
        self.pixel(x + 9, y - 7, (255, 255, 255))
        
        self.pixel(x + 10, y - 6, (255, 255, 255))
        self.pixel(x + 10, y - 7, (255, 255, 255))
        self.pixel(x + 11, y - 4, (255, 255, 255))
        self.pixel(x + 12, y - 5, (255, 255, 255))
        self.pixel(x + 12, y - 3, (255, 255, 255))
        self.pixel(x + 13, y - 4, (255, 255, 255))
        self.pixel(x + 14, y - 4, (255, 255, 255))
        self.pixel(x + 14, y - 7, (255, 255, 255))
        self.pixel(x + 15, y - 7, (255, 255, 255))
        self.pixel(x + 16, y - 7, (255, 255, 255))
        self.pixel(x + 17, y - 6, (255, 255, 255))
        self.pixel(x + 18, y - 4, (255, 255, 255))
        self.pixel(x + 19, y - 2, (255, 255, 255))
        self.pixel(x + 19, y - 6, (255, 255, 255))
        self.pixel(x + 20, y - 4, (255, 255, 255))
        self.pixel(x + 20, y - 5, (255, 255, 255))
        self.pixel(x + 22, y - 3, (255, 255, 255))
        self.pixel(x + 22, y - 5, (255, 255, 255))
        self.pixel(x + 23, y - 3, (255, 255, 255))
        self.pixel(x + 23, y - 5, (255, 255, 255))
        self.pixel(x + 23, y - 6, (255, 255, 255))
        self.pixel(x + 24, y - 4, (255, 255, 255))
        self.pixel(x + 25, y - 2, (255, 255, 255))
        for i in range(20, 27):
            self.pixel(x + i, y - 1, (255, 255, 255))
        
        self.pixel(x + 27, y - 3, (255, 255, 255))
        self.pixel(x + 28, y - 3, (255, 255, 255))
        self.pixel(x + 28, y - 1, (255, 255, 255))
        self.pixel(x + 29, y - 3, (255, 255, 255))
        self.pixel(x + 29, y - 3, (255, 255, 255))
        
        self.pixel(x + 31, y - 2, (255, 255, 255))
        self.pixel(x + 31, y - 3, (255, 255, 255))
        self.pixel(x + 31, y - 4, (255, 255, 255))
        
        self.pixel(x + 33, y - 2, (255, 255, 255))
        self.pixel(x + 33, y - 6, (255, 255, 255))
        self.pixel(x + 34, y - 2, (255, 255, 255))
        self.pixel(x + 34, y - 3, (255, 255, 255))
        self.pixel(x + 34, y - 7, (255, 255, 255))
        self.pixel(x + 35, y - 5, (255, 255, 255))
        self.pixel(x + 35, y - 6, (255, 255, 255))
        self.pixel(x + 35, y - 7, (255, 255, 255))
        self.pixel(x + 36, y - 6, (255, 255, 255))
        self.pixel(x + 36, y - 7, (255, 255, 255))
        self.pixel(x + 36, y - 9, (255, 255, 255))
        self.pixel(x + 36, y - 10, (255, 255, 255))
        self.pixel(x + 37, y - 8, (255, 255, 255))
    
    def snail_r(self, x, y):
        #INFERIOR
        self.pixel(x, y + 3, (255, 255, 255))
        self.pixel(x - 1, y + 2, (255, 255, 255))
        self.pixel(x - 2, y + 3, (255, 255, 255))
        self.pixel(x - 3, y + 3, (255, 255, 255))        
        self.pixel(x - 4, y + 4, (255, 255, 255))
        self.pixel(x - 4, y + 5, (255, 255, 255))
        self.pixel(x - 5, y + 4, (255, 255, 255))
        self.pixel(x - 5, y + 5, (255, 255, 255))        
        self.pixel(x - 6, y + 5, (255, 255, 255))
        self.pixel(x - 7, y + 5, (255, 255, 255))        
        self.pixel(x - 8, y + 6, (255, 255, 255))
        self.pixel(x - 8, y + 7, (255, 255, 255))
        self.pixel(x - 9, y + 6, (255, 255, 255))
        self.pixel(x - 9, y + 7, (255, 255, 255))        
        self.pixel(x - 10, y + 6, (255, 255, 255))
        self.pixel(x - 10, y + 7, (255, 255, 255))
        self.pixel(x - 11, y + 4, (255, 255, 255))
        self.pixel(x - 12, y + 5, (255, 255, 255))
        self.pixel(x - 12, y + 3, (255, 255, 255))
        self.pixel(x - 13, y + 4, (255, 255, 255))
        self.pixel(x - 14, y + 4, (255, 255, 255))
        self.pixel(x - 14, y + 7, (255, 255, 255))
        self.pixel(x - 15, y + 7, (255, 255, 255))
        self.pixel(x - 16, y + 7, (255, 255, 255))
        self.pixel(x - 17, y + 6, (255, 255, 255))
        self.pixel(x - 18, y + 4, (255, 255, 255))
        self.pixel(x - 19, y + 2, (255, 255, 255))
        self.pixel(x - 19, y + 6, (255, 255, 255))
        self.pixel(x - 20, y + 4, (255, 255, 255))
        self.pixel(x - 20, y + 5, (255, 255, 255))
        self.pixel(x - 22, y + 3, (255, 255, 255))
        self.pixel(x - 22, y + 5, (255, 255, 255))
        self.pixel(x - 23, y + 3, (255, 255, 255))
        self.pixel(x - 23, y + 5, (255, 255, 255))
        self.pixel(x - 23, y + 6, (255, 255, 255))
        self.pixel(x - 24, y + 4, (255, 255, 255))
        self.pixel(x - 25, y + 2, (255, 255, 255))
        for i in range(20, 27):
            self.pixel(x - i, y + 1, (255, 255, 255))
        
        self.pixel(x - 27, y + 3, (255, 255, 255))
        self.pixel(x - 28, y + 3, (255, 255, 255))
        self.pixel(x - 28, y + 1, (255, 255, 255))
        self.pixel(x - 29, y + 3, (255, 255, 255))
        self.pixel(x - 29, y + 3, (255, 255, 255))        
        self.pixel(x - 31, y + 2, (255, 255, 255))
        self.pixel(x - 31, y + 3, (255, 255, 255))
        self.pixel(x - 31, y + 4, (255, 255, 255))        
        self.pixel(x - 33, y + 2, (255, 255, 255))
        self.pixel(x - 33, y + 6, (255, 255, 255))
        self.pixel(x - 34, y + 2, (255, 255, 255))
        self.pixel(x - 34, y + 3, (255, 255, 255))
        self.pixel(x - 34, y + 7, (255, 255, 255))
        self.pixel(x - 35, y + 5, (255, 255, 255))
        self.pixel(x - 35, y + 6, (255, 255, 255))
        self.pixel(x - 35, y + 7, (255, 255, 255))
        self.pixel(x - 36, y + 6, (255, 255, 255))
        self.pixel(x - 36, y + 7, (255, 255, 255))
        self.pixel(x - 36, y + 9, (255, 255, 255))
        self.pixel(x - 36, y + 10, (255, 255, 255))
        self.pixel(x - 37, y + 8, (255, 255, 255))

        #SUPERIOR
        self.pixel(x, y - 3, (255, 255, 255))
        self.pixel(x - 1, y - 2, (255, 255, 255))
        self.pixel(x - 2, y - 3, (255, 255, 255))
        self.pixel(x - 3, y - 3, (255, 255, 255))        
        self.pixel(x - 4, y - 4, (255, 255, 255))
        self.pixel(x - 4, y - 5, (255, 255, 255))
        self.pixel(x - 5, y - 4, (255, 255, 255))
        self.pixel(x - 5, y - 5, (255, 255, 255))        
        self.pixel(x - 6, y - 5, (255, 255, 255))
        self.pixel(x - 7, y - 5, (255, 255, 255))        
        self.pixel(x - 8, y - 6, (255, 255, 255))
        self.pixel(x - 8, y - 7, (255, 255, 255))
        self.pixel(x - 9, y - 6, (255, 255, 255))
        self.pixel(x - 9, y - 7, (255, 255, 255))        
        self.pixel(x - 10, y - 6, (255, 255, 255))
        self.pixel(x - 10, y - 7, (255, 255, 255))
        self.pixel(x - 11, y - 4, (255, 255, 255))
        self.pixel(x - 12, y - 5, (255, 255, 255))
        self.pixel(x - 12, y - 3, (255, 255, 255))
        self.pixel(x - 13, y - 4, (255, 255, 255))
        self.pixel(x - 14, y - 4, (255, 255, 255))
        self.pixel(x - 14, y - 7, (255, 255, 255))
        self.pixel(x - 15, y - 7, (255, 255, 255))
        self.pixel(x - 16, y - 7, (255, 255, 255))
        self.pixel(x - 17, y - 6, (255, 255, 255))
        self.pixel(x - 18, y - 4, (255, 255, 255))
        self.pixel(x - 19, y - 2, (255, 255, 255))
        self.pixel(x - 19, y - 6, (255, 255, 255))
        self.pixel(x - 20, y - 4, (255, 255, 255))
        self.pixel(x - 20, y - 5, (255, 255, 255))
        self.pixel(x - 22, y - 3, (255, 255, 255))
        self.pixel(x - 22, y - 5, (255, 255, 255))
        self.pixel(x - 23, y - 3, (255, 255, 255))
        self.pixel(x - 23, y - 5, (255, 255, 255))
        self.pixel(x - 23, y - 6, (255, 255, 255))
        self.pixel(x - 24, y - 4, (255, 255, 255))
        self.pixel(x - 25, y - 2, (255, 255, 255))
        for i in range(20, 27):
            self.pixel(x - i, y - 1, (255, 255, 255))
        
        self.pixel(x - 27, y - 3, (255, 255, 255))
        self.pixel(x - 28, y - 3, (255, 255, 255))
        self.pixel(x - 28, y - 1, (255, 255, 255))
        self.pixel(x - 29, y - 3, (255, 255, 255))
        self.pixel(x - 29, y - 3, (255, 255, 255))        
        self.pixel(x - 31, y - 2, (255, 255, 255))
        self.pixel(x - 31, y - 3, (255, 255, 255))
        self.pixel(x - 31, y - 4, (255, 255, 255))        
        self.pixel(x - 33, y - 2, (255, 255, 255))
        self.pixel(x - 33, y - 6, (255, 255, 255))
        self.pixel(x - 34, y - 2, (255, 255, 255))
        self.pixel(x - 34, y - 3, (255, 255, 255))
        self.pixel(x - 34, y - 7, (255, 255, 255))
        self.pixel(x - 35, y - 5, (255, 255, 255))
        self.pixel(x - 35, y - 6, (255, 255, 255))
        self.pixel(x - 35, y - 7, (255, 255, 255))
        self.pixel(x - 36, y - 6, (255, 255, 255))
        self.pixel(x - 36, y - 7, (255, 255, 255))
        self.pixel(x - 36, y - 9, (255, 255, 255))
        self.pixel(x - 36, y - 10, (255, 255, 255))
        self.pixel(x - 37, y - 8, (255, 255, 255))
    
    def tub(self, x, y):
        self.pixel(x, y + 1, (255, 255, 255))
        self.pixel(x, y - 1, (255, 255, 255))
        self.pixel(x + 1, y, (255, 255, 255))
        self.pixel(x - 1, y, (255, 255, 255))
    
    def beacon(self, x, y):
        self.block(x, y)
        self.block(x + 2, y + 2)
    
    def cloverhead(self, x, y):
        self.pixel(x, y - 1, (255, 255, 255))
        self.pixel(x, y - 3, (255, 255, 255))
        
        self.pixel(x + 1, y - 4, (255, 255, 255))
        self.pixel(x + 1, y - 5, (255, 255, 255))
        self.pixel(x + 2, y - 1, (255, 255, 255))
        self.pixel(x + 2, y - 2, (255, 255, 255))
        self.pixel(x + 2, y - 4, (255, 255, 255))
        self.pixel(x + 3, y - 1, (255, 255, 255))
        self.pixel(x + 3, y - 4, (255, 255, 255))
        self.pixel(x + 4, y - 2, (255, 255, 255))
        self.pixel(x + 4, y - 3, (255, 255, 255))
        self.pixel(x - 1, y - 4, (255, 255, 255))
        self.pixel(x - 1, y - 5, (255, 255, 255))
        self.pixel(x - 2, y - 1, (255, 255, 255))
        self.pixel(x - 2, y - 2, (255, 255, 255))
        self.pixel(x - 2, y - 4, (255, 255, 255))
        self.pixel(x - 3, y - 1, (255, 255, 255))
        self.pixel(x - 3, y - 4, (255, 255, 255))
        self.pixel(x - 4, y - 2, (255, 255, 255))
        self.pixel(x - 4, y - 3, (255, 255, 255))
        
        self.pixel(x, y + 1, (255, 255, 255))
        self.pixel(x, y + 3, (255, 255, 255))
        
        self.pixel(x + 1, y + 4, (255, 255, 255))
        self.pixel(x + 1, y + 5, (255, 255, 255))
        self.pixel(x + 2, y + 1, (255, 255, 255))
        self.pixel(x + 2, y + 2, (255, 255, 255))
        self.pixel(x + 2, y + 4, (255, 255, 255))
        self.pixel(x + 3, y + 1, (255, 255, 255))
        self.pixel(x + 3, y + 4, (255, 255, 255))
        self.pixel(x + 4, y + 2, (255, 255, 255))
        self.pixel(x + 4, y + 3, (255, 255, 255))
        self.pixel(x - 1, y + 4, (255, 255, 255))
        self.pixel(x - 1, y + 5, (255, 255, 255))
        self.pixel(x - 2, y + 1, (255, 255, 255))
        self.pixel(x - 2, y + 2, (255, 255, 255))
        self.pixel(x - 2, y + 4, (255, 255, 255))
        self.pixel(x - 3, y + 1, (255, 255, 255))
        self.pixel(x - 3, y + 4, (255, 255, 255))
        self.pixel(x - 4, y + 2, (255, 255, 255))
        self.pixel(x - 4, y + 3, (255, 255, 255))
                               
pygame.init()
screen = pygame.display.set_mode((500, 500))

r = Life(screen)

r.ggg(50, 50)

r.ggg(150, 50)

r.snail(20, 250)

r.snail(60, 130)

r.snail(100, 100)

r.glider(10, 60)

r.faces(200, 300)

r.lwss(80, 400)

r.block(400, 10)

r.block(400, 400)

r.penta_decathlon_v(380, 320)

r.penta_decathlon_h(350, 350)

r.pulsar(400, 200)

r.pulsar(380, 180)

r.pulsar(350, 150)

r.blinker_h(250, 430)

r.blinker_v(250, 420)

r.snail_r(380, 480)

r.pulsar(400, 200)

r.penta_decathlon_v(320, 260)

r.beacon(485, 100)

r.cloverhead(200, 200)

r.hwss(20, 490)

r.hwss_r(400, 100)

r.hwss_r(410, 110)

r.hwss_r(420, 120)

r.pulsar(200, 380)

r.penta_decathlon_h(180, 370)

r.cloverhead(220, 180)

r.tub(220, 160)

r.penta_decathlon_v(300, 120)

r.lwss(20, 320)
r.lwss(50, 330)
r.hwss(80, 340)
r.lwss(50, 350)
r.lwss(20, 360)

r.snail_r(480, 440)

r.glider(80, 250)

r.glider_alt_2(90, 240)
r.glider_alt_2(80, 240)
r.glider_alt_2(100, 240)

r.glider_alt_1(250, 240)
r.glider_alt_1(260, 240)
r.glider_alt_1(270, 240)

counter = 0
while counter != 85:
    r.tub(random.randint(10, 170), random.randint(410, 475))
    counter += 1

r.pulsar(20, 200)
r.pulsar(40, 180)

counter = 0
while counter != 20:
    r.pulsar(random.randint(400, 490), random.randint(200, 400))
    counter += 1

# x = (220, 300), y = (250, 400)-------------------------------
counter = 0
while counter != 25:
    r.block(random.randint(220, 300), random.randint(250, 400))
    counter += 1

counter = 0
while counter != 8:
    r.blinker_h(random.randint(220, 300), random.randint(250, 400))
    counter += 1

counter = 0
while counter != 8:
    r.blinker_v(random.randint(220, 300), random.randint(250, 400))
    counter += 1
#-----------------------------------------------------------------
counter = 0
while counter != 15:
    r.cloverhead(random.randint(220, 350), random.randint(10, 100))
    counter += 1

counter = 0
while counter != 25:
    r.beacon(random.randint(220, 350), random.randint(10, 100))
    counter += 1

counter = 0
while counter != 25:
    r.block(random.randint(220, 350), random.randint(10, 100))
    counter += 1
#------------------------------------------------------------------
r.ggg(310, 200)
r.snail_r(350, 400)

while True:
    r.copy()
    r.clear()
    r.render()
    
    pygame.display.flip()
