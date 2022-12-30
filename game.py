from abc import ABC, abstractclassmethod
from string import ascii_lowercase

FILE = ascii_lowercase[:8]
RANK = list(range(1, 9))

class Piece(ABC):
    def __init__(self) -> None:
        self.position = str()

    @abstractclassmethod
    def valid_move(self) -> list:
        pass

    @abstractclassmethod
    def move(self, new_pos: str):
        if new_pos in self.valid_move:
            self.position = new_pos
    

class King(Piece):
    pass

class Queen(Piece):
    pass 

class Bishop(Piece):
    pass

class Knight(Piece):
    pass

class Rooke(Piece):
    pass

class Pawn(Piece):
    pass

white = [
    *[Pawn() for _ in range(8)],
    Rooke(), Knight(), Bishop(), Queen(), King(), Bishop(), Knight(), Rooke()
]

black = white.copy()

if "__main__" == __name__:
    pass
