import pygame
import random
pygame.init()
screenWidth = 450
screenHeight = 800
bg = pygame.Surface((screenWidth, screenHeight))
win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Ment Card Game")
#used to help set framerate
clock = pygame.time.Clock()

class player1:
    
    cardCounter = 0
    cardsInHand = []
    cardTypes = [(35,35,255),(255,35,35),(35,255,35),(35,255,35),(35,255,35)]
    inPlay0 = []
    inPlay1 = []
    inPlay2 = []
    
    def pickTypes(arg):
        player1.cardTypes.append(arg)        
    
    def diceRoll():
        dice0 = random.randint(1,10) * 10
        dice1 = random.randint(1,10) * 10
        #print(dice0)
        #print(dice1)
        return dice0 + dice1

    while cardCounter < 10:
        cardsInHand.append(diceRoll())
        #print(cardsInHand)
        cardCounter += 1
        
class computer:
    
    cardCounter = 0
    cardsInHand = []
    cardTypes = []
    
    def pickTypes(arg):
        computer.cardTypes.append(arg)        
    
    def diceRoll():
        dice0 = random.randint(1,10) * 10
        dice1 = random.randint(1,10) * 10
        #print(dice0)
        #print(dice1)
        return dice0 + dice1

    while cardCounter < 10:
        cardsInHand.append(diceRoll())
        #print(cardsInHand)
        cardCounter += 1

print(len(player1.cardTypes))
print(computer.cardsInHand)

font = pygame.font.SysFont(None, 25)

def messageToScreen(msg,color,x,y):
    screen_text = font.render(msg, True, color)
    win.blit(screen_text, [x, y])

#redraws game window so there isn't a million of the same image, order matters
def redrawGameWindow():
    win.fill((20,20,20))
    
    #can use this for an image background
    #win.blit(bg, (0, 0))
    
    #Cards bottom row PLAYER CARDS
    pygame.draw.rect(win, player1.cardTypes[0], (40, 600, 50, 75))
    messageToScreen(str(player1.cardsInHand[0]), (0,0,0), 50, 625)
    pygame.draw.rect(win, player1.cardTypes[1], (120, 600, 50, 75))
    messageToScreen(str(player1.cardsInHand[1]), (0,0,0), 130, 625)
    pygame.draw.rect(win, player1.cardTypes[2], (200, 600, 50, 75))
    messageToScreen(str(player1.cardsInHand[2]), (0,0,0), 210, 625)
    pygame.draw.rect(win, player1.cardTypes[3], (280, 600, 50, 75))
    messageToScreen(str(player1.cardsInHand[3]), (0,0,0), 290, 625)
    pygame.draw.rect(win, player1.cardTypes[4], (360, 600, 50, 75))
    messageToScreen(str(player1.cardsInHand[4]), (0,0,0), 370, 625)
    #on top of those
    pygame.draw.rect(win, (150,150,150), (40, 700, 50, 75))
    messageToScreen(str(player1.cardsInHand[5]), (0,0,0), 50, 725)
    pygame.draw.rect(win, (150,150,150), (120, 700, 50, 75))
    messageToScreen(str(player1.cardsInHand[6]), (0,0,0), 130, 725)
    pygame.draw.rect(win, (150,150,150), (200, 700, 50, 75))
    messageToScreen(str(player1.cardsInHand[7]), (0,0,0), 210, 725)
    pygame.draw.rect(win, (150,150,150), (280, 700, 50, 75))
    messageToScreen(str(player1.cardsInHand[8]), (0,0,0), 290, 725)
    pygame.draw.rect(win, (150,150,150), (360, 700, 50, 75))
    messageToScreen(str(player1.cardsInHand[9]), (0,0,0), 370, 725)
    
    #Computer Cards
    pygame.draw.rect(win, (250,250,150), (40, 25, 50, 75))
    messageToScreen(str(computer.cardsInHand[0]), (0,0,0), 50,  50)
    pygame.draw.rect(win, (250,250,150), (120, 25, 50, 75))
    messageToScreen(str(computer.cardsInHand[1]), (0,0,0), 130,  50)
    pygame.draw.rect(win, (250,250,150), (200, 25, 50, 75))
    messageToScreen(str(computer.cardsInHand[2]), (0,0,0), 210,  50)
    pygame.draw.rect(win, (250,250,150), (280, 25, 50, 75))
    messageToScreen(str(computer.cardsInHand[3]), (0,0,0), 290,  50)
    pygame.draw.rect(win, (250,250,150), (360, 25, 50, 75))
    messageToScreen(str(computer.cardsInHand[4]), (0,0,0), 370,  50)
    #below those    
    pygame.draw.rect(win, (250,250,150), (40, 125, 50, 75))
    messageToScreen(str(computer.cardsInHand[5]), (0,0,0), 50,  150)
    pygame.draw.rect(win, (250,250,150), (120, 125, 50, 75))
    messageToScreen(str(computer.cardsInHand[6]), (0,0,0), 130,  150)
    pygame.draw.rect(win, (250,250,150), (200, 125, 50, 75))
    messageToScreen(str(computer.cardsInHand[7]), (0,0,0), 210,  150)
    pygame.draw.rect(win, (250,250,150), (280, 125, 50, 75))
    messageToScreen(str(computer.cardsInHand[8]), (0,0,0), 290,  150)
    pygame.draw.rect(win, (250,250,150), (360, 125, 50, 75))
    messageToScreen(str(computer.cardsInHand[9]), (0,0,0), 370,  150)
    
    pygame.display.update()
    
run = True
#main game loop
while run:
    #frame rate 30/s  ### commented out for weird timing
    clock.tick(30)  
    
    for event in pygame.event.get():
        
        mouse_pos = pygame.mouse.get_pos()
        print(event)
        #5 is for MouseButtonDown
        if event.type == 5 and mouse_pos[0] > 40 and mouse_pos[0] < 90 and mouse_pos[1] > 600 and mouse_pos[1] < 675:
        #if pygame.mouse.get_pressed()[0] and mouse_pos[0] > 40 and mouse_pos[0] < 90 and mouse_pos[1] > 600 and mouse_pos[1] < 675:
            print('triggered')
            player1.cardTypes[0] = (150,150,150) 
        
        if event.type == pygame.QUIT:
            run = False
            
    redrawGameWindow()
    
pygame.quit()