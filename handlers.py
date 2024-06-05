
import logging
import json
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

    # Read the JSON file and generate keyboard buttons
    try:
        with open("prices.json", "r", encoding="utf-8") as json_data:
            coins_data = json.load(json_data)
        
        keyboard = [
            [InlineKeyboardButton(name, callback_data=name)]
            for name in coins_data.keys()
        ]
        
        keyboard_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=reply, reply_markup=keyboard_markup)
    
    except Exception as e:
        await query.edit_message_text(text=f"Ошибка при чтении файла JSON: {str(e)}")
        