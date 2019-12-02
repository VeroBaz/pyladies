# This program designs characters for a game "Tři dny v životě".
# The game enables a player to experience how it feels to be discriminated against.
# There are four available characters created according to the protected chracteristics - ethnicity, gender, age and disability.

class Character:
    # Parent class for all the characters: sets name, dignity and methods for getting and losing dignity points
    def __init__(self, name):
        self.name = name
        self.dignity = 100

    def get_dignity(self):
        # Returns the current amount of dignity points
        return self.dignity
    
    def update_dignity(self, points):
        # The character lose random amount of dignity points
        # self.dignity = self.get_dignity()
        self.dignity += points

class CharacterRoma(Character):
    # Character to play as Roma (ethnicity)
    def get_background(self):
        # Prints the character's background story
        print(f"{self.name} je Rom.\nJe mu 28 let a spolu se ženou a dvěma dětmi se stěhuje do nového města.\nZkus si tři dny v jeho životě.")

    def get_dignity(self):
        # Just for the sake of homework assignment
        print("I rewrite the method of the parent class.")

class CharacterWoman(Character):
    # Character to play as woman (gender)
    def get_background(self):
        # Prints the character's background story
        print(f"{self.name} je matka dvou dětí.\nJe jí 32 let a poslední čtyři roky byla na rodičovské dovolené.\nZkus si tři dny v jejím životě.")

    def update_dignity(self, points):
        # Just for the sake of homework assignment
        points = points + 10
        super().update_dignity(points)

class CharacterElderly(Character):
    # Character to play as elderly person (age)
    def get_background(self):
        # Prints the character's background story
        print(f"{self.name} bude mít příští rok 60 let.\nPracuje jako kuchař.\nV poslední době cítí, že se ho zaměstnavatel chce zbavit a najmout místo něj někoho mladšího.\nZkus si tři dny v jeho životě.")

class CharacterWheelchair(Character):
    # Character to play as a person using wheelchair (disability)
    def get_background(self):
        # Prints the character's background story
        print(f"{self.name} používá k pohybu vozík.\nVe čtrnácti letech totiž měla úraz na lyžích a ochrnuly jí obě nohy.\nNyní jí je 38 let a živí se jako překladatelka.\nZkus si tři dny v jejím životě.")
