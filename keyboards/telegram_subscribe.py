from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from config import CHANNELS

telegram_subscribe_keyboard = [
    [InlineKeyboardButton(channel[0], url=channel[1])]
    for channel in CHANNELS
]

telegram_subscribe_keyboard.append([InlineKeyboardButton("Проверить подписки", callback_data="sell_selected_token")])

telegram_subscribe_keyboard_m = InlineKeyboardMarkup(telegram_subscribe_keyboard)