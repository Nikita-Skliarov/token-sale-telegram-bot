from telegram import Update
from telegram.ext import ContextTypes
from keyboards.start import start_keyboard_m

async def Start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = (
        "Приветствую! 💰\n"
        "С помощью этого бота Вы сможете продать токены и криптовалюту.\n"
        "Для того что бы продолжить, нажмите на кнопку ниже и выберите следующие варианты."
    )
    if update.callback_query:
        query = update.callback_query
        await query.answer()
        await query.message.reply_text(message_text, reply_markup=start_keyboard_m)
    else:
        await update.message.reply_text(message_text, reply_markup=start_keyboard_m)
    await update.callback_query.answer()