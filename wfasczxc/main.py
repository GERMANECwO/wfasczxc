import telebot
from telebot.types import Message

TOKEN = "6477608399:AAHOtPmfZUd6JSm9KqzEIKrrLelxttBnHnw"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["/start"])
def handle_start(message: Message):
    bot.send_message(
        message.chat.id,
        "Привет!",
    )


bot.polling()
