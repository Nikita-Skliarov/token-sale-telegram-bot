from telegram import Update
from telegram.ext import ContextTypes

async def Status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    status = context.user_data.get("status")
    
    if status is not None:
        message = status
    else:
        message = "Вы не выбрали токен для продажи."

    if update.callback_query:
        await update.callback_query.message.reply_text(message, parse_mode="Markdown")
        await update.callback_query.answer()
    elif update.message:
        await update.message.reply_text(message, parse_mode="Markdown")