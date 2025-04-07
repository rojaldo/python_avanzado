
class TetrisPiece:
    def __init__(self, shape):
        self.shape = shape
        self.rotation = 0

    def rotate(self):
        pass

class LPiece(TetrisPiece):
    def __init__(self):
        super().__init__([
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0]
            
        ])
    def rotate(self):
        self.rotation = (self.rotation + 1) % 4
        if self.rotation == 0:
            self.shape = [
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 1, 0],
                [0, 0, 0, 0, 0]
            ]
        elif self.rotation == 1:
            self.shape = [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0]
            ]
        elif self.rotation == 2:
            self.shape = [
                [0, 0, 0, 0, 0],
                [0, 1, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0]
            ]
        elif self.rotation == 3:
            self.shape = [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]
            ]

class OPiece(TetrisPiece):
    def __init__(self):
        super().__init__([
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0],
            [0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0]
        ])

    def rotate(self):
        pass

class IPiece(TetrisPiece):

    def __init__(self):
        super().__init__([
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]])
    
    def rotate(self):
        self.rotation = (self.rotation + 1) % 2
        if self.rotation == 0:
            self.shape = [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]
            ]
        elif self.rotation == 1:
            self.shape = [
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0]
            ]

class TetrisPieceSingleton:
    ___instance: TetrisPiece = None

    def __init__(self):
        pass

    def createInstance(self,piece):
        if self.___instance is None:
            self.___instance = piece
        return self.___instance
    
class TetrisPieceFactory:
    def create_piece(self, piece_type) -> TetrisPiece:
        if piece_type == "L":
            return LPiece()
        elif piece_type == "O":
            return OPiece()
        elif piece_type == "I":
            return IPiece()
        else:
            raise ValueError("Unknown piece type")


if __name__ == "__main__":
    factory = TetrisPieceFactory()
    piece1 = factory.create_piece("L")
    piece2 = factory.create_piece("O")
    piece3 = factory.create_piece("I")
    
    print(piece1.shape)
    print(piece2.shape)
    print(piece3.shape)
    
    piece1.rotate()
    print(piece1.shape)


