class Player():

    def __init__(self, playerCharacter : str, playerName : str) -> None:
        self.playerCharacter = playerCharacter
        self.playerName = playerName
        self.lastChosenPosition = None

    def getCharacter():
        return self.playerCharacter 
    
    def __str__(self) -> str:
        return self.playerName
    
    def getOption(self) -> int:
        chosenOption = int(input("\nEnter the option here -> "))
        self.lastChosenPosition = chosenOption
        return chosenOption
    
    def getLastChosenPosition(self) -> int:
        return self.lastChosenPosition