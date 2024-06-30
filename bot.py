from player import Player
import random

class EasyBot(Player):

    def __init__(self, playerCharacter: str, gameListReference: list) -> None:
        super().__init__(playerCharacter, "Easy Bot")
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

        super().lastChosenPosition = chosenPosition

        return chosenPosition