from telegram import Bot, Update
from telegram.ext import ContextTypes
from keyboards.sell_selected_token import sell_selected_token_keyboard_m
from keyboards.telegram_subscribe import telegram_subscribe_keyboard_m
from config import CHANNELS

async def Sell_selected_token(update: Update, context: ContextTypes.DEFAULT_TYPE):
    is_subscribed = await Check_subs(update, context)
    if not is_subscribed:
        message_text = (
        f"Чтобы продолжить, подпишитесь пожалуйста на наших партнеров и спонсоров.\n"
        f"Для проверки, нажмите на кнопку *'Проверить подписки'*"
        )
        await update.callback_query.message.reply_text(message_text, reply_markup=telegram_subscribe_keyboard_m, parse_mode="Markdown")
    else:
        selected_token = context.user_data.get("selected_token")
        message_text = (
        f"Вы выбрали *{selected_token}* как токен, который хотите продать. \n"
        f"В скором времени с Вами свяжется поддержка, чтобы выяснить реквизиты для получения, количество и произвести продажу."
        )
        context.user_data["status"] = message_text
        await update.callback_query.message.reply_text(message_text, reply_markup=sell_selected_token_keyboard_m, parse_mode="Markdown")
    await update.callback_query.answer()
    


async def Check_subs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    for channel in CHANNELS:
        channel_id = channel[2]
        try:
            chat_member = await context.bot.get_chat_member(chat_id=channel_id, user_id=user_id)
            if chat_member.status not in ['member', 'administrator', 'creator']:
                return False
        except Exception as e:
            print(f"Error checking subscription for channel {channel_id}: {e}")
            return False
    return True