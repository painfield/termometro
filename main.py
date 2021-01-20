import pygame, sys
from pygame.locals import *

class Termometro():
    
    def __init__(self):
        self.skin = pygame.image.load('images/termo1.png')
        
class NumberInput():
    __value = 0
    __position = [0,0]
    __size = [0,0]
    
    def __init__(self,value=0):
        self.__font = pygame.font.SysFont('Arial',24)
        self.value(int(value))
        
    def on_event(self,event):
        strValue = str(self.value())

        if event.unicode.isdigit() and len(strValue)<9:
            strValue += event.unicode
            self.value(int(strValue))

        elif event.key is K_BACKSPACE:
            if len(strValue) > 1:
                strValue = strValue[:-1]
            else:
                strValue = '0'
            self.value(int(strValue))
            
        elif event.key is K_LEFT:
            pass
        
        elif event.key is K_RIGHT:
            pass
        
    def render(self):
        
        textBlock = self.__font.render('{}º'.format(self.__value), True, (74,74,74)) #convertimos valor a bitmap
        rect = textBlock.get_rect() #creamos rectángulo a partir del bloque de texto
        rect.left = self.__position[0] #definimos coordenada izquierda, que ha sido fijada en mainApp
        rect.top = self.__position[1] #definimos coordenada superior, que ha sido fijada en mainApp
        rect.size = self.__size #definimos tamaño, que ha sido fijado en mainApp
        
        return (rect,textBlock) #devolvemos el rectángulo ya definido y el render del texto
        
    def value(self, val=None):
        if val is None:
            return self.__value
        else:
            val = str(val)
            try:
                self.__value = int(val)
            except:
                pass
    
    def posX(self,val=None):
        if val is None:
            return self.__position[0]
        else:
            try:
                self.__position[0] = int[val]
            except:
                pass
            
    def posY(self,val=None):
        if val is None:
            return self.__position[1]
        else:
            try:
                self.__position[1] = int[val]
            except:
                pass
            
    def pos(self,val=None):
        if val == None:
            return self.__position
        else:
            try:
                self.__position = [int(val[0]),int(val[1])]
            except:
                pass
            
    def width(self,val=None):
        if val is None:
            return self.__size[0]
        else:
            try:
                self.__size[0] = int[val]
            except:
                pass
            
    def height(self,val=None):
        if val is None:
            return self.__size[1]
        else:
            try:
                self.__size[1] = int[val]
            except:
                pass
            
    def size(self,val=None):
        if val == None:
            return self.__size
        else:
            try:
                self.__size = [int(val[0]),int(val[1])]
            except:
                pass
            
class Selector():
    
    def __init__(self):
        self.celsius = True
        self.skin = pygame.image.load('images/posiC.png')
        
    def Celsius(self):
        return self.celsius
    
    def Switch(self):
        if self.celsius == True:
            self.celsius = False
            self.skin = pygame.image.load('images/posiF.png')
        else:
            self.celsius = True
            self.skin = pygame.image.load('images/posiC.png')
        
class mainApp():
    termometro = None
    entrada = None
    selector = None
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((290,415))
        pygame.display.set_caption('Termómetro')
        
        self.termometro = Termometro()
        self.entrada = NumberInput()
        self.entrada.pos((106,58))
        self.entrada.size((133,28))
        
        self.entrada.value(36)
        
        self.selector = Selector()
        
    def __on_close(self):
        pygame.quit()
        sys.exit()
    
    def start(self):
        while True:
            celsius = True
            for event in pygame.event.get():

                if event.type == QUIT:
                    self.__on_close()
                    
                elif event.type == MOUSEBUTTONDOWN:
                    self.selector.Switch()
                    if self.selector.Celsius():
                        self.entrada.value(int((self.entrada.value()-32)*5/9)) #convierte F a C
                        
                    else:
                        self.entrada.value(int((self.entrada.value()*9/5)+32)) #convierte C a F
                
                elif event.type == KEYDOWN:
                    self.entrada.on_event(event)
                        
                self.__screen.fill((244,236,203))
                self.__screen.blit(self.termometro.skin,(50,34)) #pintamos termómetro en su posición
                text = self.entrada.render() #obtenemos rectángulo y texto
                pygame.draw.rect(self.__screen,(255,255,255),text[0]) #creamos rectángulo blanco
                self.__screen.blit(text[1],self.entrada.pos()) #pintamos el render del texto
                self.__screen.blit(self.selector.skin,(106,120))
                pygame.display.flip() 
        
if __name__ == '__main__':
    pygame.font.init()
    app = mainApp()
    app.start()