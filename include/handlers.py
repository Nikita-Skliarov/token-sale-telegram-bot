
import logging
import json

#import json
from include.json_parse import coins_data

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
        keyboard = [
            [InlineKeyboardButton(name, callback_data=name)]
            for name in coins_data.keys()
        ]
        
        keyboard_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=reply, reply_markup=keyboard_markup)
    
    except Exception as e:
        await query.edit_message_text(text=f"Ошибка при чтении файла JSON: {str(e)}")
        
async def Click_on_name_token(update: Update, context: ContextTypes.DEFAULT_TYPE, coin_name: str):
    query = update.callback_query
    await query.answer()
    coin_info = coins_data[coin_name]
    message = (
        f"<b><u>{coin_name}</u></b>\n\n"
        f"<i>Цена за ({coin_info['Количество']}):</i>\n"
        f"<b>{coin_info['Цена']} $</b>\n\n"
        f"<i>В наличии!</i>"
    )
    await update.callback_query.message.reply_text(message, parse_mode='HTML')
