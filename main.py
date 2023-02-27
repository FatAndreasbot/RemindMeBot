import sqlite3
from API_token import token
import telebot as tb

dbGenScript = open("generate_db.sql", 'r')

connection = sqlite3.connect('remindMe.sqlite3')
cursor = connection.cursor()

bot = tb.TeleBot(token, parse_mode=None)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Test")


def init():
    script = dbGenScript.read().split(';')
    for query in script:
        cursor.execute(query)

if __name__ == "__main__":
    init()
    bot.infinity_polling()