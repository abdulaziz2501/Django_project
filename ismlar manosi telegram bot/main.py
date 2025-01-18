import json
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from config import token_name

TOKEN = token_name


def load_data():
    with open('ismlar_manosi.json', 'r', encoding='utf-8') as file:
        return json.load(file)

def start(update, context) -> None:
    update.message.reply_text("Salom! Ismingizni kiriting, men uning ma'nosini aytaman.")

def find_meaning(ism, data):
    for item in data:
        if item["properties"]["name"].lower() == ism.lower():
            mano = item["properties"]["meaning"].replace("'", "").replace('"', "")
            return mano
    return None

def handle_name(update, context) -> None:
    try:
        ism = update.message.text.strip()
        data = load_data()
        mano = find_meaning(ism, data)
        if mano:
            update.message.reply_text(f"{ism.capitalize()} ismining ma'nosi: {mano}")
        else:
            update.message.reply_text("Kechirasiz, bu ism uchun ma'no topilmadi.")
    except Exception as e:
        update.message.reply_text("Xato yuz berdi. Iltimos, yana urinib ko'ring.")

def main() -> None:
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text, handle_name))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
