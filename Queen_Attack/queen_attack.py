class Queen:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.validacion()

    def can_attack(self, another_queen):
        if another_queen.row == self.row and another_queen.column == self.column:
            raise ValueError("Invalid queen position: both queens in the same square")
        if another_queen.row == self.row or another_queen.column == self.column:
            return True
        return (another_queen.row, another_queen.column) in self.all_positions()

    def all_positions(self):
        lst = []
        x = self.row
        y = self.column
        for i in range(0, 8):
            lst.append((x - i, y + i))
            lst.append((x + i, y - i))
            lst.append((x - i, y - i))
            lst.append((x + i, y + i))
        new_lst = []
        for itens in lst:
            if itens[0] < 0 or itens[0] > 8 or itens[1] < 0 or itens[1] > 8:
                continue
            new_lst.append(itens)
        print(new_lst)
        return new_lst

    def validacion(self):
        if self.row < 0:
            raise ValueError("row not positive")
        if self.column < 0:
            raise ValueError("column not positive")
        if self.row > 7:
            raise ValueError("row not on board")
        if self.column > 7:
            raise ValueError("column not on board")


ana = Queen(4, 3).can_attack(Queen(3, 2))
print(ana)
