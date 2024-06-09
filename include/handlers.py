import logging
import random
import json
from include.json_parse import coins_data
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes, CallbackContext, ConversationHandler

TOKEN_SALE_PROCEDURE, TOKEN_COUNT, CHECK_SUBSCRIPTION = range(3)

# Load sponsors data
with open('include/sponsors.json', 'r', encoding='utf-8') as file:
    sponsors_data = json.load(file)

############################ KEYBOARDS MARKUPS ############

start_keyboard = [
    [InlineKeyboardButton("📊 Статус продажи", callback_data='sale_status')],
    [InlineKeyboardButton("💎 Продажа токенов", callback_data='token_sale')]
]
start_keyboard_m = InlineKeyboardMarkup(start_keyboard)

token_sale_keyboard = [
    [InlineKeyboardButton(name, callback_data=name)]
    for name in coins_data.keys()
]
token_sale_keyboard_m = InlineKeyboardMarkup(token_sale_keyboard)

selected_token_keyboard = [
    [InlineKeyboardButton("💎 Продать", callback_data="sale")],
    [InlineKeyboardButton("🪙 Назад к токенам", callback_data="token_sale")],
    [InlineKeyboardButton("🏠 Домой", callback_data='home')],
]
selected_token_keyboard_m = InlineKeyboardMarkup(selected_token_keyboard)

submit_token_buy_keyboard = [
    [InlineKeyboardButton("🆗", callback_data="set_queue")],
    [InlineKeyboardButton("🚫", callback_data="home")]
]

submit_token_buy_keyboard_m = InlineKeyboardMarkup(submit_token_buy_keyboard)

order_result_keyboard = [
    [InlineKeyboardButton("🏠 Домой", callback_data='home')]
]

order_result_keyboard_m = InlineKeyboardMarkup(order_result_keyboard)

############################ KEYBOARDS MARKUPS ############

async def Start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = (
        "Приветствую!\n"
        "С помощью этого бота Вы сможете продать токены и криптовалюту.\n"
        "Чтобы продолжить, нажми на кнопку внизу и выбери следующие варианты."
    )
    if update.callback_query:
        query = update.callback_query
        await query.answer()
        await query.message.reply_text(message_text, reply_markup=start_keyboard_m)
    else:
        await update.message.reply_text(message_text, reply_markup=start_keyboard_m)

async def Token_sale(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    reply = "Выберите токен, который хотите обменять."
    try:
        await update.callback_query.message.reply_text(text=reply, reply_markup=token_sale_keyboard_m)
    except Exception as e:
        await update.callback_query.message.reply_text(text=f"Ошибка при чтении файла JSON: {str(e)}")

async def Click_on_name_token(update: Update, context: ContextTypes.DEFAULT_TYPE, coin_name: str):
    query = update.callback_query
    await query.answer()
    coin_info = coins_data[coin_name]
    context.user_data['selected_token'] = coin_name
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

async def Token_sale_procedure(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    coin_name = context.user_data.get('selected_token')
    if coin_name:
        message = f"Введите число токенов, которое вы хотите продать (мин. 100.000) для {coin_name}"
        await update.callback_query.message.reply_text(message)
        return TOKEN_COUNT
    else:
        await update.callback_query.message.reply_text("Ошибка: не выбран токен для продажи.")
        return ConversationHandler.END

async def Handle_token_count(update: Update, context: ContextTypes.DEFAULT_TYPE):
    attempts = context.user_data.get("attempts", 3)
    if attempts == 0:
        await update.message.reply_text("Вы исчерпали все попытки. Пожалуйста, начните сначала.")
        context.user_data["attempts"] = 3
        return ConversationHandler.END
    
    token_count = update.message.text
    try:
        token_count = int(token_count)
        if token_count >= 100000:
            coin_name = context.user_data.get('selected_token')
            message = f"Вы хотите продать {token_count:,.2f} {coin_name}?"
            context.user_data["token_count"] = token_count
            await update.message.reply_text(message, reply_markup=submit_token_buy_keyboard_m)
        else:
            message = "Число токенов должно быть не меньше 100.000"
            context.user_data["attempts"] = attempts - 1
            await update.message.reply_text(message)
    except ValueError:
        message = "Пожалуйста, введите корректное число."
        context.user_data["attempts"] = attempts - 1
        await update.message.reply_text(message)
        
    return TOKEN_COUNT

async def Check_subscription(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    sponsor = sponsors_data['tg-channels']['Lord Crypto Exchange']
    invite_link = sponsor['invintation-link']
    
    message = (
        "Для завершения продажи токенов, пожалуйста, подпишитесь на наших партнёров и спонсоров.\n"
        "После подписки, нажмите кнопку 'Проверить подписку'."
    )
    subscribe_keyboard = [
        [InlineKeyboardButton("Подписаться на партнёра", url=invite_link)],
        [InlineKeyboardButton("Проверить подписку", callback_data='check_subscription')]
    ]
    subscribe_keyboard_m = InlineKeyboardMarkup(subscribe_keyboard)
    await query.message.reply_text(message, reply_markup=subscribe_keyboard_m)
    return CHECK_SUBSCRIPTION

async def Confirm_subscription(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    # Replace this with actual API calls to check the subscription status
    sponsor = sponsors_data['tg-channels']['Lord Crypto Exchange']
    channel_id = sponsor['channel-id']
    
    chat_member = await context.bot.get_chat_member(chat_id=channel_id, user_id=query.from_user.id)
    await query.message.reply_text(chat_member)
    
    def is_subscribed(chat_id, user_id):
        try:
            chat_member_status = chat_member.status in ['member', 'administrator', 'creator']
            return True
        except Exception as e:
            return False

    if is_subscribed(channel_id, query.from_user.id):
        await query.message.reply_text("Подписан.")
        await Submit_token_buy(update, context)
    else:
        await query.message.reply_text("Пожалуйста, подпишитесь на наших партнёров и спонсоров для завершения продажи.")
        return CHECK_SUBSCRIPTION

async def Submit_token_buy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    token_name = context.user_data.get("selected_token")
    token_count = context.user_data.get("token_count")
    token_price = coins_data[token_name]["Цена"]
    token_price_count = coins_data[token_name]["Количество"]
    total_amount = token_count / token_price_count * token_price
    
    message = (
        f"✅ *Ваш заказ успешно отправлен!* ✅\n\n"
        f"Токен: *{token_name}*\n"
        f"Количество: *{token_count:,.2f}*\n"
        f"Сумма выплаты: *{total_amount:,.2f} $*\n\n"
    )
    
    context.user_data["sale_status"] = message
    await update.callback_query.message.reply_text(message, parse_mode='Markdown', reply_markup=order_result_keyboard_m)

async def Sale_status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    message = context.user_data.get("sale_status")
    await update.callback_query.message.reply_text(message, parse_mode='Markdown', reply_markup=order_result_keyboard_m)