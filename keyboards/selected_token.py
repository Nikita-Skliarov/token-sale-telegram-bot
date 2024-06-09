from telegram import InlineKeyboardButton, InlineKeyboardMarkup

selected_token_keyboard = [
    [InlineKeyboardButton("💎 Продать", callback_data="sell_selected_token")],
    [InlineKeyboardButton("🏘 Домой", callback_data="home")]
]

selected_token_keyboard_m = InlineKeyboardMarkup(selected_token_keyboard)