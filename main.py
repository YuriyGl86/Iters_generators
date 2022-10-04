from iters_generators import Double_FlatIterator, double_flat_generator, flat_generator, FlatIterator

# Task 1. Итератор двумерного списка. #################################################
print('*'*20 + 'Task 1. Итератор двумерного списка' + '*'*20)
nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

for item in Double_FlatIterator(nested_list):
    print(item, end=' ')  #
print()

flat_list = [item for item in Double_FlatIterator(nested_list)]
print(flat_list)



# Task 2. Генератор двумерного списка отдельно. #############################################
print('\n' + '*'*20 + 'Task 2. Генератор двумерного списка' + '*'*20)
nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]

for item in double_flat_generator(nested_list):
    print(item, end=' ')
print()


#  Task 3. Итератор вложенных списков любой глубины вложенности. ##################################
print('\n' + '*'*20 + 'Task 3. Итератор вложенных списков любой глубины вложенности.' + '*'*20)
nested_list = [
    [[['a'], 'a222', 'a333'], 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]

for item in FlatIterator(nested_list):
    print(item, end=' ')  #
print()

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)



#  Task 4. Генератор вложенных списков любой глубины вложенности.################################
print('\n' + '*'*20 + 'Task 4. Генератор вложенных списков любой глубины вложенности.' + '*'*20)
nested_list = [
    [[['a'], 'a222', 'a333'], 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]
for item in flat_generator(nested_list):
    print(item, end=' ')
