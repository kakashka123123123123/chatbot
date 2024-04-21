import telebot
bot = telebot.TeleBot('7049985044:AAF7QHbHvPAujW_FPx71yQrUU_WgNRF6trg')

bot.send_message(message.chat.id, 'Привет!\n'
                                  'Я помогу тебе решить пример'
                                                                )






@bot.message_handler(commands=['start'])
def get_text_message(message):
    if message.text == 'Помоги решить пример':
     bot.send_message(message.chat.id, 'Введите выражение.Доступные знаки:+,-,*,/,^,1!(факториал')


@bot.message_handler(func=lambda message: len(message.text.split()) == 3)
def calculator(message):
    mes = message.text.split()
    vyr = {'+': int(mes[0]) + int(mes[2]),
           '-': int(mes[0]) + int(mes[2]),
           '*': int(mes[0]) + int(mes[2]),
           '/': int(mes[0]) + int(mes[2])}
    bot.send_message(message.chat.id, vyr[mes[1]])

bot.polling()