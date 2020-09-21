import telebot
import config
import time
import pymongo


myclient = pymongo.MongoClient("mongodb+srv://user:userpass@sadtalk.0ycvj.mongodb.net/patternsDB?retryWrites=true&w=majority")
mydb = myclient["patternsDB"]


collist = mydb.list_collection_names()
collection = mydb.intents



bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types=['text'])
def lalala(message):
	bot.send_chat_action(chat_id=message.chat.id, action = 'typing')
	time.sleep(0.5)
	s = message.text.lower()
	ans = ':)' 
	answerFound = 0


	if ("?" in s ):
		if ('do you' in s):
			questions = collection.find_one({"tag":"questions"})["patterns"]
			verbs = collection.find_one({"tag":"verbs"})["patterns"]
			for verb in verbs:
				for quest in questions:
					if ((verb in s) and (quest in s)):
						ans = "I don't think you will understand " + quest + " i " + verb + " that."
						answerFound = 1
						break
		
			if (answerFound==0):
				verbs = collection.find_one({"tag":"verbs"})["patterns"]
				for word in verbs:
					if (word in s):
						ans = "Now, i don't " + word + " it"
						answerFound = 1
						break
			



	if (answerFound==0):
		for obj in collection.find():
			arr = obj["patterns"]
			print(arr)
			for answ in arr:
				print(answ)
				if (answ in s):
					temp = obj["answers"]
					ans = temp[0]
					ans = ans.replace("*",answ)


		
	
	bot.send_message(message.from_user.id,ans)







bot.polling(none_stop=True, interval=0, timeout=20)

