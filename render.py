import pygame
from sys import exit
import snake
from score import setHighScore, getHighScore

SNAKECOLOR = "blue"
FOODCOLOR = "red"
MENUCOLOR = "white"
GAMEMENUCOLOR = "red"
BLANKCOLOR = "white"

class Render:
    renderStatus = 0 #0: menu       1: game
    renderGame = None
    oldplayer = None
    score = 0
    move = -1
    tickSpeed = 15 #The lower, the slower the game runs (try to keep low to reduce lag)
    frameRate = 2 #The lower the faster the game runs

    def __init__(self, tickspeed, framerate):
        self.tickSpeed = tickspeed
        self.frameRate = framerate
        ng = snake.Snake()
        self.renderGame = ng
        self.oldplayer = ng.player[0]

    def start(self, ):
        pygame.init()
        gamefont25 = pygame.font.SysFont("monospace", 25, )
        gamefont75 = pygame.font.SysFont("monospace", 75, bold=True)
        gamefont50 = pygame.font.SysFont("monospace", 50, bold=True )

        screen = pygame.display.set_mode( (500,550) )
        cover = pygame.Surface( (500,550) )
        cover.fill("black")

        pygame.display.set_caption("SNAKE")
        clock = pygame.time.Clock()
        self.highscore = getHighScore()

        playButtonText = gamefont50.render( "PLAY", 1, "green", "darkgrey" )
        playButtonRect = playButtonText.get_rect(center=(500/2, 550/2))
        
        firstRender = True
        count = 0
        while True:

            if self.renderGame.status == 3: # if failed
                        self.renderStatus = 0
                        self.renderGame.restart()
                        self.renderGame.score = 0
                        self.move = -1

            for event in pygame.event.get():
                    
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN and self.renderStatus == 0: # if in menu and clicked play, start game
                        
                        if playButtonRect.collidepoint(pygame.mouse.get_pos()):
                            self.renderStatus = 1
                    elif event.type == pygame.KEYDOWN: #change directions, so long as you are not turning in a 180
                        
                        if (pygame.K_RIGHT == event.key or pygame.K_d == event.key) and self.move != 3:
                            self.move = 1
                        elif (pygame.K_UP == event.key or pygame.K_w == event.key) and self.move != 2:
                            self.move = 0
                        elif (pygame.K_DOWN == event.key or pygame.K_s == event.key) and self.move != 0:
                            self.move = 2
                        elif (pygame.K_LEFT == event.key or pygame.K_a == event.key) and self.move != 1:
                            self.move = 3

            match self.renderStatus:

                case 0: # main menu
                    screen.blit(cover, (0,0))
                    snakeLabel = gamefont75.render( "SNAKE", 1, MENUCOLOR )
                    snakeLabelRect = snakeLabel.get_rect(center=(500/2, 57.5))
                    scoreLabel = gamefont25.render("SCORE: " + str(self.score), 1, MENUCOLOR)
                    scoreLabelRect = scoreLabel.get_rect(center=(500/2, 135))
                    highScoreLabel = gamefont25.render( "HIGH SCORE: " + str(self.highscore), 1, MENUCOLOR )
                    highScoreLabelRect = highScoreLabel.get_rect(center=(500/2, 175))
                    firstRender = True
                    
                    screen.blit(scoreLabel, scoreLabelRect)
                    screen.blit(snakeLabel, snakeLabelRect)
                    screen.blit(highScoreLabel, highScoreLabelRect)
                    screen.blit(playButtonText, playButtonRect)
                case 1: # show game

                    if firstRender:
                        firstRender = False
                        screen.blit(cover, (0,0))
                        for i in range(10):

                            for ii in range(10):
                                fillColor = BLANKCOLOR
                                
                                if self.renderGame.board[i][ii] == 1:
                                    fillColor = SNAKECOLOR
                                elif self.renderGame.board[i][ii] == 2:
                                    fillColor = FOODCOLOR
                                
                                newbox = pygame.Surface( (37,37) )
                                newbox.fill(fillColor)
                                screen.blit(newbox, (i*45+30, 550-69-(ii*45)) )
                    else:
                        firstRender = False
                        if count == self.frameRate:
                            self.score = self.renderGame.score
                            blackout = pygame.Surface( (500,60) )
                            screen.blit(blackout, (0,0))
                            self.oldplayer = self.renderGame.player[0]
                            count += 1
                            scoreLabel = gamefont25.render("Score: " + str(self.score), 1, GAMEMENUCOLOR)
                            highScoreLabel = gamefont25.render("High Score: " + str(self.highscore), 1, GAMEMENUCOLOR)
                            screen.blit(scoreLabel, ( (30,5) ))
                            screen.blit(highScoreLabel, ( (30,35) ))
                            self.renderGame.step(self.move)
                            removetail = pygame.Surface( (37,37) ) # remove old tail
                            removetail.fill("white")

                            if self.renderGame.status != 2:
                                screen.blit(removetail, (self.oldplayer[0]*45+30, 550-69-(self.oldplayer[1]*45)) )

                            if self.renderGame.score > self.highscore:
                                setHighScore(str(self.renderGame.score))
                                self.highscore = self.renderGame.score

                            coord = self.renderGame.player[len(self.renderGame.player)-1]
                            newbox = pygame.Surface( (37,37) )
                            newbox.fill(SNAKECOLOR)
                            screen.blit(newbox, (coord[0]*45+30, 550-69-(coord[1]*45)) )

                            foodbox = pygame.Surface( (37,37) )
                            foodbox.fill(FOODCOLOR)
                            screen.blit(foodbox, (self.renderGame.food[0]*45+30, 550-69-(self.renderGame.food[1]*45)) )
                            count = 1
                        else:
                            count += 1

            pygame.display.update()
            clock.tick(self.tickSpeed)