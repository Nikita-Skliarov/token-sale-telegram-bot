
import logging
import json

#import json
from include.json_parse import coins_data

from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackContext

############################ KEYBOARDS MARKUPS ############

# back button
back_button = InlineKeyboardButton("🔙 Назад", callback_data="back")

# /start (default keyboard)
start_keyboard = [
    [InlineKeyboardButton("📊 Статус продажи", callback_data='sale_status')],
    [InlineKeyboardButton("💎 Продажа токенов", callback_data='token_sale')],
    #[InlineKeyboardButton("💰 Продажа криптовалюты", callback_data='crypto_sale')]
]
start_keyboard_m = InlineKeyboardMarkup(start_keyboard)

# Token sale 
token_sale_keyboard = [
    [InlineKeyboardButton(name, callback_data=name)]
    for name in coins_data.keys()
]
token_sale_keyboard_m = InlineKeyboardMarkup(token_sale_keyboard)

# Selected token sale
selected_token_keyboard = [
    [InlineKeyboardButton("💎 Продать", callback_data="sale")],
    [InlineKeyboardButton("🪙 Назад к токенам", callback_data="token_sale")],
    [InlineKeyboardButton("🏠 Домой", callback_data='home')],
]
selected_token_keyboard_m = InlineKeyboardMarkup(selected_token_keyboard)

############################ KEYBOARDS MARKUPS ############


# /start message
async def Start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = ("Приветствую!\n"
        "С помощью этого бота Вы сможете продать токены и криптовалюту.\n"
        "Чтобы продолжить, нажми на кнопку внизу и выбери следующие варианты.")
    # Check if the update is from a callback query
    if update.callback_query:
        query = update.callback_query
        await query.answer()
        await query.message.reply_text(message_text, reply_markup=start_keyboard_m)
    else:
        # If not a callback query, handle as before
        await update.message.reply_text(message_text, reply_markup=start_keyboard_m)

# Command handler for /continue
async def Token_sale(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    reply = "Выберите токен, который хотите обменять."

    # Read the JSON file and generate keyboard buttons
    try:
        await update.callback_query.message.reply_text(text=reply, reply_markup=token_sale_keyboard_m)
    
    except Exception as e:
        await update.callback_query.message.reply_text(text=f"Ошибка при чтении файла JSON: {str(e)}")
        
async def Click_on_name_token(update: Update, context: ContextTypes.DEFAULT_TYPE, coin_name: str):
    query = update.callback_query
    await query.answer()
    coin_info = coins_data[coin_name]
    message = (
        f"<b><u>{coin_name}</u></b> 🚀\n\n"
        f"<i>Цена за ({coin_info['Количество']}):</i>\n"
        f"<b>{coin_info['Цена']} $</b>\n\n"
        f"<i>В наличии!</i> 🎉\n\n"
        f"<b>🔥 Продайте сейчас и получите эксклюзивные преимущества! 🔥</b>\n"
        f"🔹 <i>Безопасные транзакции</i>\n"
        f"🔹 <i>Гарантированный рост стоимости</i>\n"
        f"🔹 <i>Поддержка 24/7</i>\n\n"
        f"<b>Не успустите шанс заработать здесь и сейчас!</b> 🚀"
    )
    await update.callback_query.message.reply_text(message, parse_mode='HTML', reply_markup=selected_token_keyboard_m)