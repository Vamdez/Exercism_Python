class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.lista = self.matrix_string.split('\n')

    def row(self, index):
        self.matrix_int()
        return self.lista[index-1]

    def column(self, index):
        self.matrix_int()
        return [i[index-1] for i in self.lista]

    def matrix_int(self):
        lista_int = []
        temp2 = []
        for itens in self.lista:
            temp = itens.split()
            for i in temp:
                temp2.append(int(i))
            lista_int.append(temp2[:])
            temp.clear()
            temp2.clear()
        self.lista = lista_int[:]



