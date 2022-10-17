# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.

print('X, Y, Z, F')
for X in 0, 1:
    for Y in 0, 1:
        for Z in 0, 1:
            F = int(not (X and Y) or Z)
            print(X, Y, Z, F)
