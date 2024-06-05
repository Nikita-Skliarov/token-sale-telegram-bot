import json

#import json
from include.json_parse import coins_data

# commands.py has all replies to / commands
from include.handlers import Start, Token_sale, Click_on_name_token

# telegram bot library
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    application = ApplicationBuilder().token('7370415604:AAH21Q0Iv9FPdGD0eCZPhUqGt58PrmyRHDk').build()
    
    start_handler = CommandHandler('Start', Start)
    home_handler = CallbackQueryHandler(Start, pattern="home")
    token_sale_handler = CallbackQueryHandler(Token_sale, pattern="token_sale")
    
    application.add_handler(home_handler)
    application.add_handler(start_handler)
    application.add_handler(token_sale_handler)
        # Add handlers for each token name
    for name in coins_data:
        handler = CallbackQueryHandler(lambda update, context, name=name: Click_on_name_token(update, context, name), pattern=name)
        application.add_handler(handler)  
    application.run_polling()