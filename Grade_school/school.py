class School:
    def __init__(self):
        self.dicionar = dict()
        self.ok = list()
        self.all_grade = list()

    # Deve adicionar um aluno em seu grau
    def add_student(self, name, grade):
        lista = list()
        self.all_grade = lista_update(self.dicionar)
        if name in self.all_grade:
            self.ok.append(False)
        else:
            try:
                lista = self.dicionar[grade]
                lista.append(name)
            except KeyError:
                self.dicionar[grade] = [name]
            else:
                self.dicionar[grade] = sorted(lista)
            self.ok.append(True)

    # Deve retornar a lista inteira em ordem de grau e ordem alfabetica
    def roster(self):
        self.all_grade = lista_update(self.dicionar)
        return self.all_grade

    # Deve retorna a lista da grade selecionada em ordem alfabetica
    def grade(self, grade):
        try:
            return self.dicionar[grade]
        except KeyError:
            return list()

    # Deve retornar uma lista booleana de quando foi possível adicionar um aluno e quando não
    def added(self):
        return self.ok


def lista_update(dicionar):
    lista = list()
    for k in sorted(dicionar.keys()):
        lista += (dicionar[k])
    return lista
