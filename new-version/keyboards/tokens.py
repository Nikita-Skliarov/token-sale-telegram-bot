from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from config import TOKENS

tokens_keyboard = [
    [InlineKeyboardButton(token[0], callback_data=token[0])]
    for token in TOKENS
]
tokens_keyboard_m = InlineKeyboardMarkup(tokens_keyboard)