from player import Player
import random

class EasyBot(Player):

    def __init__(self, playerCharacter: str, gameListReference: list) -> None:
        self.__init__(playerCharacter, "Easy Bot")
        self.gameListReference = gameListReference

    def getOption(self) -> int:

        positionsList = []
        maxIndex = -1

        for position in range(len(self.gameListReference)):
            if self.gameListReference[position] == " ":
                positionsList.append(position)
                maxIndex += 1
                
        chosenIndex = random.randint(0, maxIndex)
        chosenPosition = positionsList[chosenIndex]

        self.lastChosenPosition = chosenPosition

        return chosenPosition


class HardBot(Player):

    def __init__(self, playerCharacter: str, gameListReference: list) -> None:
        super().__init__(playerCharacter, "Hard Bot")
        self.gameListReference = gameListReference
        self.adjacentPositionsDict = {
                                        0: [(1, 2), (3, 6), (4, 8)],
                                        1: [(0, 2), (4, 7)],
                                        2: [(0, 1), (5, 8), (4, 6)],
                                        3: [(0, 6), (4, 5)],
                                        4: [(0, 8), (2, 6), (1, 7), (3, 5)],
                                        5: [(2, 8), (3, 4)],
                                        6: [(0, 3), (7, 8), (2, 4)],
                                        7: [(6, 8), (1, 4)],
                                        8: [(0, 4), (2, 5), (6, 7)]
                                    }

    def getOption(self) -> int:

        if self.lastChosenPosition != None :

            lastChosenPosition = self.lastChosenPosition

            lastChosenPosition -= 1

            adjacentPositions = self.adjacentPositionsDict.get(lastChosenPosition)

            for positionTuple in adjacentPositions:
                i, j = positionTuple
                if (self.gameListReference[i] == self.playerCharacter and self.gameListReference[j] == " "):
                    self.lastChosenPosition = j + 1
                    return j + 1
                elif (self.gameListReference[j] == self.playerCharacter and self.gameListReference[i] == " "):
                    self.lastChosenPosition = i + 1
                    return i + 1
                
            opponentCharacter = self.getOpponentCharacter()
                
            # returns an empty position in a row whose two positions are occupied by the opponent character
            for i in range(3):

                if (self.gameListReference[i*3] == self.gameListReference[i*3 + 1] == opponentCharacter 
                    and self.gameListReference[i*3 + 2] == " ") :

                    self.lastChosenPosition = i*3 + 2 + 1
                    return i*3 + 2 + 1
                
                elif (self.gameListReference[i*3] == self.gameListReference[i*3 + 2] == opponentCharacter 
                    and self.gameListReference[i*3 + 1] == " ") :

                    self.lastChosenPosition = i*3 + 1 + 1
                    return i*3 + 1 + 1
                
                elif  (self.gameListReference[i*3 + 1] == self.gameListReference[i*3 + 2] == opponentCharacter 
                    and self.gameListReference[i*3] == " ") :

                    self.lastChosenPosition = i*3 + 1
                    return i*3 + 1
                
            # returns an empty position in a column whose two positions are occupied by the opponent character
            for i in range(3):

                if (self.gameListReference[0 + i] == self.gameListReference[3 + i] == opponentCharacter 
                    and self.gameListReference[6 + i] == " ") :

                    self.lastChosenPosition = 6 + i + 1
                    return 6 + i + 1
                
                elif (self.gameListReference[0 + i] == self.gameListReference[6 + i] == opponentCharacter 
                    and self.gameListReference[3 + i] == " ") :

                    self.lastChosenPosition = 3 + i + 1
                    return 3 + i + 1
                
                elif  (self.gameListReference[3 + i] == self.gameListReference[6 + i] == opponentCharacter 
                    and self.gameListReference[0 + i] == " ") :

                    self.lastChosenPosition = 0 + i + 1
                    return 0 + i + 1
                
            #returns an empty position in the main diagonal if two positions in it are occupied by the opponent character 
            if (self.gameListReference[0] == self.gameListReference[4] == opponentCharacter 
                    and self.gameListReference[8] == " ") :

                    self.lastChosenPosition = 8 + 1
                    return 8 + 1
                
            elif (self.gameListReference[0] == self.gameListReference[8] == opponentCharacter 
                and self.gameListReference[4] == " ") :

                self.lastChosenPosition = 4 + 1
                return 4 + 1
            
            elif  (self.gameListReference[4] == self.gameListReference[8] == opponentCharacter 
                and self.gameListReference[0] == " ") :

                self.lastChosenPosition = 0 + 1
                return 0 + 1
            
            #returns an empty position in the anti diagonal if two positions in it are occupied by the opponent character 
            if (self.gameListReference[2] == self.gameListReference[4] == opponentCharacter 
                    and self.gameListReference[6] == " ") :

                    self.lastChosenPosition = 6 + 1
                    return 6 + 1
                
            elif (self.gameListReference[2] == self.gameListReference[6] == opponentCharacter 
                and self.gameListReference[4] == " ") :

                self.lastChosenPosition = 4 + 1
                return 4 + 1
            
            elif  (self.gameListReference[4] == self.gameListReference[6] == opponentCharacter 
                and self.gameListReference[2] == " ") :

                self.lastChosenPosition = 2 + 1
                return 2 + 1
            

                
            for positionTuple in adjacentPositions:
                    i, j = positionTuple
                    if (self.gameListReference[j] == " "):
                        self.lastChosenPosition = j + 1
                        return j + 1
                    elif (self.gameListReference[i] == " "):
                        self.lastChosenPosition = i + 1
                        return i + 1


        else :

            positionsList = []
            maxIndex = -1

            for position in range(len(self.gameListReference)):
                if self.gameListReference[position] == " ":
                    positionsList.append(position)
                    maxIndex += 1
 
            chosenIndex = random.randint(0, maxIndex)
            chosenPosition = positionsList[chosenIndex]

            self.lastChosenPosition = chosenPosition

            return chosenPosition

    def getOpponentCharacter(self):
        if self.playerCharacter == "X":
            return "O"
        else:
            return "X"