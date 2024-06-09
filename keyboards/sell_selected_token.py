from telegram import InlineKeyboardButton, InlineKeyboardMarkup

sell_selected_token_keyboard = [
    [InlineKeyboardButton("🏘 Домой", callback_data="home")]
]

sell_selected_token_keyboard_m = InlineKeyboardMarkup(sell_selected_token_keyboard)