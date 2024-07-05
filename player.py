class Player():
    """
    The Player class represents a player of the game.

    It stores information regarding the player of the game which is required at every stage of the game.

    This class has been created and developed by Ayman Zuhair Shashavali.
    """

    def __init__(self, playerCharacter : str, playerName : str) -> None:
        """
        This is the constructor method of the Player class that can be used to create an object of the
        Player.

        It initialises three class variables that are stored in the Player's object:

        1.playerCharacter :

        The playerCharacter variable stores the character that is chosen by the Player in the beginning of the game.

        2.playerName :

        The playerName variable stores the name of the Player.

        3.lastChosenPosition :

        The lastChosenPosition stores the most recent position that the Player chose while playing the game.
        """
        self.playerCharacter = playerCharacter
        self.playerName = playerName
        self.lastChosenPosition = None

    def getCharacter(self):
        """
        This method returns the character chosen by the Player.
        """
        return self.playerCharacter 
    
    def __str__(self) -> str:
        """
        This method returns the String Representation of the Player, which is, the name of the Player.
        """
        return self.playerName
    
    def getOption(self) -> int:
        """
        This method returns the option chosen by the Player from the options that are displayed during the Player's turn.

        It takes a position from the Player and sets the lastChosenPosition to the currently chosen position 
        and returns the position.
        """
        chosenOption = int(input("\nEnter the option here -> "))
        self.lastChosenPosition = chosenOption
        return chosenOption
    
    def getLastChosenPosition(self) -> int:
        """
        This method returns the position that was recently chosen by the Player.
        """
        return self.lastChosenPosition