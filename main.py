import sqlite3
from API_token import token
from telebot.async_telebot import AsyncTeleBot
import asyncio
import pause
import datetime as dt


dbGenScript = open("generate_db.sql", 'r')

connection = sqlite3.connect('remindMe.sqlite3')
cursor = connection.cursor()

bot = AsyncTeleBot(token, parse_mode=None)

# create and send "the" scheduled daily message 
async def sendReminders(message, sendTime):
    pause.until(sendTime)
    await bot.send_message(message.chat.id, "u forgor smth")


@bot.message_handler(commands=['start'])
async def start(message):
    await bot.reply_to(message, "Test")
    # await bot.reply_to(message, )
    
    nextReminderData = dt.datetime.today().now() + dt.timedelta(seconds=15)
    while True:
        await sendReminders(message, nextReminderData)
        nextReminderData += dt.timedelta(seconds=20)
    



def init():
    script = dbGenScript.read().split(';')
    for query in script:
        cursor.execute(query)

if __name__ == "__main__":
    init()
    print("Start polling")
    asyncio.run(bot.polling())