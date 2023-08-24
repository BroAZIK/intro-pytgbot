import telegram
import os


TOKEN = os.environ.get('TOKEN')
bot = telegram.Bot(token=TOKEN)


updates = bot.getUpdates()

chat_id = updates[-1].message.chat.id
text = updates[-1].message.text

bot.sendMessage(chat_id=chat_id, text=text)
