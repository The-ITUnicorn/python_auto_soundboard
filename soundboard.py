from settings import *

pygame.init()
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('SoundBoards by Damien')

boardsarray = []
boardslist = os.listdir('boards')


class mainMenu():
    def __init__(self):

        boardslist = os.listdir('boards')
        for board in boardslist:
            boardsarray.append(board)
        butycoord = 50
        butxcoord = 50
        self.image = pygame.image.load('mainmenu.png')
        x = 0
        Running = True
        while Running:
            gameDisplay.blit(self.image, [0, 0])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            for board in boardsarray:
                if x > len(boardsarray) - 1:
                    x = 0
                    butycoord = 50
                    butxcoord = 50
                boardn = str(board) + 'board'
                boardn = Soundboard(board)

                if butxcoord > 650:
                    butxcoord = 50
                txtsize = 25 - len(boardn.name)
                if txtsize < 11:
                    txtsize = 10
                self.soundButtonWithText(butxcoord, butycoord, 100, 50, white, black, boardn.name, txtsize, boardn)
                butycoord += 100
                if butycoord > 450:
                    butycoord = 50
                    butxcoord += 150
                x += 1
            pygame.display.update()
    def soundButtonWithText(self, buttonXcoord, buttonYcoord, buttonLength, buttonHeight, buttonColor, textColor, text,
                            textSize, board):

        pygame.draw.rect(gameDisplay, buttonColor, (buttonXcoord, buttonYcoord, buttonLength, buttonHeight))
        smallText = pygame.font.Font("freesansbold.ttf", textSize)
        textSurf, textRect = text_objects(text, smallText, textColor)
        textRect.center = ((buttonXcoord + (buttonLength / 2)), (buttonYcoord + (buttonHeight / 2)))
        gameDisplay.blit(textSurf, textRect)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if mouse[0] > (buttonXcoord - 1) and mouse[0] < (buttonXcoord + buttonLength + 1) and mouse[1] > (
                buttonYcoord - 1) and mouse[1] < (buttonYcoord + buttonHeight + 1):
            print('mouse is in the position for ' + text + 'button')
            if click[0] == 1:
                print('you clicked on ' + text)
                board.play()


class Soundboard:
    def __init__(self, name):
        self.name = name
        self.dir = name
        self.imagefile = name + '.png'
        self.imagepath = os.path.join('boards', self.dir, self.imagefile)
        #self.imageopened = Image.open(self.imagepath)
        #self.imageresized = self.imageopened.resize((800,600))
        #self.imageresized.save(self.imagepath)
        self.image = pygame.image.load(self.imagepath)
        self.audioarray = []
        self.audiodir = os.path.join('boards', self.dir, 'audio')
        self.buttonarray = []
        for file in os.listdir(self.audiodir):
            self.audioarray.append(file)

    def play(self):

        gameDisplay.blit(self.image, [0, 0])
        pygame.display.update()
        butxcoord = 50
        butycoord = 50
        x = 0
        Running = True
        while Running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            for file in self.audioarray:
                if x > len(self.audioarray) - 1:
                    x = 0
                    butxcoord = 50
                    butycoord = 50
                file = self.audioarray[x]
                txtsize = 30 - len(file)
                if txtsize < 11:
                    txtsize = 10
                self.soundButtonWithText(butxcoord, butycoord, 100, 50, white, black, file[:-4], txtsize, file)
                if butycoord > 449:
                    butxcoord += 150
                if butxcoord > 650:
                    butxcoord = 50
                butycoord += 100
                if butycoord > 450:
                    butycoord = 50
                x += 1
            self.mainMenuButton(10, 525, 100, 50, black, white, "Main Menu", 15)
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if mouse[0] > (10 - 1) and mouse[0] < (10 + 100 + 1) and mouse[1] > (525 - 1) and mouse[1] < (525 + 50 + 1):
                if click[0] == 1:
                    print('you clicked on main menu')
                    Running = False
            pygame.display.update()


    def soundButtonWithText(self, buttonXcoord, buttonYcoord, buttonLength, buttonHeight, buttonColor, textColor, text,
                            textSize, soundfile):
        file = soundfile
        pygame.draw.rect(gameDisplay, buttonColor, (buttonXcoord, buttonYcoord, buttonLength, buttonHeight))
        smallText = pygame.font.Font("freesansbold.ttf", textSize)
        textSurf, textRect = text_objects(text, smallText, textColor)
        textRect.center = ((buttonXcoord + (buttonLength / 2)), (buttonYcoord + (buttonHeight / 2)))
        gameDisplay.blit(textSurf, textRect)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if mouse[0] > (buttonXcoord - 1) and mouse[0] < (buttonXcoord + buttonLength + 1) and mouse[1] > (
                buttonYcoord - 1) and mouse[1] < (buttonYcoord + buttonHeight + 1):
            if click[0] == 1:
                print('you clicked on ' + str(file))
                pygame.mixer.init()
                pygame.mixer.music.load(os.path.join(self.audiodir, file))
                pygame.mixer.music.play()
                pygame.event.wait()

    def mainMenuButton(self, buttonXcoord, buttonYcoord, buttonLength, buttonHeight, buttonColor, textColor, text, textSize):
        pygame.draw.rect(gameDisplay, buttonColor, (buttonXcoord, buttonYcoord, buttonLength, buttonHeight))
        smallText = pygame.font.Font("freesansbold.ttf", textSize)
        textSurf, textRect = text_objects(text, smallText, textColor)
        textRect.center = ((buttonXcoord + (buttonLength / 2)), (buttonYcoord + (buttonHeight / 2)))
        gameDisplay.blit(textSurf, textRect)

main1 = mainMenu
