
class TetrisPieceComposite:
    def __init__(self, shape):
        self.shape = shape

    def add_row(self, piece):
        self.shape.append(piece)
    
    def remove_row(self, piece):
        self.shape.remove(piece)

    def rotate(self):
        # Logic to rotate the composite piece
        pass

    def draw(self):
        for piece in self.pieces:
            piece.draw()

class TetrisBuilder:
    def __init__(self):
        self.pieces = []

    def add_piece(self, piece):
        self.pieces.append(piece)

    def remove_piece(self, piece):
        self.pieces.remove(piece)

    def build(self, shape):
        composite_piece = TetrisPieceComposite(shape)
        self.pieces.append(composite_piece)
        return composite_piece
    
# Example usage

if __name__ == "__main__":
    builder = TetrisBuilder()
    composite_piece = builder.build([
                [0, 1, 1, 1, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0]
            ])
    
    print("Composite piece created with shape:")
    for row in composite_piece.shape:
        print(row)