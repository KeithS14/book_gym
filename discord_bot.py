# python3 -m pip install discord
import discord
import asyncio



class MyBot(discord.Client):
    def __init__(self, intents ,message):
        super().__init__(intents=intents)
        self.message = message
    
    async def on_ready(self):
        
        print(f'Logged in as {self.user.name} ({self.user.id})')
        
        # Set your Discord server ID and general channel ID
        server_id = 1113204216413048914
        general_channel_id = 1113204217017016352
        # Get the server and general channel
        server = self.get_guild(server_id)
        general_channel = server.get_channel(general_channel_id)
        
        # Send a Discord notification
        user = await bot.fetch_user(350345815824531467)
        mention = user.mention 
        tagged_message = f"{mention} {self.message}"
        await general_channel.send(tagged_message)
        
        await self.close()
# Set your Discord bot token
BOT_TOKEN = 'MTExMzE5NjY2OTE0ODg2MDQ5Ng.G9Hi2o.CXKLfSTDl1V1ylO3-2YiVisPbGnA4MiibJhfSU'

# Create an instance of your bot
bot = MyBot(intents=discord.Intents.default(),message="Test")

# Run the bot
bot.run(BOT_TOKEN)



