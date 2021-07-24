import logging
import requests
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)




def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    
    update.message.reply_text('Top level insults\nEnter anything to get started')


def help_command(update: Update, context: CallbackContext) -> None:
    
    update.message.reply_text('Type anything to get roasted')

def get_insult():
    contents = requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=json').json()
    insult = contents['insult']
    return insult

def insult(update: Update, context: CallbackContext) -> None:
    
    update.message.reply_text(get_insult())


def main() -> None:
    """Start the bot."""
    
    updater = Updater("1934144890:AAG5hbbR6fiOKy2iJBq9oJu5rK8HLNi4OWg")

    
    dispatcher = updater.dispatcher

    
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, insult))

    
    updater.start_polling()

    
    
    
    updater.idle()


if __name__ == '__main__':
    main()