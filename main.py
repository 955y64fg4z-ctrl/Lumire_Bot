import telebot

TOKEN =  HTTP API:
8919637860:AAEyjjl9VZVtpIE-V7x2oPzeOyrvh4NkKDo
ADMIN_ID = 5457891099

bot = telebot.TeleBot(TOKEN)

users = {}

questions = [
    "🎮 Напиши свой ник в Roblox:",
    "🎂 Сколько тебе лет?",
    "🌍 Из какой ты страны/города?",
    "🏠 Почему хочешь вступить в Roblox хаус?"
]

@bot.message_handler(commands=["start"])
def start(message):
    users[message.chat.id] = {"step": 0, "answers": []}
    bot.send_message(message.chat.id, questions[0])

@bot.message_handler(func=lambda m: m.chat.id in users)
def get_answer(message):
    user = users[message.chat.id]

    user["answers"].append(message.text)
    user["step"] += 1

    if user["step"] < len(questions):
        bot.send_message(message.chat.id, questions[user["step"]])
    else:
        text = "🏠 Новая анкета Roblox хаус:\n\n"
        
        for i in range(len(questions)):
            text += f"{questions[i]}\n➡️ {user['answers'][i]}\n\n"

        bot.send_message(ADMIN_ID, text)
        bot.send_message(message.chat.id, "✅ Анкета отправлена! Ожидай ответа.")

        del users[message.chat.id]


bot.infinity_polling()
