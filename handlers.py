from telegram.ext import CallbackContext
from telegram import Update


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    # get chat id from the update
    chat_id = update.message.chat_id

    # get first name from the update
    first_name = update.message.from_user.first_name

    # get bot from context
    bot = context.bot

    # send message
    bot.sendMessage(chat_id=chat_id, text=f'Hello, <b>{first_name}</b>!\n\nWelcome to the bot!', parse_mode='HTML')


def echo_text(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    # get chat id and text from the update
    chat_id = update.message.chat_id
    text = update.message.text

    # get bot from context
    bot = context.bot

    # send message
    bot.sendMessage(chat_id=chat_id, text=text)


def echo_photo(update: Update, context: CallbackContext) -> None:
    """Echo the user photo."""
    # get chat id and photo id from the update
    chat_id = update.message.chat_id
    photo_id = update.message.photo[-1].file_id

    # get bot from context
    bot = context.bot

    # send photo
    bot.sendPhoto(chat_id=chat_id, photo=photo_id)


def echo_sticker(update: Update, context: CallbackContext) -> None:
    """Echo the user sticker."""
    # get chat id and sticker id from the update
    chat_id = update.message.chat_id
    sticker_id = update.message.sticker.file_id

    # get bot from context
    bot = context.bot

    # send sticker
    bot.sendSticker(chat_id=chat_id, sticker=sticker_id)


def echo_voice(update: Update, context: CallbackContext) -> None:
    """Echo the user voice."""
    # get chat id and voice id from the update
    chat_id = update.message.chat_id
    voice_id = update.message.voice.file_id

    # get bot from context
    bot = context.bot

    # send voice
    bot.sendVoice(chat_id=chat_id, voice=voice_id)


def echo_video(update: Update, context: CallbackContext) -> None:
    """Echo the user video."""
    # get chat id and video id from the update
    chat_id = update.message.chat_id
    video_id = update.message.video.file_id

    # get bot from context
    bot = context.bot

    # send video
    bot.sendVideo(chat_id=chat_id, video=video_id)


def echo_video_note(update: Update, context: CallbackContext) -> None:
    """Echo the user video note."""
    # get chat id and video note id from the update
    chat_id = update.message.chat_id
    video_note_id = update.message.video_note.file_id

    # get bot from context
    bot = context.bot

    # send video note
    bot.sendVideoNote(chat_id=chat_id, video_note=video_note_id)


def echo_animation(update: Update, context: CallbackContext) -> None:
    """Echo the user animation."""
    # get chat id and animation id from the update
    chat_id = update.message.chat_id
    animation_id = update.message.animation.file_id

    # get bot from context
    bot = context.bot

    # send animation
    bot.sendAnimation(chat_id=chat_id, animation=animation_id)


def echo_document(update: Update, context: CallbackContext) -> None:
    """Echo the user document."""
    # get chat id and document id from the update
    chat_id = update.message.chat_id
    document_id = update.message.document.file_id

    # get bot from context
    bot = context.bot

    # send document
    bot.sendDocument(chat_id=chat_id, document=document_id)


def echo_audio(update: Update, context: CallbackContext) -> None:
    """Echo the user audio."""
    # get chat id and audio id from the update
    chat_id = update.message.chat_id
    audio_id = update.message.audio.file_id

    # get bot from context
    bot = context.bot

    # send audio
    bot.sendAudio(chat_id=chat_id, audio=audio_id)


def echo_location(update: Update, context: CallbackContext) -> None:
    """Echo the user location."""
    # get chat id and location from the update
    chat_id = update.message.chat_id
    location = update.message.location

    # get bot from context
    bot = context.bot

    # send location
    bot.sendLocation(chat_id=chat_id, latitude=location.latitude, longitude=location.longitude)


def echo_contact(update: Update, context: CallbackContext) -> None:
    """Echo the user contact."""
    # get chat id and contact from the update
    chat_id = update.message.chat_id
    contact = update.message.contact

    # get bot from context
    bot = context.bot

    # send contact
    bot.sendContact(chat_id=chat_id, phone_number=contact.phone_number, first_name=contact.first_name)


def echo_poll(update: Update, context: CallbackContext) -> None:
    """Echo the user poll."""
    # get chat id and poll from the update
    chat_id = update.message.chat_id
    poll = update.message.poll

    # get bot from context
    bot = context.bot

    # send poll
    bot.sendPoll(chat_id=chat_id, question=poll.question, options=poll.options)


def echo_dice(update: Update, context: CallbackContext) -> None:
    """Echo the user dice."""
    # get chat id and dice from the update
    chat_id = update.message.chat_id
    dice = update.message.dice

    # get bot from context
    bot = context.bot

    # send dice
    bot.sendDice(chat_id=chat_id, emoji=dice.emoji)
