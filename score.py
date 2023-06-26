def setHighScore(nscore):
    file = open("highscore.txt", "w")
    file.writelines(str(nscore))
    file.close()
    
def getHighScore():
    file = open("highscore.txt", "r")
    return int(file.readline())