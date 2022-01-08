import random
import os
import discord

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")
client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the auto fill league!'
    )

@client.event
async def on_message(message):
    if message.content.lower() == 'roll-the-dice':
        lanes_returned = rls()
        await message.channel.send(lanes_returned)

def rls():
    lanes = ['Top','ADC','Support','Jungle','Mid']
    i = 5
    selected_lanes = []
    while i > 0:
        if len(lanes) > 1:
            randselection = random.randint(0,i-1)
        else:
            randselection = 0
        selected_lanes.append(lanes[randselection])
        lanes.remove(lanes[randselection])
        i = i-1
    return selected_lanes

client.run(TOKEN)


