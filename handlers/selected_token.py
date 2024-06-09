from telegram import Update
from telegram.ext import ContextTypes
from keyboards.selected_token import selected_token_keyboard_m
from config import TOKENS

async def ShowSelectedCoin(update: Update, context: ContextTypes.DEFAULT_TYPE, token_name):
     # Find the token details in TOKENS
    token_details = next((token for token in TOKENS if token[0] == token_name), None)
    
    context.user_data["selected_token"] = token_name
    
    if token_details:
        message = (
            f"*{token_name}* 🚀\n"
            f"Цена за 1.000.000: *{token_details[1]}* $\n"
            f"В наличии! 🎉"
        )
        await update.callback_query.message.reply_text(message, reply_markup=selected_token_keyboard_m, parse_mode="Markdown")
    await update.callback_query.answer()
    