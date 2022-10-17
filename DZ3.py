# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

text1 = input('Введите первую строку ')
text2 = input('Введите вторую строку ')
countChar = 0

for i in text1:
    for j in text2:
        if j == i:
            countChar += 1
    print(f'символ {i} - {countChar} шт')
    countChar = 0
