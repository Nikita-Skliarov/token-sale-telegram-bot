import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler

# handlers
from handlers.start import Start
from handlers.tokens import ShowTokens
from handlers.selected_token import ShowSelectedCoin
from handlers.sell_selected_token import Sell_selected_token
from handlers.status import Status

# config arrays + bot token
from private.token import TOKEN
from config import TOKENS


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    # /start
    start_handler = CommandHandler('start', Start)
    application.add_handler(start_handler)
    
    # go home
    home_handler = CallbackQueryHandler(Start, pattern="home")
    application.add_handler(home_handler)
    
    # status
    status_handler = CallbackQueryHandler(Status, pattern="status")
    application.add_handler(status_handler)
    
    # show tokens 
    tokens_handler = CallbackQueryHandler(ShowTokens, pattern="token_sale")
    application.add_handler(tokens_handler)
    
    # selected token
    for token in TOKENS:
        pattern = token[0]
        token_handler = CallbackQueryHandler(
            lambda update, context, token_name=pattern: ShowSelectedCoin(update, context, token_name),
            pattern=pattern
        )
        application.add_handler(token_handler)
    
    # sell selected token 
    sell_selected_token_handler = CallbackQueryHandler(Sell_selected_token, pattern="sell_selected_token")
    application.add_handler(sell_selected_token_handler)
    
    application.run_polling()