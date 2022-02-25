import telebot 
from gtts import gTTS
import pytube
from googletrans import Translator
from datetime import datetime
now = datetime.now()


token='5226178173:AAH7-iG6-3rId1cvuvSSlHkb2E0xYH87Lm0'

bot = telebot.TeleBot(token=token)
@bot.message_handler(commands=['start'])
def send_messagee(message):
    username=message.chat.first_name
    bot.send_message(message.chat.id, f'Привет {username}. Я телеграм бот')
        
@bot.message_handler(content_types='text')
def send(message):
    translator = Translator()
    txt = translator.translate(message.text, dest='ru')
    bot.send_message(message.chat.id, 'audio downloading...')
    audio=gTTS(txt.text, lang='ru')
    name = ('audio/'+ str(now) +'.mp3')
    audio.save(name)

    audio = open(name, 'rb')
    bot.send_audio(message.chat.id, audio)
    audio.close()

print('Бот работает.....')  
bot.infinity_polling()

