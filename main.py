import pygame
import random
pygame.init()
cardWidth = 50
cardHeight = 75
screenWidth = 450
screenHeight = 800
red = (255, 35, 35)
green = (35, 255, 35)
blue = (35, 35, 255)
black = (0, 0, 0)
bg = pygame.Surface((screenWidth, screenHeight))
win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Ment Card Game")
# used to help set frame rate
clock = pygame.time.Clock()

# add a pass button that just puts zeros into proper list/tuples


def diceRoll():
    dice0 = random.randint(1, 5)
    dice1 = random.randint(1, 5)
    dice2 = random.randint(1, 5)
    dice3 = random.randint(1, 5)
    return dice0 + dice1 + dice2 + dice3


class player1:
    
    cardsInHand = []
    cardTypes = []
    cardsInPlayPower = []
    cardsInPlayPowerSum = sum(cardsInPlayPower)
    cardsInPlayType = []
    cardPosX = [40, 120, 200, 280, 360, 40, 120, 200, 280, 360]
    cardPosY = [600, 600, 600, 600, 600, 700, 700, 700, 700, 700]
    
    while len(cardTypes) < 10:
        dice = random.randint(1, 3)
        if dice == 1:
            cardTypes.append(red)
        if dice == 2:
            cardTypes.append(green)
        if dice == 3:
            cardTypes.append(blue)

    cardCounter = 0
    while cardCounter < 10:
        cardsInHand.append(diceRoll())
        cardCounter += 1

# this works for a tuple inside a list
# EXAMPLE player1.cardsInPlay = [(110, (1,2,3)),(120,(4,5,6)),(130,(7,8,9))]
# print(player1.cardsInPlay[0][1])
# OUTPUT: (1,2,3)


class computer:
    
    cardsInHand = []
    cardTypes = []
    cardsInPlayPower = []
    cardsInPlayPowerSum = sum(cardsInPlayPower)
    cardsInPlayType = []
    cardPosX = [40, 120, 200, 280, 360, 40, 120, 200, 280, 360]
    cardPosY = [25, 25, 25, 25, 25, 125, 125, 125, 125, 125]
    
    while len(cardTypes) < 10:
        dice = random.randint(1, 3)
        if dice == 1:
            cardTypes.append(red)
        if dice == 2:
            cardTypes.append(green)
        if dice == 3:
            cardTypes.append(blue)
    
    cardCounter = 0
    while cardCounter < 10:
        cardsInHand.append(diceRoll())
        cardCounter += 1

class gameState:
    turn = ['player1']
    cip_player1_posXindex = []
    cip_computer_posXindex = []


font = pygame.font.SysFont(None, 25)
def messageToScreen(msg, color, x, y):
    screen_text = font.render(msg, True, color)
    win.blit(screen_text, [x, y])


# shows totals in console, NOT NECESSARY
def addTotal():
    ans1 = 0
    for item in player1.cardsInHand:
        ans1 += item
    print('player1 total power: ', ans1)
    ans2 = 0
    for item in computer.cardsInHand:
        ans2 += item
    print('computer total power: ', ans2)


addTotal()


# redraws game window so there isn't a million of the same image, order matters
def redrawGameWindow():
    win.fill((65, 65, 65))
    # can use this for an image background
    # win.blit(bg, (0, 0))
    
    # Cards top row PLAYER CARDS
    # drawing the cards to screen
    for i in range(10):
        messagePosX = player1.cardPosX[i] + 10
        messagePosY = player1.cardPosY[i] + 25
        pygame.draw.rect(win, player1.cardTypes[i], (player1.cardPosX[i], player1.cardPosY[i], cardWidth, cardHeight))
        messageToScreen(str(player1.cardsInHand[i]), (0, 0, 0), messagePosX, messagePosY)
    
    # drawing computer's cards
    for i in range(10):
        # Computer Cards
        messagePosX = computer.cardPosX[i] + 10
        messagePosY = computer.cardPosY[i] + 25
        pygame.draw.rect(win, computer.cardTypes[i], (computer.cardPosX[i], computer.cardPosY[i], cardWidth, cardHeight))
        messageToScreen(str(computer.cardsInHand[i]), (0, 0, 0), messagePosX,  messagePosY)
    
    # Displays player1 total power in play
    messageToScreen(str(player1.cardsInPlayPowerSum), (255, 255, 255), 10, 435)
    # Displays computer total power in play
    messageToScreen(str(computer.cardsInPlayPowerSum), (255, 255, 255), 10, 340)

    # Pass option button
    messageToScreen('Pass Turn', (255, 255, 255), 10, 385)

    if len(gameState.turn) == 7:
        messageToScreen('Next Round', (255, 255, 255), 350, 385)
    
    pygame.display.update()


def typeCheckCalc():
    print('typeCheckCalc')
    if len(player1.cardsInPlayType) == len(computer.cardsInPlayType) and len(player1.cardsInPlayType) > 0:
        for i in range(len(player1.cardsInPlayType)):
            if player1.cardsInPlayType[i] == red and computer.cardsInPlayType[i] == blue:
                player1.cardsInPlayPowerSum -= 2
            elif player1.cardsInPlayType[i] == blue and computer.cardsInPlayType[i] == green:
                player1.cardsInPlayPowerSum -= 2
            elif player1.cardsInPlayType[i] == green and computer.cardsInPlayType[i] == red:
                player1.cardsInPlayPowerSum -= 2
        for i in range(len(computer.cardsInPlayType)):
            if computer.cardsInPlayType[i] == red and player1.cardsInPlayType[i] == blue:
                computer.cardsInPlayPowerSum -= 2
            elif computer.cardsInPlayType[i] == blue and player1.cardsInPlayType[i] == green:
                computer.cardsInPlayPowerSum -= 2
            elif computer.cardsInPlayType[i] == green and player1.cardsInPlayType[i] == red:
                computer.cardsInPlayPowerSum -= 2

run = True
# main game loop
while run:
    # frame rate 30/s
    clock.tick(30)

    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():

        # skip turn block of code
        if event.type == 5 and 10 < mouse_pos[0] < 90 and 385 < mouse_pos[1] < 400:
            if gameState.turn[-1] == 'player1':
                player1.cardsInPlayPower.append(0)
                player1.cardsInPlayType.append(black)
                gameState.turn.append('computer')
            elif gameState.turn[-1] == 'computer':
                computer.cardsInPlayPower.append(0)
                computer.cardsInPlayType.append(black)
                gameState.turn.append('player1')
            print('welcome to the skip club')

        # can use this to move played cards off the board and out of play
        if (
            event.type == 5
            and 350 < mouse_pos[0] < 445
            and 385 < mouse_pos[1] < 400
            and len(gameState.turn) == 7
        ):
            player1.cardsInPlayType = []
            player1.cardsInPlayPower = []
            player1.cardsInPlayPowerSum = 0
            computer.cardsInPlayType = []
            computer.cardsInPlayPower = []
            computer.cardsInPlayPowerSum = 0
            if gameState.turn[-1] == 'player1':
                gameState.turn = ['computer']
            elif gameState.turn[-1] == 'computer':
                gameState.turn = ['player1']
            for item in gameState.cip_player1_posXindex:
                player1.cardPosX[item] += 400
            for item in gameState.cip_computer_posXindex:
                computer.cardPosX[item] += 400
            gameState.cip_player1_posXindex = []
            gameState.cip_computer_posXindex = []
            print('registering next round click, clearing cards in play data')

        # dev check for seeing class data
        if event.type == 5 and mouse_pos[1] < 50:
            print('###')
            print('computer cardsInHand: ', computer.cardsInHand)
            print('computer cardTypes: ', computer.cardTypes)
            print('computer cardsInPlayPower: ', computer.cardsInPlayPower)
            print('computer cardsInPlayType: ', computer.cardsInPlayType)
            print('gameState turn: ', gameState.turn)
            print('gameState cip_computer_posXindex: ', gameState.cip_computer_posXindex)

        if event.type == 5 and mouse_pos[1] > 750:
            print('###')
            print('player1 cardsInHand: ', player1.cardsInHand)
            print('player1 cardTypes: ', player1.cardTypes)
            print('player1 cardsInPlayPower: ', player1.cardsInPlayPower)
            print('player1 cardsInPlayType: ', player1.cardsInPlayType)
            print('gameState turn: ', gameState.turn)
            print('gameState cip_player1_posXindex: ', gameState.cip_player1_posXindex)


        # 5 is for pygame.MOUSEBUTTONDOWN 6 is for pygame.MOUSEBUTTONUP
        for i in range(10):
            if (
                event.type == 5
                and player1.cardPosX[i] < mouse_pos[0] < player1.cardPosX[i] + cardWidth
                and player1.cardPosY[i] < mouse_pos[1] < player1.cardPosY[i] + cardHeight
                and gameState.turn[-1] == 'player1'
            ):
                if len(player1.cardsInPlayPower) == 0:
                    player1.cardsInPlayPower.append(player1.cardsInHand[i])
                    player1.cardsInPlayType.append(player1.cardTypes[i])
                    player1.cardPosX[i] = 120
                    player1.cardPosY[i] = 410
                    gameState.cip_player1_posXindex.append(i)
                    player1.cardsInPlayPowerSum = sum(player1.cardsInPlayPower)
                    typeCheckCalc()
                    gameState.turn.append('computer')
                    break
                if len(player1.cardsInPlayPower) == 1:
                    player1.cardsInPlayPower.append(player1.cardsInHand[i])
                    player1.cardsInPlayType.append(player1.cardTypes[i])
                    player1.cardPosX[i] = 200
                    player1.cardPosY[i] = 410
                    gameState.cip_player1_posXindex.append(i)
                    player1.cardsInPlayPowerSum = sum(player1.cardsInPlayPower)
                    typeCheckCalc()
                    gameState.turn.append('computer')
                    break
                if len(player1.cardsInPlayPower) == 2:
                    player1.cardsInPlayPower.append(player1.cardsInHand[i])
                    player1.cardsInPlayType.append(player1.cardTypes[i])
                    player1.cardPosX[i] = 280
                    player1.cardPosY[i] = 410
                    gameState.cip_player1_posXindex.append(i)
                    player1.cardsInPlayPowerSum = sum(player1.cardsInPlayPower)
                    typeCheckCalc()
                    gameState.turn.append('computer')
                    break
                else:
                    print('max cards played')



        for i in range(10):
            if (
                event.type == 5
                and computer.cardPosX[i] < mouse_pos[0] < computer.cardPosX[i] + cardWidth
                and computer.cardPosY[i] < mouse_pos[1] < computer.cardPosY[i] + cardHeight
                and gameState.turn[-1] == 'computer'
            ):
                if len(computer.cardsInPlayPower) == 0:
                    computer.cardsInPlayPower.append(computer.cardsInHand[i])
                    computer.cardsInPlayType.append(computer.cardTypes[i])
                    computer.cardPosX[i] = 120
                    computer.cardPosY[i] = 315
                    gameState.cip_computer_posXindex.append(i)
                    computer.cardsInPlayPowerSum = sum(computer.cardsInPlayPower)
                    typeCheckCalc()
                    gameState.turn.append('player1')
                    break
                if len(computer.cardsInPlayPower) == 1:
                    computer.cardsInPlayPower.append(computer.cardsInHand[i])
                    computer.cardsInPlayType.append(computer.cardTypes[i])
                    computer.cardPosX[i] = 200
                    computer.cardPosY[i] = 315
                    gameState.cip_computer_posXindex.append(i)
                    computer.cardsInPlayPowerSum = sum(computer.cardsInPlayPower)
                    typeCheckCalc()
                    gameState.turn.append('player1')
                    break
                if len(computer.cardsInPlayPower) == 2:
                    computer.cardsInPlayPower.append(computer.cardsInHand[i])
                    computer.cardsInPlayType.append(computer.cardTypes[i])
                    computer.cardPosX[i] = 280
                    computer.cardPosY[i] = 315
                    gameState.cip_computer_posXindex.append(i)
                    computer.cardsInPlayPowerSum = sum(computer.cardsInPlayPower)
                    typeCheckCalc()
                    gameState.turn.append('player1')
                    break
                else:
                    print('max cards played')


        if event.type == pygame.QUIT:
            run = False



            
    redrawGameWindow()
    
pygame.quit()
