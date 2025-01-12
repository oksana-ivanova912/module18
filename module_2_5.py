def get_matrix(n, m, value):
    matrix = [] # создаем пустой список matrix
    for i in range(n): # внешний цикл для строк
        row = [] # создаем пустой список для строк
        for j in range(m): # внутренний цикл для столбцов
            row.append(value) # добавляем значение value в строку
        matrix.append(row) # добавляем строку в матрицу
    return matrix # возвращаем полученную матрицу
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)