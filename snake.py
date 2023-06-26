import random

board = []
#  0: empty     1: player       2: food

class Snake:
    board = []
    score = 0
    food = []
    player = [ [0,0] ]
    head = [ 0,0 ]
    availSpots = []

    status = 0 # 0: normal      1: recieved food        3: dead     4: won

    def updateAvail(self, ):
        self.availSpots = []
        for i in range(10):

                for ii in range(10):
                    if (i, ii) not in self.player:
                        self.availSpots.append( [i,ii] )

    def clearboard(self, ):
        self.board = []
        for i in range(0,10):
            ys = []
            for ii in range(0,10):
                ys.append(0)
            self.board.append(ys)
        self.board[0][0] = 1
        self.updateAvail()

    def addfood(self, ):
        self.updateAvail()
        randi = random.randint(0,len(self.availSpots)-1)
        randx = self.availSpots[randi][0]
        randy = self.availSpots[randi][1]

        while True:
            inplayer = False
            for part in self.player:

                if part == [ randx, randy ]:
                    randi = random.randint(0,len(self.availSpots))
                    randx = self.availSpots[randi][0]
                    randy = self.availSpots[randi][1]
                    inplayer = True
            if not inplayer:
                break
            
        self.board[randx][randy] = 2
        self.food = [randx, randy]

    def __init__(self, ):
        self.clearboard()
        self.addfood()

    def restart(self, ):
        self.clearboard()
        self.addfood()
        self.score = 0
        self.player = [ [0,0] ]
        self.head = [ 0,0 ]
        self.status = 0
        

    def step(self, move): #0: up        1: right        2: down     3: left
        if move == 0:

            if [ self.head[0], self.head[1]+1] in self.player:
                self.status = 3
            else:
                self.head = [ self.head[0], self.head[1]+1]
                if self.head == self.food:
                    self.player.append(self.head)
                    self.status = 1
                    self.score += 1
                    self.board[ self.head[0]][self.head[1] ] = 1
                    self.addfood()
                elif self.head[1] > 9:
                    self.status = 3
                else:
                    self.status = 0
                    newplayer = []
                    for i in range(len(self.player)-1):
                        newplayer.append(self.player[i+1])
                    newplayer.append([ self.head[0], self.head[1] ])
                    self.board[self.head[0]][self.head[1]] = 1
                    self.board[self.player[0][0]][self.player[0][1]] = 0
                    self.player = newplayer
        elif move == 1:
            if [ self.head[0]+1, self.head[1]] in self.player:
                self.status = 3
            else:
                self.head = [ self.head[0]+1, self.head[1]]
                if self.head == self.food:
                    self.player.append(self.head)
                    self.status = 1
                    self.score += 1
                    self.board[ self.head[0]][self.head[1] ] = 1
                    self.addfood()
                elif self.head[0] > 9:
                    self.status = 3
                else:
                    self.status = 0
                    newplayer = []
                    for i in range(len(self.player)-1):
                        newplayer.append(self.player[i+1])
                    newplayer.append([ self.head[0], self.head[1]])
                    self.board[self.head[0]][self.head[1]] = 1
                    self.board[self.player[0][0]][self.player[0][1]] = 0
                    self.player = newplayer
        elif move == 2:
            if [ self.head[0], self.head[1]-1] in self.player:
                self.status = 3
            else:
                self.head = [ self.head[0], self.head[1]-1]
                if self.head == self.food:
                    self.player.append(self.head)
                    self.status = 1
                    self.score += 1
                    self.board[ self.head[0]][self.head[1] ] = 1
                    self.addfood()
                elif self.head[1] < 0:
                    self.status = 3
                else:
                    self.status = 0
                    newplayer = []
                    for i in range(len(self.player)-1):
                        newplayer.append(self.player[i+1])
                    newplayer.append([ self.head[0], self.head[1]])
                    self.board[self.head[0]][self.head[1]] = 1
                    self.board[self.player[0][0]][self.player[0][1]] = 0
                    self.player = newplayer
        elif move == 3:

            if [ self.head[0]-1, self.head[1]] in self.player:
                self.status = 3
            else:
                self.head = [ self.head[0]-1, self.head[1]]
                if self.head == self.food:
                    self.player.append(self.head)
                    self.status = 1
                    self.score += 1
                    self.board[ self.head[0]][self.head[1] ] = 1
                    self.addfood()
                elif self.head[0] < 0:
                    self.status = 3
                else:
                    self.status = 0
                    newplayer = []
                    for i in range(len(self.player)-1):
                        newplayer.append(self.player[i+1])
                    newplayer.append([ self.head[0], self.head[1]])
                    self.board[self.head[0]][self.head[1]] = 1
                    self.board[self.player[0][0]][self.player[0][1]] = 0
                    self.player = newplayer
