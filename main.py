import telebot
from telebot import types


bot = telebot.TeleBot('6741003468:AAFltKvoJJszlKV8a54QWPwPsbdABHJrlmQ')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'hi {message.from_user.first_name}'
    bot.send_message(message.chat.id, mess)


@bot.message_handler(commands=['but'])
def but(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Amirchik & Haru - Чистый кайф')
    btn2 = types.KeyboardButton('Bakr - Бедный поэт')
    btn3 = types.KeyboardButton('V $ X V PRiNCE & De Lacure - Су')
    btn4 = types.KeyboardButton('Jax - Sebelep')
    btn5 = types.KeyboardButton('Mirbek Atabekov & Begish - Айтчы')
    btn6 = types.KeyboardButton('ILUXA & ULUKMANAPO - Миледи')
    btn7 = types.KeyboardButton('FREEMAN996 - Герой')
    btn8 = types.KeyboardButton('Эллай - Давай просто летать')
    btn9 = types.KeyboardButton('V $ X V PRiNCE - Суета')
    btn10 = types.KeyboardButton('Akha - Какая ты красивая')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10)
    bot.send_message(message.chat.id, text="hi {0.first_name}".format(message.from_user), reply_markup=markup)


@bot.message_handler()
def user(message):
    if message.text == 'Amirchik & Haru - Чистый кайф':
        with open('./music/чистый кайф amirchik & haru [speed up].mp3', 'rb') as file:
            audio_data = file.read()
        bot.send_audio(message.chat.id, audio_data)
    elif message.text == 'Bakr - Бедный поэт':
        audio = open('music/Bakr - Бедный поэт.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
    elif message.text == 'V $ X V PRiNCE & De Lacure - Су':
        audio = open('music/V $ X V PRiNCE feat. De Lacure - Су.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
    elif message.text == 'Jax - Sebelep':
        audio = open('music/Jax (02.14) - Sebelep.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
    elif message.text == 'Mirbek Atabekov & Begish - Айтчы':
        audio = open('music/Мирбек Атабеков, Бегиш - Айтчы.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
    elif message.text == 'ILUXA & ULUKMANAPO - Миледи':
        audio = open('music/ILUXA, Ulukmanapo - Миледи (Official Audio).mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
    elif message.text == 'FREEMAN996 - Герой':
        audio = open('music/FREEMAN 996 - Герой (speed Up).mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
    elif message.text == 'Эллай - Давай просто летать':
        audio = open('music/Эллаи_давай_просто_летать_speed_up_baby_Я_не_твой_baby_ты_не_моя.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
    elif message.text == 'V $ X V PRiNCE - Суета':
        audio = open('music/Не_спрыгивай,_рискни_давай_Попробуй,_но_не_привыкай_•_V_$_X_V_PRiNCE.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
    elif message.text == 'Akha - Какая ты красивая':
        audio = open('music/akha-какая ты красивая speed up.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
    else:
        print('Dont understand')


bot.polling(none_stop=True)