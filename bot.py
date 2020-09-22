import telebot
import config
import time
import json
import numpy
import re

with open('intents.json') as file:
    data = json.load(file)

bot = telebot.TeleBot(config.TOKEN)

def randChoice(arr):
    rand = numpy.random.randint(0, len(arr))
    return arr[rand]

def findAnswer(s):
	if (s=="/start"):
		return "Chat started"
	else:
	    for intent in data['intents']:
	        doc = intent
	        patterns = doc["patterns"]
	        for pattern in patterns:
	            if (not re.search( ("[a-zA-Z]"+pattern),s) or pattern==""):
	                if (not re.search((pattern+"[a-zA-Z]"),s) or pattern==""):
	                    if (pattern in s):
	                        if ( doc["context_set"] in s):
	                            if ( doc["anti_context_set"] != "-"):
	                                if (not doc["anti_context_set"] in s):
	                                    answers = doc["answers"]
	                                    result = randChoice(answers)
	                                    result = result.replace("*", pattern)
	                                    return result
	                            else:
	                                answers = doc["answers"]
	                                result = randChoice(answers)
	                                result = result.replace("*", pattern)
	                                return result
        
   
@bot.message_handler(content_types=['text'])
def lalala(message):
  bot.send_chat_action(chat_id=message.chat.id, action = 'typing')
  time.sleep(0.5)
  s = message.text.lower()
  answer = findAnswer(s)
  bot.send_message(message.from_user.id,answer)

bot.polling(none_stop=True, interval=0, timeout=20)