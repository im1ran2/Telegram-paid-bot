from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "8217603414:AAECa3sKKrci9Wwuj8Mo2Mx0LFULvOz-LRU"
ADMIN_ID = 5887692543
GROUP_ID = -1001234567890

def start(update, context):
    update.message.reply_text(
        "🔥 Premium Group Access 🔥\n\n"
        "💰 Price: 200৳\n"
        "📲 bKash: 01600050898\n\n"
        "পেমেন্ট করে Screenshot পাঠান 👇"
    )

def receive_payment(update, context):
    user = update.message.from_user
    photo = update.message.photo[-1].file_id

    context.bot.send_photo(
        chat_id=ADMIN_ID,
        photo=photo,
        caption=f"Payment Request\nUser ID: {user.id}"
    )

    update.message.reply_text(
        "✅ Screenshot received\nAdmin approve করলে গ্রুপ লিংক পাবেন"
    )

def approve(update, context):
    if update.message.from_user.id != ADMIN_ID:
        return

    user_id = int(context.args[0])
    link = context.bot.create_chat_invite_link(
        chat_id=GROUP_ID,
        member_limit=1
    )

    context.bot.send_message(
        chat_id=user_id,
        text=f"🎉 Payment Approved!\nJoin Group:\n{link.invite_link}"
    )

updater = Updater(TOKEN)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.photo, receive_payment))
dp.add_handler(CommandHandler("approve", approve))

updater.start_polling()
updater.idle()
