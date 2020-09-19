import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types=['text'])
def lalala(message):
	s = message.text+'!!'
	bot.send_message(message.chat.id, s)


bot.polling(none_stop=True)