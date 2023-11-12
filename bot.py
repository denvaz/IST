# Подключаем модуль случайных чисел 
import random
# Подключаем модуль для Телеграма
import telebot
# Указываем токен
bot = telebot.TeleBot('6800467293:AAHaQp8-XxEOTYtFv2k-RaJS69fjVOotwzY')
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types

# Метод, который получает сообщения и обрабатывает их
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если написали «Привет»
    if message.text == "Привет":
        # Пишем приветствие
        bot.send_message(message.from_user.id, "Добро пожаловать в программный комплекс!")

        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого знака зодиака
        key_oven = types.InlineKeyboardButton(text='Овен', callback_data='zodiac')
        # И добавляем кнопку на экран
        keyboard.add(key_oven)
        # key_telec = types.InlineKeyboardButton(text='Телец', callback_data='zodiac')
        # keyboard.add(key_telec)
        keyboard.add(types.InlineKeyboardButton(text='Телец', callback_data='zodiac'))

        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.from_user.id, text='Выбери свой знак зодиака', reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # Если нажали на одну из 12 кнопок — выводим гороскоп
    if call.data == "zodiac": 
        # Формируем гороскоп
        msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(second_add) + ' ' + random.choice(third)
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop=True, interval=0)