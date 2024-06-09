import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler

# handlers
from handlers.start import Start
from handlers.tokens import ShowTokens

# config arrays + bot token
from private.token import TOKEN
from config import TOKENS


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    ### make handlers
    start_handler = CommandHandler('start', Start)
    tokens_handler = CallbackQueryHandler(ShowTokens, pattern="token_sale")
    
    ### append handlers to application
    application.add_handler(start_handler)
    application.add_handler(tokens_handler)
    
    application.run_polling()