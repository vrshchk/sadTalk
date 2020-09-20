import telebot
import config
import time
import pymongo


myclient = pymongo.MongoClient("mongodb+srv://user:userpass@sadtalk.0ycvj.mongodb.net/patternsDB?retryWrites=true&w=majority")
mydb = myclient["patternsDB"]


collist = mydb.list_collection_names()
collection = mydb.intents


for post in collection.find():
	print(post)




if "intents" in collist:
  print("The collection exists.")


bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types=['text'])
def lalala(message):
	#bot.send_chat_action(chat_id=message.chat.id, action = Telegram.chat.ChatAction.TYPING)
	time.sleep(1)
	s = message.text+'!!!!'
	bot.send_message(message.chat.id, s)



bot.polling(none_stop=True, interval=0, timeout=20)

