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

        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик
        generate = types.InlineKeyboardButton(text='Сгенерировать массив', callback_data='generate')
        # И добавляем кнопку на экран
        keyboard.add(generate)
        sort = types.InlineKeyboardButton(text='Сортировка выбором', callback_data='sort')
        keyboard.add(sort)
        # Показываем кнопки и пишем сообщение о выборе
        bot.send_message(message.from_user.id, text='Выберите действие', reply_markup=keyboard)

    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "generate":
        # спрашиваем про количество элементов в массиве
        msg = bot.send_message(call.from_user.id, "Введите размер массива")
        bot.register_next_step_handler(msg, process_array_size)

def process_array_size(message):
    try:
        n = int(message.text)
        array = generate_array(n)
        bot.send_message(message.from_user.id, str(array))
    except ValueError:
        bot.send_message(message.from_user.id, "Введите корректное число")

# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop=True, interval=0)
