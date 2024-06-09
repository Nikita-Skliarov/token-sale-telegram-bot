from telegram import Update
from telegram.ext import ContextTypes

async def Status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    status = context.user_data.get("status")
    if status is not None:
        await update.callback_query.message.reply_text(status, parse_mode="Markdown")
    else:
        message = "Вы не выбрали токен для продажи."
        await update.callback_query.message.reply_text(message)
    
    await update.callback_query.answer()