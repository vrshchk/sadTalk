import telebot
import config
import time
import pymongo


myclient = pymongo.MongoClient("mongodb+srv://user:userpass@sadtalk.0ycvj.mongodb.net/patternsDB?retryWrites=true&w=majority")
mydb = myclient["patternsDB"]


collist = mydb.list_collection_names()
collection = mydb.intents
index_cursor = collection.list_indexes()
print(index_cursor)


for index in index_cursor:
	print(index.keys())

for post in collection.find():
	arr = (post['patterns'])
	print(arr)




if "intents" in collist:
  print("The collection exists.")


bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types=['text'])
def lalala(message):
	bot.send_chat_action(chat_id=message.chat.id, action = 'typing')
	time.sleep(1)
	s = message.text
	ans = ':)' 
	answerFound = 0
 
	foundExactly = (collection.find({"patterns":s}).count())

	if (foundExactly != 0 ):
		ans = collection.find_one({"patterns":s})["answers"]
		answerFound = 1

	if (answerFound==0):
		for obj in collection.find():
			arr = obj["patterns"]
			for answ in arr:
				if (answ in s):
					temp = obj['answers']
					ans = temp[0]
					ans = ans.replace("*",answ)


		
	
	bot.send_message(message.from_user.id,ans)



bot.polling(none_stop=True, interval=0, timeout=20)

