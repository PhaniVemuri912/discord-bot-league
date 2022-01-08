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
    if '*roll' in message.content.lower():
        message_string = message.content
        names = message_string.split()
        names.remove('*roll')
        if len(names) < 5:
            new_no_names = 5 - len(names)
            while new_no_names > 0:
                names.append("random "+str(5-new_no_names))
                new_no_names = new_no_names - 1
        lanes_returned = rls(names)
        await message.channel.send(lanes_returned)


def rls(names):
    lanes = ['Top','ADC','Support','Jungle','Mid']
    name_and_lanes = []
    i = 0
    j = 5
    selected_lanes = []
    while i <= 4:
        if len(lanes) > 1:
            randselection = random.randint(0,j-1)
        else:
            randselection = 0
        selected_lanes.append(lanes[randselection])
        name_and_lanes.append(names[i]+"-"+lanes[randselection])
        lanes.remove(lanes[randselection])
        i = i+1
        j = j-1
    return name_and_lanes

client.run(TOKEN)


