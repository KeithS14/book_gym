# python3 -m pip install discord
import discord
import asyncio



async def send_dm_message(bot_token, user_id, message):
    intents = discord.Intents.default()
    bot = discord.Client(intents=intents)

    @bot.event
    async def on_ready():
        user = await bot.fetch_user(user_id)
        await user.send(message)
        await bot.logout()
        loop.stop()

    await bot.start(bot_token)

# Set your Discord bot token and your user ID
BOT_TOKEN = 'MTExMzE5NjY2OTE0ODg2MDQ5Ng.G9Hi2o.CXKLfSTDl1V1ylO3-2YiVisPbGnA4MiibJhfSU'
USER_ID = '350345815824531467'

# Prompt the user to enter a message
message = "Test2"



loop = asyncio.get_event_loop()
loop.run_until_complete(send_dm_message(BOT_TOKEN, USER_ID, message))
loop.close() 