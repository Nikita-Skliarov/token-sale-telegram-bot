import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from handlers.start import Start

TOKEN = '7368447977:AAGcMF8ZpQNfDeu_NWxWZ0bAGU5qf7zlzaw'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', Start)
    application.add_handler(start_handler)
    
    application.run_polling()