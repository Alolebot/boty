import telebot,requests
from telebot import types
import random
bot = telebot.TeleBot('توكن')
@bot.message_handler(commands=['start'])
def start(message):
    buttons = types.InlineKeyboardMarkup(row_width=1)
    but1 = types.InlineKeyboardButton(text=' - حسابي - ', url='https://t.me/P_2_9')
    but2 = types.InlineKeyboardButton(text=' - قناتي - ', url='https://t.me/OPP0Y')
    buttons.add(but1,but2)
    bot.send_message(message.chat.id, '''<strong>
اهلا بك في بوت صيد يوزرات تيك توك تم صنع البوت من قبل المبرمج عبيس قم ب ضغط على /Start للصيد
</strong>''', parse_mode='html', reply_to_message_id=message.message_id, reply_markup=buttons)

@bot.message_handler(commands=['Start'])
def Start(message):
 aab = message.text
 while True:
  user=str("".join(random.choice('1234567890_.qwertyuiopasdfghjklzxcvbnm')for i in range(4)))
  hea = {

        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',    }
  tiko = f'https://www.tiktok.com/@{user}?lang=ar'
  reqsnd = requests.get(tiko, headers=hea).status_code
  if reqsnd==404:
   print(f" - Good user : {user}")
   bot.send_message(message.chat.id,f""" - تم صيد يوزر تيك ✅ :
— — — — — 
user TikTok : {user}
— — — — —
- BY : @OPP0Y - @P_2_9 """)
  else:
   print(f" - Bad user : {user}")

bot.polling()
                
		
