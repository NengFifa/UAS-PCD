import telebot
import cv2

api = ('6301337173:AAEhc_m6Ygym-yMMUR0uw6PXJ-eI_TapxL8')
bot = telebot.TeleBot(api)


def welcome(message):
    # membalas pesan
    
        bot.send_message(message, "Tidak pakai masker")
        bot.sendPhoto(message, ('temp.jpg', temp))

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, 'oiiii')

bot.polling()



