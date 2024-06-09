from telegram import Update
from telegram.ext import ContextTypes
from keyboards.sell_selected_token import sell_selected_token_keyboard_m

async def Sell_selected_token(update: Update, context: ContextTypes.DEFAULT_TYPE):
    selected_token = context.user_data.get("selected_token")
    message_text = (
        f"Вы выбрали *{selected_token}* как токен, который хотите продать. \n"
        f"В скором времени с вами свяжется поддержка, чтобы выяснить реквизиты для получения, количество и произвести продажу."
    )
    context.user_data["status"] = message_text
    await update.callback_query.message.reply_text(message_text, reply_markup=sell_selected_token_keyboard_m, parse_mode="Markdown")
