import telegram
import os
import time


# get token from environment variable
TOKEN = os.environ.get('TOKEN')

# create bot object
bot = telegram.Bot(token=TOKEN)


# echo function
def echo():
    last_update_id = 0 # last update id

    # infinite loop
    while True: 
        time.sleep(0.5) # pause 0.5 seconds

        current_update = bot.getUpdates()[-1] # get last update

        # if the last update id is not equal to the current update id
        if last_update_id != current_update.update_id: 
            
            # get chat id from the current update
            chat_id = current_update.message.chat.id

            # if the message is not None
            if current_update.message.text is not None:
                # get text from the current update
                text = current_update.message.text

                if text == '/start':
                    text = 'Hello, World!'
                # send message
                bot.sendMessage(chat_id=chat_id, text=text)

            # if the message is not None
            elif current_update.message.photo is not None:
                # get photo id from the current update
                photo_id = current_update.message.photo[-1].file_id

                # send photo
                bot.sendPhoto(chat_id=chat_id, photo=photo_id)


            # update last update id
            last_update_id = current_update.update_id

        

echo() # call echo function
