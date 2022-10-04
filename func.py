# Task 1. Итератор и генератор. 2 в 1.
class FlatIterator2:
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        for i in range(len(self.lst)):
            for j in range(len(self.lst[i])):
                yield self.lst[i][j]


#  Task 2. Генератор двумерного списка отдельно.
def flat_generator2(lst):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            yield lst[i][j]


#  Task 4. Генератор вложенных списков дюбой глубины вложенности.
def flat_generator(lst):
    for i in lst:
        if isinstance(i, list):
            for j in flat_generator(i):
                yield j
        else:
            yield i
