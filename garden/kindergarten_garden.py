import re

list_students = ('Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny',
                 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry')
types_plants = {
                'C': "Clover",
                'G': "Grass",
                'R': "Radishes",
                'V': "Violets"
                }


class Garden:
    def __init__(self, diagram, students=list_students):
        self.students = sorted(students)
        self.diagram = diagram.splitlines()

    def plants(self, name):
        count = self.students.index(name)
        lista = [re.findall('..', self.diagram[i]) for i in range(2)]
        resp = [lista[0][count] + lista[1][count]]
        return [types_plants[resp[0][i]] for i in range(4)]
