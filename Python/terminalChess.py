
#######################

# Made by Philip Hoel

####################

# Coordinates are reverse
# regular vector (x,y) is thus (y,x)
# because of the reverse print in double for loop

class King:

    counter = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        King.counter += 1
        self.name = f"K{King.counter}"

    def move(self,x1,y1):
        
        if abs(self.x - x1) > 1 or abs(self.y - y1) > 1:
            return False

        if self.x > 8 or self.x < 0:
            return False

        if self.y > 8 or self.y < 0:
            return False

        self.x = x1
        self.y = y1
        return True



class Queen:

    counter = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Queen.counter += 1
        self.name = f"D{Queen.counter}"

    def move(self,x1,y1):

        # define illegal moves

        if self.x > 8 or self.x < 0:
            return False

        if self.y > 8 or self.y < 0:
            return False

        self.x = x1
        self.y = y1
        return True

class Bishop:

    counter = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Bishop.counter += 1
        self.name = f"P{Bishop.counter}"

    def move(self,x1,y1):

        # define illegal moves

        if self.x > 8 or self.x < 0:
            return False

        if self.y > 8 or self.y < 0:
            return False

        self.x = x1
        self.y = y1
        return True

class Knight:

    counter = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Knight.counter += 1
        self.name = f"R{Knight.counter}"

    def move(self,x1,y1):

        if abs(self.x - x1) > 2 or abs(self.y - y1) > 2:
            print("hei")
            return False

        if (abs(self.x - x1) == 2 and abs(self.y - y1) != 1) or (abs(self.x - x1) == 1 and abs(self.y - y1) != 2):
            #print("hei")
            return False

        if self.x > 8 or self.x < 0:
            #print("hei")
            return False

        if self.y > 8 or self.y < 0:
            #print("hei")
            return False

        self.x = x1
        self.y = y1
        return True

class Rook:

    counter = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Rook.counter += 1
        self.name = f"T{Rook.counter}"

    def move(self,x1,y1):

        if self.x != x1 and self.y != y1:
            return False

        if self.x > 8 or self.x < 0:
            return False

        if self.y > 8 or self.y < 0:
            return False

        self.x = x1
        self.y = y1
        return True

class Pawn:

    counter = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Pawn.counter += 1
        self.name = f"B{Pawn.counter}"

    def attackable(self):
        return False

    def move(self,x1,y1):

        if self.x != x1 and self.attackable() == False:
            return False

        if self.x > 8 or self.x < 0:
            return False

        if self.y > 8 or self.y < 0:
            return False

        self.x = x1
        self.y = y1
        return True

class Board:

    def __init__(self):
        self.color1 = "0;95"
        self.color2 = "0;92"
        self.start_code1 = f"\033[{self.color1}m"
        self.start_code2 = f"\033[{self.color2}m"
        self.end_code = "\033[0m"
        self.alfa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.coordianteMap = {}

        self.purple = {(5,1) : King(5,1), (4,1) : Queen(4,1), (3,1) : Bishop(3,1), (6,1) : Bishop(6,1), (2,1) : Knight(2,1), (7,1) : Knight(7,1), (1,1) : Rook(1,1), (8,1) : Rook(8,1),
                      (1,2) : Pawn(1,2), (2,2) : Pawn(2,2), (3,2) : Pawn(3,2), (4,2) : Pawn(4,2), (5,2) : Pawn(5,2), (6,2) : Pawn(6,2), (7,2) : Pawn(7,2), (8,2) : Pawn(8,2)}

        self.green = {(5,8) : King(5,8), (4,8) : Queen(4,8), (3,8) : Bishop(3,8), (6,8) : Bishop(6,8), (2,8) : Knight(2,8), (7,8) : Knight(7,8), (1,8) : Rook(1,8), (8,8) : Rook(8,8),
                      (1,7) : Pawn(1,7), (2,7) : Pawn(2,7), (3,7) : Pawn(3,7), (4,7) : Pawn(4,7), (5,7) : Pawn(5,7), (6,7) : Pawn(6,7), (7,7) : Pawn(7,7), (8,7) : Pawn(8,7)}
        self.board = {}
        for i in range(1,9):
            for j in range(1, 9):
                if j == 8:
                    self.board[(i,j)] = "|   |\n"
                else:
                    self.board[(i,j)] = "|   |"
                self.coordianteMap[f'{self.alfa[i-1]}{j}'] = (i,j)

        
    def updateBoard(self, lstP=None, lstG=None):
        if lstP is not None:
            self.purple = lstP

        if lstG is not None:
            self.green = lstG

        for i in range(1,9):
            for j in range(1, 9):
                if j == 8:
                    self.board[(i,j)] = "|   |\n"
                else:
                    self.board[(i,j)] = "|   |"

        for key in self.purple:
            if key[0] == 8:
                self.board[(key[1],key[0])] = f"| {self.start_code1}X{self.end_code} |\n"
            else:
                self.board[(key[1],key[0])] = f"| {self.start_code1}X{self.end_code} |"

        for key in self.green:
            if key[0] == 8:
                self.board[(key[1],key[0])] = f"| {self.start_code2}O{self.end_code} |\n"
            else:
                self.board[(key[1],key[0])] = f"| {self.start_code2}O{self.end_code} |"


    def printBoard(self):
        #print("    a    b    c    d    e    f    g    h")
        print("    1    2    3    4    5    6    7    8")
        print("   ____ ____ ____ ____ ____ ____ ____ ____")
        for i in range(1, 9):
            print(f"{i} ", end="")
            for j in range(1, 9):      
                print(self.board[(i,j)], end="")
            print("   ---- ---- ---- ---- ---- ---- ---- ---- ")
        print("   ----------------------------------------")

        print()
        print()

class Player:

    def __init__(self, a):
        self.pieces = a

    
    def makeAMove(self):

        aString = input("Enter coordinates from and to: ")
        x, y, newX, newY = aString.split()
        x = int(x)
        y = int(y)
        newX = int(newX)
        newY = int(newY)
        
        BOOL = self.pieces[(x,y)].move(newX,newY)
        if not BOOL:
            print(f"Illegal Move for {self.pieces[(x,y)].name}, try again!")
            self.makeAMove()
        else:
            self.pieces[(newX,newY)] = self.pieces.pop((x,y))

    def printPieces(self):
        for key in self.pieces:
            print(f"Name: {self.pieces[key].name}", end=" ")
            print(f"Coord: ({self.pieces[key].x},{self.pieces[key].y})", end="  ||  ")
            
        print()
    


def openingSeq():
    print("K = Konge/King")
    print("D = Dronning/Queen")
    print("P = Prest/Bishop")
    print("R = Ridder/Knight")
    print("T = Tårn/Rook")
    print("B = Bonde/Pawn")
    print()

    print("For more than one piece, left = 1 and right = 2")
    print("Example Bishop on left = P1 and Bishop on right = P2")

    print("Purple = White - Player 1")
    print("Green = Black - Player 2")
    print()
    print()
                    
if __name__ == "__main__":

    openingSeq()

    myBoard = Board()
    myBoard.updateBoard()
    myBoard.printBoard()
    player1 = Player(myBoard.purple)
    player2 = Player(myBoard.green)
    
    
    #Game loop
    breakingVar = True
    while breakingVar:

        player1.printPieces()
        player1.makeAMove()
        
        myBoard.updateBoard(lstP=player1.pieces)
        myBoard.printBoard()

        # Create collision function

        player2.printPieces()
        player2.makeAMove()
        
        myBoard.updateBoard(lstG=player2.pieces)
        myBoard.printBoard()

    