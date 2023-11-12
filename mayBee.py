import random  # Импорт модуля для генерации случайных чисел
import datetime  # Импорт класса для работы с датой и временем
# Коммент
# Глобальные переменные
Lmax = 10000  # Максимальное значение элемента массива
NLimitPrintMas = 20  # Максимальное количество элементов массива для вывода
A = [0] * Lmax  # Инициализация массива A нулями длиной Lmax
CopyA = [0] * Lmax  # Инициализация копии массива A нулями длиной Lmax
N = 0  # Размер массива
SMALL_SIZE = 20  # Максимальный размер небольшого массива

def time_it(func):   # Функция time_it принимает другую функцию (func) в качестве аргумента и возвращает обертку (wrapper).
    def wrapper(*args, **kwargs): 
        #  *args позволяет передавать неименованные аргументы в функцию в виде кортежа, а **kwargs позволяет передавать именованные аргументы в виде словаря. Эти конструкции делают функции гибкими и позволяют им принимать разное количество аргументов.
        start_time = datetime.datetime.now()  # Записываем текущее время перед выполнением целевой функции.
        result = func(*args, **kwargs)   # Вызываем целевую функцию (func) с переданными аргументами и получаем её результат.
        end_time = datetime.datetime.now()    # Записываем текущее время после выполнения целевой функции.
        execution_time = end_time - start_time  # Рассчитываем время выполнения, вычитая начальное время из конечного времени.
        #  Создаем словарь, который сопоставляет английские имена функций с русскими описаниями.
        russian_function_name = {
            'generate_array': 'Генерация массива',
            'selection_sort': 'Функция сортировки выбором',
            'bubble_sort': 'Функция сортировки пузырьком',
            'insertion_sort': 'Функция сортировки вставкой',
            'quick_sort': 'Функция быстрой сортировки',
            'linear_search': 'Функция линейного поиска элемента',
            'binary_search_all': 'Функция двоичного поиска элемента',
            'linear_search_first_n_elements': 'Функция линейного поиска первых 1000 чисел натурального ряда',
            'binary_search_first_n_elements': 'Функция двоичного поиска первых 1000 чисел натурального ряда',
        }
        func_name = russian_function_name.get(func.__name__, func.__name__)   # Получаем русское описание функции, если оно есть в словаре, или используем английское имя в противном случае.
        print(f"{func_name} выполнилась за {execution_time}")  # Выводим наименование функции и время выполнения.
        return result   # Возвращаем результат выполнения целевой функции.
    return wrapper  # Возвращаем обертку (wrapper) как результат выполнения функции time_it.

@time_it
# Функция для генерации массива случайных чисел
def generate_array(n):
    # Создаем массив случайных чисел, где n - количество элементов в массиве
    # и каждый элемент находится в диапазоне от 1 до Lmax включительно
    arr = [random.randint(1, Lmax) for _ in range(n)]
    return arr

# Функция для вывода массива с возможностью ограничения вывода по размеру
def print_array(arr):
    if len(arr) <= NLimitPrintMas:  # Если размер массива меньше или равен NLimitPrintMas
        print(arr)
    else:
        print(arr[:NLimitPrintMas])  # Выводим первые NLimitPrintMas элементов
        print("...")  # Обозначаем, что массив продолжается

@time_it
# Функция сортировки выбором
def selection_sort(arr, order):
    global CopyA, N  # Используем глобальные переменные для N и CopyA
    N = len(arr)  # Получаем размер массива
    CopyA = arr.copy()  # Создаем копию массива
 
    for j in range(N):  # Проходим по всем элементам массива
        min_idx = j
        for i in range(j+1, N):  # Проходим по оставшимся элементам массива
            if (order == 1 and CopyA[i] < CopyA[min_idx]) or (order == 2 and CopyA[i] > CopyA[min_idx]):
                min_idx = i
        CopyA[j], CopyA[min_idx] = CopyA[min_idx], CopyA[j]  # Обмен элементов
   
@time_it
# Функция сортировки пузырьком
def bubble_sort(arr, order):
    global CopyA, N  # Используем глобальные переменные для N и CopyA
    N = len(arr)  # Получаем размер массива
    CopyA = arr.copy()  # Создаем копию массива

    for i in range(N):  # Проходим по всем элементам массива
        for j in range(N-i-1):  # Проходим по элементам до N-i-1
            if (order == 1 and CopyA[j] > CopyA[j+1]) or (order == 2 and CopyA[j] < CopyA[j+1]):
                CopyA[j], CopyA[j+1] = CopyA[j+1], CopyA[j]  # Обмен элементов

@time_it
# Функция сортировки вставкой
def insertion_sort(arr, order):
    global CopyA, N  # Используем глобальные переменные для N и CopyA
    N = len(arr)  # Получаем размер массива
    CopyA = arr.copy()  # Создаем копию массива

    for i in range(1, N):  # Проходим по всем элементам массива, начиная со второго
        key_item = CopyA[i]  # Выбираем текущий элемент
        j = i - 1
        while j >= 0 and ((order == 1 and CopyA[j] > key_item) or (order == 2 and CopyA[j] < key_item)):
            CopyA[j+1] = CopyA[j]  # Сдвигаем элементы вправо
            j -= 1
        CopyA[j+1] = key_item  # Вставляем элемент на нужное место

@time_it
# Функция быстрой сортировки
def quick_sort(arr, order):
    global CopyA, N  # Используем глобальные переменные для N и CopyA
    N = len(arr)  # Получаем размер массива
    CopyA = arr.copy()  # Создаем копию массива

    # Вспомогательная функция для быстрой сортировки
    def qsort(lst):
        if len(lst) <= 1:
            return lst
        else:
            pivot = lst[len(lst) // 2]  # Выбираем опорный элемент
            less_lst = [elem for elem in lst if elem < pivot]  # Элементы меньше опорного
            equal_lst = [elem for elem in lst if elem == pivot]  # Элементы равные опорному
            greater_lst = [elem for elem in lst if elem > pivot]  # Элементы больше опорного
            if order == 1:
                return qsort(less_lst) + equal_lst + qsort(greater_lst)  # Рекурсивно сортируем и объединяем
            else:
                return qsort(greater_lst) + equal_lst + qsort(less_lst)  # Рекурсивно сортируем и объединяем

    CopyA = qsort(CopyA)  # Вызываем вспомогательную функцию
    
@time_it   
# Функция линейного поиска элемента
def linear_search(arr, item):
    indices = []  # Список для хранения индексов
    for i in range(len(arr)):
        if arr[i] == item:  # Если элемент равен искомому
            indices.append(i)  # Добавляем индекс в список
    return indices  # Возвращаем список индексов

@time_it
# Функция двоичного поиска для всех вхождений элемента
def binary_search_all(arr, item, order):
    indices = []  # Список для хранения индексов
    low = 0  # Нижняя граница
    high = len(arr) - 1  # Верхняя граница

    # Поиск первого вхождения элемента
    first_occurrence = -1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            first_occurrence = mid
            break
        elif (order == 1 and guess > item) or (order == 2 and guess < item):
            high = mid - 1
        else:
            low = mid + 1

    if first_occurrence == -1:
        return indices  # Возвращаем пустой список, так как элемент не был найден

    # Поиск влево от первого вхождения
    left = first_occurrence
    while left >= 0 and ((order == 1 and arr[left] == item) or (order == 2 and arr[left] == item)):
        indices.append(left)
        left -= 1

    # Поиск вправо от первого вхождения
    right = first_occurrence + 1
    while right < len(arr) and ((order == 1 and arr[right] == item) or (order == 2 and arr[right] == item)):
        indices.append(right)
        right += 1

    return indices  # Возвращаем список индексов

@time_it
# Функция линейного поиска первых n элементов
def linear_search_first_n_elements(arr, n):
    result = []  # Список для хранения результатов
    unique_set = set()  # Множество для отслеживания уникальных элементов

    for i in arr:
        if n == 0:  # Если количество найденных элементов достигло n
            break
        if i <= 1000 and i not in unique_set:  # Если элемент меньше или равен 1000 и ещё не добавлен
            result.append(i)  # Добавляем элемент в результат
            unique_set.add(i)  # Добавляем элемент в множество
            n -= 1

    return result # Возвращаем список результатов

@time_it
# Функция двоичного поиска первых n элементов
def binary_search_first_n_elements(arr):
    result = []
    current_number = 1  # Инициализируем переменную для отслеживания текущего числа
    
    while current_number <= 1000:  # Пока не найдено 1000 чисел (или менее)
        low = 0  # Нижняя граница для бинарного поиска
        high = len(arr) - 1  # Верхняя граница для бинарного поиска
        found = False  # Флаг для отслеживания нахождения текущего числа

        while low <= high:  # Проводим бинарный поиск внутри массива
            mid = (low + high) // 2 # Находим середину текущего интервала
            if arr[mid] == current_number:  # Если текущее число найдено
                found = True  # Устанавливаем флаг на "найдено"
                break
            elif arr[mid] < current_number:   # Если текущий элемент меньше искомого числа
                low = mid + 1   # Сдвигаем нижнюю границу
            else:
                high = mid - 1   # Сдвигаем верхнюю границу

        if found:   # Если текущее число было найдено
            result.append(current_number)   # Добавляем его в результат
        current_number += 1  # Переходим к поиску следующего числа

    return result

# Функция проверки введенного числа
def get_positive_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Неверный ввод. Введите положительное целое число.")
        except ValueError:
            print("Неверный ввод. Введите целое число.")

# Главная функция
def main():
    global A  # Используем глобальную переменную A

    print("Добро пожаловать в программный комплекс!")  # Приветствие
    input("Нажмите Enter, чтобы продолжить...")  # Ожидание ввода пользователя

    while True:  # Бесконечный цикл для меню
        print("---------------------------------------------------------")
        print("1. Сгенерировать массив")
        print("2. Сортировка выбором")
        print("3. Сортировка пузырьком")
        print("4. Сортировка вставкой")
        print("5. Быстрая сортировка")
        print("6. Линейный поиск элемента")
        print("7. Двоичный поиск элемента")
        print("8. Задать режим табулирования")
        print("9. Поиск первых 1000 чисел натурального ряда (линейный)")
        print("10. Поиск первых 1000 чисел натурального ряда (двоичный)")
        print("0. Выход")
        print("---------------------------------------------------------")

        choice = input("Выберите опцию: ")  # Ввод выбора пользователя

        sorted_array = sorted(A)  # Создание отсортированной копии массива

        if choice == "0":
            break  # Выход из цикла при выборе 0
        elif choice == "1":
            n = get_positive_integer_input("Введите размер массива: ")  # Ввод размера массива
            A = generate_array(n)  # Генерация массива
            print_array(A)  # Вывод массива

            if n <= SMALL_SIZE:  # Если размер массива небольшой
                for order in [1, 2]:
                    print("\nСортировка выбором (Порядок: {}):".format("возрастание" if order == 1 else "убывание"))
                    selection_sort(A.copy(), order)  # Сортировка выбором
                    print_array(CopyA)  # Вывод отсортированного массива

                    print("\nСортировка пузырьком (Порядок: {}):".format("возрастание" if order == 1 else "убывание"))
                    bubble_sort(A.copy(), order)  # Сортировка пузырьком
                    print_array(CopyA)  # Вывод отсортированного массива

                    print("\nСортировка вставкой (Порядок: {}):".format("возрастание" if order == 1 else "убывание"))
                    insertion_sort(A.copy(), order)  # Сортировка вставкой
                    print_array(CopyA)  # Вывод отсортированного массива

                    print("\nБыстрая сортировка (Порядок: {}):".format("возрастание" if order == 1 else "убывание"))
                    quick_sort(A.copy(), order)  # Быстрая сортировка
                    print_array(CopyA)  # Вывод отсортированного массива
           

    
        elif choice == "2":
            order = get_positive_integer_input("Выберите порядок сортировки (1 - возрастание, 2 - убывание): ")  # Ввод порядка сортировки
            if order == 1 or order == 2:
                selection_sort(A, order)  # Сортировка выбором
                print("Отсортированный массив:")
                print_array(CopyA)  # Вывод отсортированного массива
            else:
                print("Некорректный порядок сортировки")  # Вывод сообщения об ошибке

        elif choice == "3":
            order = get_positive_integer_input("Выберите порядок сортировки (1 - возрастание, 2 - убывание): ")  # Ввод порядка сортировки
            if order == 1 or order == 2:
                bubble_sort(A, order)  # Сортировка пузырьком
                print("Отсортированный массив:")
                print_array(CopyA)  # Вывод отсортированного массива
            else:
                print("Некорректный порядок сортировки")  # Вывод сообщения об ошибке

        elif choice == "4":
            order = get_positive_integer_input("Выберите порядок сортировки (1 - возрастание, 2 - убывание): ")  # Ввод порядка сортировки
            if order == 1 or order == 2:
                insertion_sort(A, order)  # Сортировка вставкой
                print("Отсортированный массив:")
                print_array(CopyA)  # Вывод отсортированного массива
            else:
                print("Некорректный порядок сортировки")  # Вывод сообщения об ошибке

        elif choice == "5":
            order = get_positive_integer_input("Выберите порядок сортировки (1 - возрастание, 2 - убывание): ")  # Ввод порядка сортировки
            if order == 1 or order == 2:
                quick_sort(A, order)  # Быстрая сортировка
                print("Отсортированный массив:")
                print_array(CopyA)  # Вывод отсортированного массива
            else:
                print("Некорректный порядок сортировки")  # Вывод сообщения об ошибке

        elif choice == "6":
            item = get_positive_integer_input("Введите элемент для поиска: ")  # Ввод искомого элемента
            indices = linear_search(CopyA, item)  # Линейный поиск
            if indices:
                print("Элемент", item, "найден в позициях:", ", ".join(map(str, indices)))  # Вывод результатов поиска
            else:
                print("Элемент не найден")  # Вывод сообщения об отсутствии элемента

        elif choice == "7":
            item = get_positive_integer_input("Введите элемент для поиска: ")  # Ввод искомого элемента
            indices = binary_search_all(CopyA, item, order)  # Двоичный поиск
            if indices:
                print("Элемент", item, "найден в позициях:", ", ".join(map(str, indices)))  # Вывод результатов поиска
            else:
                print("Элемент не найден")  # Вывод сообщения об отсутствии элемента

        elif choice == "8":
            # Ввод параметров для табулирования
            NBegin = get_positive_integer_input("Введите начальное значение N: ")
            NEnd = get_positive_integer_input("Введите конечное значение N: ")
            NStep = get_positive_integer_input("Введите шаг для N: ")

            for n in range(NBegin, NEnd + 1, NStep):  # Цикл по значениям N
                A = generate_array(n)  # Генерация массива
                print(f"\nМассив с размером {n}:")
                print_array(A)  # Вывод массива
                for order in [1, 2]:
                    print("\nСортировка выбором (Порядок: {}):".format("возрастание" if order == 1 else "убывание"))
                    selection_sort(A.copy(), order)  # Сортировка выбором
                    print_array(CopyA)  # Вывод отсортированного массива

                    print("\nСортировка пузырьком (Порядок: {}):".format("возрастание" if order == 1 else "убывание"))
                    bubble_sort(A.copy(), order)  # Сортировка пузырьком
                    print_array(CopyA)  # Вывод отсортированного массива

                    print("\nСортировка вставкой (Порядок: {}):".format("возрастание" if order == 1 else "убывание"))
                    insertion_sort(A.copy(), order)  # Сортировка вставкой
                    print_array(CopyA)  # Вывод отсортированного массива

                    print("\nБыстрая сортировка (Порядок: {}):".format("возрастание" if order == 1 else "убывание"))
                    quick_sort(A.copy(), order)  # Быстрая сортировка
                    print_array(CopyA)  # Вывод отсортированного массива

        elif choice == "9":
            print("Линейный поиск первых 1000 чисел натурального ряда")
            found_elements = linear_search_first_n_elements(sorted_array, 1000)  # Линейный поиск первых 1000 элементов
            
            print("Элементы:", found_elements)  # Вывод найденных элементов

        elif choice == "10":
            print("Двоичный поиск первых 1000 чисел натурального ряда")

            found_elements2 = binary_search_first_n_elements(sorted_array)
            
            print("Элементы:", found_elements2)  # Вывод найденных элементов
        
        else:
            print("Выберете опцию. Введите цифру от 0 до 10.")
            
# Вызов главной функции
main()

