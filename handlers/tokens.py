from telegram import Update
from telegram.ext import ContextTypes
from keyboards.tokens import tokens_keyboard_m

async def ShowTokens(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = "Выберите токен, которые хотите обменять:"
    await update.callback_query.message.reply_text(message, reply_markup=tokens_keyboard_m)