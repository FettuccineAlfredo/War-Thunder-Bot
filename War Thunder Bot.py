import discord

TOKEN = ''

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!warn'):
        msg = '<@214930153145499648> Be careful! War Thunder has been detected as a virus and you are being warned to close it now!'.format(message)
        await client.send_message(message.channel, msg)

client.run(TOKEN)
