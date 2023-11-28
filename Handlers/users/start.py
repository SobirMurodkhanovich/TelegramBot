def start_handler(update, context):
    user_name = update.message.from_user.first_name
    update.message.reply_text(
        text=f"<b>Assalomu alaykum {user_name}</b>",
        parse_mode='HTML'
    )
