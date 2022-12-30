from abc import ABC, abstractclassmethod
from string import ascii_lowercase

FILE = ascii_lowercase[:8]
RANK = "".join(str(x) for x in range(1, 9))

class Piece(ABC):
    def __init__(self, position) -> None:
        self.position = position

    @abstractclassmethod
    def valid_move(self) -> list:
        pass

    @abstractclassmethod
    def move(self, new_pos: str):
        if new_pos in self.valid_move:
            self.position = new_pos

    @staticmethod
    def cell_validaty(pos: str):
        if pos[0] in FILE and pos[1] in RANK:
            return True
        return False    

class King(Piece):
    def valid_move(self) -> list:
        output = []
        file_index = FILE.find(self.position[0])

        for i in range(-1, 2):
            for j in range(-1, 2):
                valid_pos = ascii_lowercase[file_index + i] + str(int(self.position[1]) + j)

                if self.cell_validaty(valid_pos) and valid_pos != self.position:
                    output.append(valid_pos)
        
        return output

    def move(self, new_pos: str):
        super().move(new_pos)

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

# white = [
#     *[Pawn("b" + str(x)) for x in range(1, 9)],
#     Rooke(), Knight(), Bishop(), Queen(), King(), Bishop(), Knight(), Rooke()
# ]

if "__main__" == __name__:
    print(King("a1").valid_move())
