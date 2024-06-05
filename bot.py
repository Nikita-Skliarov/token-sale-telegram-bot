import json

# commands.py has all replies to / commands
from handlers import Start, Continue

# telegram bot library
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# init prices
with open("prices.json", "r", encoding="utf-8") as json_data:
    coins_data = json.load(json_data)

if __name__ == '__main__':
    application = ApplicationBuilder().token('7370415604:AAH21Q0Iv9FPdGD0eCZPhUqGt58PrmyRHDk').build()
    
    start_handler = CommandHandler('Start', Start)
    continue_handler = CallbackQueryHandler(Continue, pattern="continue")
    
    # add handlers for json tokens names
    for name in coins_data:
        token_handler = CallbackQueryHandler(name, pattern=name)
    application.add_handler(start_handler)
    application.add_handler(continue_handler)
    application.run_polling()