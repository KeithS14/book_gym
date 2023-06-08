#from telegram import Bot
import telegram
import asyncio
async def main():
    api_key = '6008231050:AAGAZ68BXofK5n14uzC7zdQsrLlYYoxpDME'
    user_id = '6087124042'

    #bot = Bot(token=api_key)
    bot = telegram.Bot(token=api_key)
    await bot.send_message(chat_id=user_id, text='goodbye world3')
asyncio.run(main())