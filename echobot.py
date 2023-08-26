from telegram.ext import (
    Updater,
    MessageHandler,
    CommandHandler,
    Filters,
)
from handlers import (
    start,
    echo_text,
    echo_photo,
    echo_sticker,
    echo_voice,
    echo_video,
    echo_document,
    echo_location,
    echo_contact,
    echo_animation,
    echo_audio,
    echo_video_note,
)

import os


# get token from environment variable
TOKEN = os.environ.get('TOKEN')


def main():
    # create updater object
    updater = Updater(token=TOKEN)
    
    # get dispatcher from updater
    dispatcher = updater.dispatcher
    
    # add start handler to dispatcher
    dispatcher.add_handler(handler=CommandHandler(command=('start', 'boshlash'), callback=start))
    
    # add echo handler to dispatcher
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text, callback=echo_text))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.photo, callback=echo_photo))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.sticker, callback=echo_sticker))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.voice, callback=echo_voice))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.video, callback=echo_video))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.document, callback=echo_document))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.location, callback=echo_location))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.contact, callback=echo_contact))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.animation, callback=echo_animation))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.audio, callback=echo_audio))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.video_note, callback=echo_video_note))
    
    
    # start polling
    updater.start_polling()
    
    # stop polling after 60 seconds
    updater.idle()
    

if __name__ == '__main__':
    main()
