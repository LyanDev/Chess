from abc import ABC, abstractclassmethod
from string import ascii_lowercase
import math

FILE = ascii_lowercase[:8]
RANK = "".join(str(x) for x in range(1, 9))

class Piece(ABC):
    def __init__(self, position) -> None:
        self.position = position

    def __str__(self):
        return self.__class__.__name__[0] + self.position
    
    @abstractclassmethod
    def valid_move(self) -> list:
        pass

    def move(self, new_pos: str):
        if new_pos in self.valid_move:
            self.position = new_pos

    @staticmethod
    def cell_validaty(pos: str):
        if pos[0] in FILE and pos[1:] in RANK:
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


class Queen(Piece):
    def valid_move(self):
        return Bishop(self.position).valid_move() + Rooke(self.position).valid_move()

class Bishop(Piece):
    def valid_move(self):
        output = []

        current_file_index = FILE.find(self.position[0])
        
        for file_index in range(8):
            if current_file_index == file_index:
                continue

            valid_pos_2 = FILE[file_index] + str(int(self.position[1]) - abs(current_file_index - file_index))
            valid_pos_1 = FILE[file_index] + str(int(self.position[1]) + abs(current_file_index - file_index))

            if self.cell_validaty(valid_pos_1):
                output.append(valid_pos_1)

            if self.cell_validaty(valid_pos_2):
                output.append(valid_pos_2)
        
        return output
        
class Knight(Piece):
    pass

class Rooke(Piece):
    def valid_move(self):
        output = []

        for file in FILE.replace(self.position[0], ""):
            output.append(file + self.position[1])
        
        for rank in RANK.replace(self.position[1], ""):
            output.append(self.position[0] + rank)

        return output

class Pawn(Piece):
    pass

# white = [
#     *[Pawn("b" + str(x)) for x in range(1, 9)],
#     Rooke(), Knight(), Bishop(), Queen(), King(), Bishop(), Knight(), Rooke()
# ]

if "__main__" == __name__:
    b = Queen("f6")
    print(b.valid_move())

