from pyowm import OWM
import telebot
from time import sleep
from translate import Translator
a = Translator(from_lang = 'en', to_lang = 'ru')


owm = OWM('ff0653937d132f04bf3b4b139e8ce579')
bot = telebot.TeleBot("1341898477:AAHihWTvE1-f9AWimNmKvrbBQotAkRlyvP8", parse_mode=None)


@bot.message_handler(commands=['start'])
def inp(message):
	bot.send_message(message.chat.id, "Введите город/ ?:")

@bot.message_handler(content_types = ['text'])
def send_data(message):
	try:
		mgr = owm.weather_manager()
		observation = mgr.weather_at_place(message.text)
		w = observation.weather
		temp = w.temperature( 'celsius' )["temp"]
		#sleep(2)
		b = a.translate(w.detailed_status)
		answer = "В городе " + message.text + " сейчас " + b + "\n"
		answer += "Температура сейчас в раёне " + str(temp)+ "\n\n"

		if temp < 10:
			bot.send_message(message.chat.id,"3 секуды и вы получите Предскозание")
			sleep(3)
			answer += " Сейчас очень холодно 🥶🥶🥶 оденься как танк! "+"\n"
			answer += "Предскозание завершена !"
			bot.send_message(message.chat.id, answer)
		elif temp < 1:
			bot.send_message(message.chat.id,"3 секуды и вы получите Предскозание")
			sleep(3)
			answer += "Понимаешь, сечас не время гулять 🥶🥶🥶 замерзнишь! \n"
			answer += "Предскозание завершена !"
			bot.send_message(message.chat.id, answer)
		elif temp < 20:
			bot.send_message(message.chat.id,"3 секуды и вы получите Предскозание")
			sleep(3)
			answer += " Сейчас холодно оденьтесь потеплее !"+"\n"
			answer+= "Предскозание завершена !"
			bot.send_message(message.chat.id, answer)
		elif temp > 20:
			bot.send_message(message.chat.id,"3 секуды и вы получите Предскозание")
			sleep(3)
			answer += "На улице погода норм, одевай что угодно! "+"\n"
			answer+= "Предскозание завершена !"
			bot.send_message(message.chat.id, answer)
	except:
		bot.send_message(message.chat.id, "Введите имя города или введите ее правильно !!!")


bot.polling( none_stop = True )
