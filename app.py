import logging
from flask import Flask, request
from telegram import (ChatAction, ReplyKeyboardMarkup,
                      ReplyKeyboardRemove, Bot, Update)


from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler, run_async, Dispatcher)
import time
import os

PORT = int(os.environ.get('PORT','8443')) 
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


TOKEN = "Hidden Confidential Check in Google Keep" 

bot = Bot(TOKEN) 

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello'


@app.route(f'/{TOKEN}', methods=['GET', 'POST'])
def webhook():
    """ webhook view which receives updates from telegram """
    # create update object from json-format request data
    update = Update.de_json(request.get_json(), bot)
    # proces update
    dp.process_update(update)
    return "ok"


ONE, TWO, THREE, FOUR, ONE_temp1, ONE_temp2 = range(6)

# @run_async


def start(update, context):
    reply_keyboard = [['Boy', 'Girl', 'Other']]
    bot.send_message(update.message.chat_id,
                     "If you are feeling depressed you have come to the best place in the world",
                     )
    bot.send_chat_action(update.message.chat_id, action=ChatAction.TYPING)
    time.sleep(1)
    bot.send_message(update.message.chat_id,
                     "I have everything in the world but I need a friend like you.",
                     )
    bot.send_chat_action(update.message.chat_id, action=ChatAction.TYPING)
    time.sleep(1)
    bot.send_message(update.message.chat_id,
                     "Please tell me your name.",
                     )
    return ONE


def second(update, context):
    user = update.message.from_user
    #logger.info("Gender of %s: %s", user.first_name, update.message.text)
    update.message.reply_text('I haven’t heard a beautiful name like that in years.'
                              'Tell me your three wishes',
                              )
    return TWO


def third(update, context):
    user = update.message.from_user
    reply_keyboard = [['YES']]
    #logger.info("Gender of %s: %s", user.first_name, update.message.text)
    update.message.reply_text('Your wishes are amazing. Your intentions are great.\nBut remember, if you fail and become depressed ever, which you might become never, be aware of not doing the following :\n'

                              )
    bot.send_chat_action(update.message.chat_id, action=ChatAction.TYPING)
    time.sleep(2)
    update.message.reply_text(
        '\n\nDenying the outcome \n\nBecome angry with yourself \n\nTry to convince yourself that you worth it \n\n Silly depression')

    bot.send_chat_action(update.message.chat_id, action=ChatAction.TYPING)
    time.sleep(1)

    update.message.reply_text('Just accept the outcome and shoot for the moon.'
                              )
    bot.send_chat_action(update.message.chat_id, action=ChatAction.TYPING)
    time.sleep(2)
    update.message.reply_text('Do you want to create new connections?',
                              reply_markup=ReplyKeyboardMarkup(
                                  reply_keyboard, one_time_keyboard=True)
                              )

    return THREE


def fouth(update, context):
    user = update.message.from_user
    #logger.info("Gender of %s: %s", user.first_name, update.message.text)
    update.message.reply_text('Newton created gravity by connecting two facts. One was known and the other was unknown. \nThe known fact was apple falls downwards; and the unknown fact was what made it fell downwards. \nWhen he assembled the two concepts, he discovered gravity. \n\nIt was his new connection.', reply_markup=ReplyKeyboardRemove()
                              )
    bot.send_chat_action(update.message.chat_id, action=ChatAction.TYPING)
    time.sleep(1)
    update.message.reply_text('What’s yours?'
                              )
    return FOUR


def cancel(update, context):
    user = update.message.from_user
    update.message.reply_text('Bye! I hope we can talk again some day.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


def tempreply(update, context):
    return ONE_temp1


def tempreply1(update, context):
    return ONE_temp2


def random(update, context):
    update.message.reply_text(
        "I'm always with my friend.\nDon't forget to come back whenever you feel down\n\nWrite /start to start again my friend")
    return ConversationHandler.END



def error(update , context):
  logger.error("Update '%s' caused error '%s', update , update.error")

 # def error(update, context):
 #  logger.error("Update '%s' caused error '%s'", update, update.error)







def main():

  """Start the bot."""
  # Create the Updater and pass it your bot's token.
  # Make sure to set use_context=True to use the new context based callbacks
  # Post version 12 this will no longer be necessary
  # bot = Bot(TOKEN)
  updater = Updater(
      TOKEN, use_context=True)

  # Get the dispatcher to register handlers
  dp = updater.dispatcher

  # on different commands - answer in Telegram

  conv_handler = ConversationHandler(



    entry_points=[CommandHandler('start', start)],

    states={
        ONE: [MessageHandler(Filters.text, second)],

        TWO: [MessageHandler(Filters.text, tempreply)],

        ONE_temp1: [MessageHandler(Filters.text, tempreply1)],

        ONE_temp2: [MessageHandler(Filters.text, third)],


        THREE: [MessageHandler(Filters.regex('^(YES)$'), fouth)],

        FOUR: [MessageHandler(Filters.text | Filters.sticker, random)]

    },

    fallbacks=[CommandHandler('cancel', cancel)]
  )
  #dp.add_handler(MessageHandler(Filters.text | Filters.sticker, random))
  dp.add_handler(conv_handler)

  

  # Start the Bot
  updater.start_webhook(listen="0.0.0.0",
                        port=PORT,
                        url_path=TOKEN)
  # updater.bot.set_webhook(url=settings.WEBHOOK_URL)
  updater.bot.set_webhook("https://whispering-bayou-03397.herokuapp.com/" + TOKEN)

  # Run the bot until you press Ctrl-C or the process receives SIGINT,
  # SIGTERM or SIGABRT. This should be used most of the time, since
  # start_polling() is non-blocking and will stop the bot gracefully.
  updater.idle()


if __name__ == '__main__':
    main()










### Previous Part ###

############################  Main Part   #########################################
# bot = Bot(TOKEN)

# try:
#   bot.set_webhook("https://boiling-hamlet-54033.herokuapp.com/"+TOKEN)
# except Exception as e:
#   raise e




# dp = Dispatcher(bot, None, use_context=True)

# #job_queue = JobQueue()
# # job_queue.set_dispatcher(dp)
# # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
# conv_handler = ConversationHandler(
#     entry_points=[CommandHandler('start', start)],

#     states={
#         ONE: [MessageHandler(Filters.text, second)],

#         TWO: [MessageHandler(Filters.text, tempreply)],

#         ONE_temp1: [MessageHandler(Filters.text, tempreply1)],

#         ONE_temp2: [MessageHandler(Filters.text, third)],


#         THREE: [MessageHandler(Filters.regex('^(YES)$'), fouth)],

#         FOUR: [MessageHandler(Filters.text | Filters.sticker, random)]

#     },

#     fallbacks=[CommandHandler('cancel', cancel)]
# )
# #dp.add_handler(MessageHandler(Filters.text | Filters.sticker, random))
# dp.add_handler(conv_handler)
# dp.add_error_handler(error)

# if __name__ == '__main__':
#     app.run(port=8443)
