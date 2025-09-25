import telebot
import random

# ТУТ встав свій токен від BotFather
API_TOKEN = "8024668338"

bot = telebot.TeleBot(API_TOKEN)

# Команда /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привіт 👋! Я твій розважальний бот.\nНапиши 'гра', щоб пограти в Камінь-Ножиці-Папір.")

# Реакція на повідомлення
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    text = message.text.lower()
    if text == "гра":
        bot.send_message(message.chat.id, "Вибери: камінь / ножиці / папір")
    elif text in ["камінь", "ножиці", "папір"]:
        options = ["камінь", "ножиці", "папір"]
        bot_choice = random.choice(options)
        result = ""
        if text == bot_choice:
            result = "Нічия 🤝"
        elif (text == "камінь" and bot_choice == "ножиці") \
             or (text == "ножиці" and bot_choice == "папір") \
             or (text == "папір" and bot_choice == "камінь"):
            result = "Ти виграв! 🎉"
        else:
            result = "Бот виграв! 😈"
        bot.send_message(message.chat.id, f"Бот вибрав: {bot_choice}\n{result}")
    else:
        bot.send_message(message.chat.id, "Я тебе не зрозумів 🤔. Напиши 'гра'.")

# Запускаємо бота
bot.polling()
