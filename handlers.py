
import logging
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackContext

# /start message
async def Start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = ("Приветствую!\n"
                    "С помощью этого бота Вы сможете продать токены и криптовалюту.\n"
                    "Чтобы продолжить, нажми на кнопку внизу и выбери следующие варианты.")
    keyboard = [[InlineKeyboardButton("Продолжить", callback_data='continue')]]
    keyboard_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(message_text, reply_markup=keyboard_markup)

# Command handler for /continue
async def Continue(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()  # Acknowledge the callback query
    reply = "Выберите токен, который хотите обменять."
    keyboard = [
        [InlineKeyboardButton("HAMSTER", callback_data="HAMSTER")],
        [InlineKeyboardButton("MEMECOIN", callback_data="MEMECOIN")],
        [InlineKeyboardButton("MEMEFICOIN", callback_data="MEMEFICOIN")],
        [InlineKeyboardButton("TON", callback_data="TON")]
    ]
    keyboard_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text=reply, reply_markup=keyboard_markup)