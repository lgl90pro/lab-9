import numpy as np # імпортуємо необіхдні бібліотеки і функції з них
from random import randint
from time import time

def main_function(): # задаємо головну фунцію, де користувач буде вводити чи генерувати масив, і обирати метод сортування
    global arr # задаємо глобальний масив, щоб його "бачили" інші функції
    while True: # створюємо умову для зациклення, якщо користувач вводить невірні дані
        question = input('Ви бажаєте самостійно ввести числа в масив (1) чи згенерувати (2) ?\n') # питаємо
        if (question == '1'): # самостійно вводимо числа в масив
            while True:
                try:
                    n = int(input('Введіть кількість елементів масиву (до 30): '))
                    if (n > 30 or n < 1): # кількість елементів може бути від 1 до 30
                        print('Не більше 30 і не менше 1!\n')
                        continue
                    break
                except ValueError:
                    print('Ви можете ввести лише цілі числа від 0 до 30.\n') # помилка
            arr = np.zeros(n, dtype = int) # ініціалізуємо масив нулями
            for i in range(n):
                while True:
                    try:
                        arr[i] = int(input(f'arr[{i}] = ')) # заповнюємо кожний елемент
                        break
                    except ValueError:
                        print('Введіть лише ціле число!\n') # помилка
        elif (question == '2'): # генеруємо 10 000 чисел (для кращої перевірки часу)
            n = 10000
            arr = np.zeros(n, dtype=int)
            for i in range(n):
                arr[i] = randint(0, 1000) # рандомно заповнюємо кожний елемент числом від 0 до 1000
        else:
            print('Введіть лише 1 або 2!\n') # інакше - знову питаємо користувача
            continue
        break
    print (f'\nВихідний масив: {arr}.\n') # виводимо вихідний масив
    while True:
        question = input('Оберіть метод сортування: \n1) бульбашкою;\n2) вибором;\n3) простими вставками;\n' # обираємо метод сортування
              '4) перемішуванням\n5) сортування Шелла;\n6) пірамідальне.\n')
        if (question == '1'):
            bubbleSort(arr)
        elif (question == '2'):
            selectionSort(arr)
        elif (question == '3'):
            insertionSort(arr)
        elif (question == '4'):
            cocktailSort(arr)
        elif (question == '5'):
            shellSort(arr)
        elif (question == '6'):
            heapSort(arr)
        else:
            print('Введіть ваш вибір цифрою (від 1 до 6).\n') # інакше - знову питаємо
            continue
        break

def bubbleSort(arr): # бульбашкове (простими обмінами)
    comparison = 0 # ініціалізуємо лічильник порівнянь
    replacement = 0 # ініціалізуємо лічильник обмінів
    n = len(arr) # визначаємо довжину масиву
    while True:
        question = input('Сортувати за зростанням (1) чи спаданням (2) ?\n') # питаємо
        start = time() # початок відліку часу виконнаня програми
        if (question == '1'): # сортування за зростанням
            for i in range(n): # зовнішній цикл для проходження по масиву
                flag = False # прапор для оптимізації сортування
                for j in range(0, n - i - 1): # внутрішній цикл
                    if arr[j] > arr[j + 1]: # якщо наступний елемент масиву менший за попередній
                        arr[j], arr[j + 1] = arr[j + 1], arr[j] # то міняємо їх місцями
                        replacement += 1 # +1 до обміну
                        flag = True # змінюємо прапор на правду
                    comparison += 1 # +1 до кількості перестановок
                if flag == False: # знінюємо прапор на хибу
                    break
        elif (question == '2'): # все те ж, що і за зростанням, лише змінюємо знак рівності в іншу сторону
            for i in range(n):
                flag = False
                for j in range(0, n - i - 1):
                    if arr[j] < arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        replacement += 1
                        flag = True
                    comparison += 1
                if flag == False:
                    break
        else:
            print('Введіть лише 1 або 2!\n') # інакше - знову питаємо
            continue
        break

    stop = time() # кінець відліку часу роботи програми
    print(f'\nВідсортований масив: {arr}.\n') # виводимо відсортований масив і дані по ньому
    print(f'Кількість порівнянь: {comparison}.')
    print(f'Кількість обмінів: {replacement}.')
    print(f'Затрачений час: {stop - start}.')
    print('____________________________________________________________________________________________________')

def selectionSort(arr): # сортування вибором
    comparison = 0
    replacement = 0
    n = len(arr)
    while True:
        question = input('Сортувати за зростанням (1) чи спаданням (2) ?\n')
        start = time()
        if (question == '1'):
            for i in range(n): # зовнішній цикл
                min = i # визначаємо мінімальний елемент, і перевіряємо з кожним наступним
                for j in range(i + 1, n): # внутрішній цикл
                    comparison += 1
                    if arr[min] > arr[j]:
                        min = j # якщо знаходимо менший елемент, робимо його мінімальним
                arr[i], arr[min] = arr[min], arr[i] # ставимо мінімальний елемент на позицію і-го
                replacement += 1
        elif (question == '2'):
            for i in range(n):
                min = i
                for j in range(i + 1, n):
                    comparison += 1
                    if arr[min] < arr[j]:
                        min = j
                arr[i], arr[min] = arr[min], arr[i]
                replacement += 1
        else:
            print('Введіть лише 1 або 2!\n')
            continue
        break

    stop = time()
    print(f'\nВідсортований масив: {arr}.\n')
    print(f'Кількість порівнянь: {comparison}.')
    print(f'Кількість обмінів: {replacement}.')
    print(f'Затрачений час: {stop - start}.')
    print('____________________________________________________________________________________________________')

def insertionSort(arr): # сортування простими вставками
    comparison = 0
    replacement = 0
    n = len(arr)
    while True:
        question = input('Сортувати за зростанням (1) чи спаданням (2) ?\n')
        start = time()
        if (question == '1'):
            for i in range(1, n): # проходимось по масиву
                j = i - 1 # ініціалізуємо j
                key = arr[i] # робимо і-тий елемент ключовим
                comparison += 2
                while arr[j] > key and j >= 0: # якщо елемент з індексом j більший за ключовий і j більше рівне нуля
                    comparison += 2
                    arr[j + 1] = arr[j] # то елемент правіший за елемент з індексом j стає йому рівний
                    replacement += 1
                    j -= 1 # ідемо в протилежну сторону
                arr[j + 1] = key # елемент з індексом j+1 стає рівний ключовому
                replacement += 1
        elif (question == '2'):
            for i in range(1, n):
                j = i - 1
                key = arr[i]
                comparison += 2
                while arr[j] < key and j >= 0:
                    comparison += 2
                    arr[j + 1] = arr[j]
                    replacement += 1
                    j -= 1
                arr[j + 1] = key
                replacement += 1
        else:
            print('Введіть лише 1 або 2!\n')
            continue
        break

    stop = time()
    print(f'\nВідсортований масив: {arr}.\n')
    print(f'Кількість порівнянь: {comparison}.')
    print(f'Кількість обмінів: {replacement}.')
    print(f'Затрачений час: {stop - start}.')
    print('____________________________________________________________________________________________________')

def cocktailSort(arr): # сортування перемішування
    comparison = 0
    replacement = 0
    n = len(arr)
    while True:
        question = input('Сортувати за зростанням (1) чи спаданням (2) ?\n')
        start = time()
        if (question == '1'): # сортування дуже схоже до бульбашкового, але тепер після проходження масиву
            flag = True       # цикл іде з кінця в початок, тому вводяться змінні beginning i end
            beginning = 0
            end = n - 1
            while (flag == True):
                flag = False
                for i in range(beginning, end):
                    comparison += 1
                    if (arr[i] > arr[i + 1]):
                        arr[i], arr[i + 1] = arr[i + 1], arr[i]
                        replacement += 1
                        flag = True
                if (flag == False):
                    break
                flag = False
                end = end - 1
                for i in range(end - 1, beginning - 1, -1):
                    comparison += 1
                    if (arr[i] > arr[i + 1]):
                        arr[i], arr[i + 1] = arr[i + 1], arr[i]
                        replacement += 1
                        flag = True
                beginning = beginning + 1
        elif (question == '2'):
            flag = True
            beginning = 0
            end = n - 1
            while (flag == True):
                flag = False
                for i in range(beginning, end):
                    comparison += 1
                    if (arr[i] < arr[i + 1]):
                        arr[i], arr[i + 1] = arr[i + 1], arr[i]
                        replacement += 1
                        flag = True
                if (flag == False):
                    break
                flag = False
                end = end - 1
                for i in range(end - 1, beginning - 1, -1):
                    comparison += 1
                    if (arr[i] < arr[i + 1]):
                        arr[i], arr[i + 1] = arr[i + 1], arr[i]
                        replacement += 1
                        flag = True
                beginning = beginning + 1
        else:
            print('Введіть лише 1 або 2!\n')
            continue
        break

    stop = time()
    print(f'\nВідсортований масив: {arr}.\n')
    print(f'Кількість порівнянь: {comparison}.')
    print(f'Кількість обмінів: {replacement}.')
    print(f'Затрачений час: {stop - start}.')
    print('____________________________________________________________________________________________________')

def shellSort(arr): # сортування Шелла - схоже до сортування простими вставка: сортуємо вставкою
    comparison = 0  # підгрупи елементів, але тепер в підгрупі вони йдуть не в ряд, а рівномірно вибираються з деякою дельтою за індексом,
    replacement = 0 # тому вводимо змінній gap та temp
    n = len(arr)
    while True:
        question = input('Сортувати за зростанням (1) чи спаданням (2) ?\n')
        start = time()
        if (question == '1'):
            gap = n // 2
            while gap > 0:
                for i in range(gap, n):
                    temp = arr[i]
                    j = i
                    comparison += 2
                    while j >= gap and arr[j - gap] > temp:
                        arr[j] = arr[j - gap]
                        replacement += 1
                        j -= gap
                    arr[j] = temp
                gap //= 2
        elif (question == '2'):
            gap = n // 2
            while gap > 0:
                for i in range(gap, n):
                    temp = arr[i]
                    j = i
                    comparison += 2
                    while j >= gap and arr[j - gap] < temp:
                        arr[j] = arr[j - gap]
                        replacement += 1
                        j -= gap
                    arr[j] = temp
                gap //= 2
        else:
            print('Введіть лише 1 або 2!\n')
            continue
        break

    stop = time()
    print(f'\nВідсортований масив: {arr}.\n')
    print(f'Кількість порівнянь: {comparison}.')
    print(f'Кількість обмінів: {replacement}.')
    print(f'Затрачений час: {stop - start}.')
    print('____________________________________________________________________________________________________')

def heapSort(arr): # пірамідальне сортування: шукаємо максимальний елемент в невідсортованій частині масиву і ставимо його в кінець цього підмассива.
    comparison = 0 # У пошуках максимуму підмассив перебудовується в, так зване, сортувальне дерево, в результаті чого
    replacement = 0# максимум сам "спливає" в початок масиву. Після цього переміщаємо максимум в кінець підмассиву.
    n = len(arr)   # Потім над частиною масиву, що залишилася, знову здійснюється процедура перебудови в сортувальне дерево
                   # з подальшим переміщенням максимуму в кінець підмассива.
    while True:
        question = input('Сортувати за зростанням (1) чи спаданням (2) ?\n')
        start = time()
        if (question == '1'):
            def heapify(arr, n, i): # створюємо ще одну функцію для "піддерева"
                largest = i
                l = 2 * i + 1
                r = 2 * i + 2
                if l < n and arr[i] < arr[l]:
                    largest = l
                if r < n and arr[largest] < arr[r]:
                    largest = r
                if largest != i:
                    arr[i], arr[largest] = arr[largest], arr[i]
                    nonlocal replacement
                    nonlocal comparison
                    replacement += 1
                    comparison += 2
                    heapify(arr, n, largest)

            for i in range(int(n / 2) - 1 - 1, -1, -1):
                heapify(arr, n, i)
            for i in range(n-1, 0, -1):
                arr[i], arr[0] = arr[0], arr[i]
                replacement += 1
                heapify(arr, i, 0)
        elif (question == '2'):
            def heapify(arr, n, i):
                smallest = i
                l = 2 * i + 1
                r = 2 * i + 2
                if l < n and arr[l] < arr[smallest]:
                    smallest = l
                if r < n and arr[r] < arr[smallest]:
                    smallest = r
                if smallest != i:
                    (arr[i], arr[smallest]) = (arr[smallest], arr[i])
                    nonlocal replacement
                    nonlocal comparison
                    replacement += 1
                    comparison += 2
                    heapify(arr, n, smallest)

            for i in range(int(n / 2) - 1, -1, -1):
                heapify(arr, n, i)
            for i in range(n - 1, -1, -1):
                arr[0], arr[i] = arr[i], arr[0]
                replacement += 1
                heapify(arr, i, 0)
        else:
            print('Введіть лише 1 або 2!\n')
            continue
        break

    stop = time()
    print(f'\nВідсортований масив: {arr}.\n')
    print(f'Кількість порівнянь: {comparison}.')
    print(f'Кількість обмінів: {replacement}.')
    print(f'Затрачений час: {stop - start}.')
    print('____________________________________________________________________________________________________')

main_function()

