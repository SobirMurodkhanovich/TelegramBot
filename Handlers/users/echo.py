def echo_handler(update, context):
    """Userdan kelgan matnni o'ziga qaytarib yuboruchi funksiya"""
    text = update.message.text
    update.message.reply_text(
        text=text
    )
