# Импорт модуля для генерации случайных чисел
import random
# Импорт класса для работы с датой и временем
import datetime
# Подключаем модуль для Телеграма
import telebot
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types

# Указываем токен бота
bot = telebot.TeleBot('6800467293:AAHaQp8-XxEOTYtFv2k-RaJS69fjVOotwzY')

# Глобальные переменные
Lmax = 10000  # Максимальное значение элемента массива
NLimitPrintMas = 20  # Максимальное количество элементов массива для вывода
A = [0] * Lmax  # Инициализация массива A нулями длиной Lmax
CopyA = [0] * Lmax  # Инициализация копии массива A нулями длиной Lmax
N = 0  # Размер массива
SMALL_SIZE = 20  # Максимальный размер небольшого массива


###### ФУНКЦИИ РАСЧЕТОВ

# Функция для вывода массива с возможностью ограничения вывода по размеру
def print_array(arr):
    if len(arr) <= NLimitPrintMas:  # Если размер массива меньше или равен NLimitPrintMas
        # print(arr)
        return arr
    else:
        cutarr = arr[:NLimitPrintMas]  # Выводим первые NLimitPrintMas элементов
        # print("...")  # Обозначаем, что массив продолжается
        cutarr = ", ".join(map(str, cutarr)) + "..."
        return cutarr

# @time_it
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

# @time_it
# Функция сортировки пузырьком
def bubble_sort(arr, order):
    global CopyA, N  # Используем глобальные переменные для N и CopyA
    N = len(arr)  # Получаем размер массива
    CopyA = arr.copy()  # Создаем копию массива

    for i in range(N):  # Проходим по всем элементам массива
        for j in range(N-i-1):  # Проходим по элементам до N-i-1
            if (order == 1 and CopyA[j] > CopyA[j+1]) or (order == 2 and CopyA[j] < CopyA[j+1]):
                CopyA[j], CopyA[j+1] = CopyA[j+1], CopyA[j]  # Обмен элементов

# @time_it
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

# @time_it
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
    

# Готовим кнопки
keyboard = types.InlineKeyboardMarkup()

# Добавляем кнопку на экран
keyboard.add(types.InlineKeyboardButton(text='Сгенерировать массив', callback_data='generate_array'))
keyboard.add(types.InlineKeyboardButton(text='Сортировка выбором', callback_data='selection_sort'))
keyboard.add(types.InlineKeyboardButton(text='Сортировка пузырьком', callback_data='bubble_sort'))
keyboard.add(types.InlineKeyboardButton(text='Сортировка вставкой', callback_data='insertion_sort'))
keyboard.add(types.InlineKeyboardButton(text='Быстрая сортировка', callback_data='quick_sort'))
keyboard.add(types.InlineKeyboardButton(text='Линейный поиск элемента', callback_data='linear_search'))
keyboard.add(types.InlineKeyboardButton(text='Двоичный поиск элемента', callback_data='binary_search_all'))
keyboard.add(types.InlineKeyboardButton(text='Задать режим табулирования', callback_data='tab_select'))
keyboard.add(types.InlineKeyboardButton(text='Поиск первых 1000 чисел натурального ряда (линейный)', callback_data='linear_search_first_n_elements'))
keyboard.add(types.InlineKeyboardButton(text='Поиск первых 1000 чисел натурального ряда (двоичный)', callback_data='binary_search_first_n_elements'))
keyboard.add(types.InlineKeyboardButton(text='Выход', callback_data='exit'))


# Функция для генерации массива случайных чисел
def generate_array(n):
    # Создаем массив случайных чисел, где n - количество элементов в массиве
    # и каждый элемент находится в диапазоне от 1 до Lmax включительно
    arr = [random.randint(1, Lmax) for _ in range(int(n))]  # Преобразуем введенное значение в целое число
    return arr

# Метод, который получает сообщения и обрабатывает их
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Добро пожаловать в программный комплекс!")

        # # Готовим кнопки
        # keyboard = types.InlineKeyboardMarkup()
        # # По очереди готовим текст и обработчик
        # generate = types.InlineKeyboardButton(text='Сгенерировать массив', callback_data='generate')
        # # И добавляем кнопку на экран
        # keyboard.add(generate)
        # sort = types.InlineKeyboardButton(text='Сортировка выбором', callback_data='sort')
        # keyboard.add(sort)
        # Показываем кнопки и пишем сообщение о выборе
        bot.send_message(message.from_user.id, text='Выберите действие', reply_markup=keyboard)

    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "generate_array":
        # спрашиваем про количество элементов в массиве
        msg = bot.send_message(call.from_user.id, "Введите размер массива")
        bot.register_next_step_handler(msg, process_array_size)

def process_array_size(message):
    global A
    try:
        n = int(message.text)
        A = generate_array(n)
        # Вывод сообщения с массивом
        

        if n <= SMALL_SIZE:  # Если размер массива небольшой
            result_message = "Начальный массив:" + "\n" + str(A) + "\n"  # Начинаем с вывода исходного массива
            for order in [1, 2]:
                result_message += "\n\nСортировка выбором (Порядок: {}):".format("возрастание" if order == 1 else "убывание")
                selection_sort(A.copy(), order)  # Сортировка выбором
                result_message += "\n" + str(CopyA)  # Добавляем результат сортировки

                result_message += "\n\nСортировка пузырьком (Порядок: {}):".format("возрастание" if order == 1 else "убывание")
                bubble_sort(A.copy(), order)  # Сортировка пузырьком
                result_message += "\n" + str(CopyA)  # Добавляем результат сортировки

                result_message += "\n\nСортировка вставкой (Порядок: {}):".format("возрастание" if order == 1 else "убывание")
                insertion_sort(A.copy(), order)  # Сортировка вставкой
                result_message += "\n" + str(CopyA)  # Добавляем результат сортировки

                result_message += "\n\nБыстрая сортировка (Порядок: {}):".format("возрастание" if order == 1 else "убывание")
                quick_sort(A.copy(), order)  # Быстрая сортировка
                result_message += "\n" + str(CopyA)  # Добавляем результат сортировки

            bot.send_message(message.from_user.id, result_message, reply_markup=keyboard)


    except ValueError:
        # bot.send_message(message.from_user.id, "Введите корректное число", reply_markup=keyboard)
        bot.send_message(message.from_user.id, text='Введите корректное число', reply_markup=keyboard)

# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop=True, interval=0)
