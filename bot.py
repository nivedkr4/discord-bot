import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'✅ Logged on as {self.user}!')

    async def on_message(self, message):
        
        if message.author == self.user:
            return

       
        if message.content.startswith('Who do you love?'):
            await message.channel.send('Advika ♡')

# Enable message content so bot can read messages
intents = discord.Intents.default()
intents.message_content = True

# Create bot client
client = MyClient(intents=intents)

# Run bot with your token (keep this secret!)
client.run('MTQwODgzMDk5NTgwOTA0NjY5MA.GIwA1B.VJqvOKqVnM1BosmStua7SqWV5AjpcpC1cVoIys')
