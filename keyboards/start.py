from telegram import InlineKeyboardButton, InlineKeyboardMarkup

start_keyboard = [
    [InlineKeyboardButton("📊 Статус продажи", callback_data='status')],
    [InlineKeyboardButton("💎 Продажа токенов", callback_data='token_sale')]
]
start_keyboard_m = InlineKeyboardMarkup(start_keyboard)