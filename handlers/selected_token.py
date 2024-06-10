from telegram import Update
from telegram.ext import ContextTypes
from keyboards.selected_token import selected_token_keyboard_m
from config import TOKENS
from handlers.sell_selected_token import Sell_selected_token

async def ShowSelectedCoin(update: Update, context: ContextTypes.DEFAULT_TYPE, token_name):
     # Find the token details in TOKENS
    token_details = next((token for token in TOKENS if token[0] == token_name), None)
    
    context.user_data["selected_token"] = token_name
    
    if token_details:
        try:
            message = (
            f"*{token_name}* 🚀\n"
            f"Цена за 1.000.000: *{token_details[1]}* $\n"
            )
            await update.callback_query.message.reply_text(message, reply_markup=selected_token_keyboard_m, parse_mode="Markdown")
        except Exception: # if there is no description, skip price show
            await Sell_selected_token(update, context)
            
    await update.callback_query.answer()
    