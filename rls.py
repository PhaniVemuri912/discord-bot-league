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
    if '*select' in message.content.lower():
        message_string = message.content
        names = message_string.split()
        names.remove('*select')
        hero_selected = rcs(names[0])
        await message.channel.send(hero_selected)     
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


def rcs(name):
    top = ['Aatrox', 'Akali', 'Akshan', 'Camille', 'Cassiopeia', 'ChoGath', 'Darius', 'Dr. Mundo', 'Fiora', 'Gangplank', 'Garen', 'Gnar', 'Gragas', 'Graves', 'Gwen', 'Heimerdinger', 'Illaoi', 'Irelia', 'Jax', 'Jayce', 'Kayle', 'Kennen', 'Kled', 'Malphite', 'Mordekaiser', 'Nasus', 'Ornn', 'Poppy', 'Quinn', 'Renekton', 'Riven', 'Ryze', 'Sett', 'Shaco', 'Shen', 'Singed', 'Sion', 'Sylas', 'Tahm Kench', 'Teemo', 'Trundle', 'Tryndamere', 'Urgot', 'Viktor', 'Vladimir', 'Warwick', 'Wukong', 'Yasuo', 'Yone', 'Yorick']  
    jungle = ["Amumu", "Brand", "Chogath", "Diana", "Dr. Mundo", "Ekko", "Elise", "Evelynn", "Fiddlesticks", "Gragas", "Graves", "Hecarim", "Ivern", "JarvenIV", "Jax", "Karthus", "Kayn", "Kha'Zix", "Kindred", "Kled", "Lee Sin", "Lillia", "Master Yi", "Nidalee", "Nocturne", "NUNU", "Olaf", "Ornn", "Poppy", "Rammu", "Reksai", "Rengar", "Sejuani", "Sett", "Shaco", "Shyvana", "Skarner", "Sylas", "Taliya", "Trundle", "Udyr", "Vi", "Viego", "Volibear", "Warwick", "Wukong", "Xin Zhao", "Zac"]
    mid = ["Aatrox", "Ahri", "Akali", "Akshan", "Anivia", "Annie", "Aurelion Sol", "Azir", "Brand", "Camile", "Cassiopeia", "Chogath", "Corki", "Ekko", "Fizz", "Galio", "Garen", "Heimerdinger", "Irelia", "Ivern", "Jayce", "Kassadin", "Katarina", "Leblanc", "Lillia", "Lissandra", "Lucian", "Lux", "Malphite", "Malzahar", "Neeko", "Nocturne", "Nunu", "Orianna", "Patheon", "Pyke", "Qiyana", "Renekton", "Rumble", "Ryze", "Swain", "Sylas", "Syndra", "Talon", "Twisted Fate", "Viegar", "VelKoz", "Viktor", "Vladimir", "Xerath", "Yasuo", "Zed", "Ziggs", "Zilean", "Zoe", "Trydamere"]
    adc = ["Akshan", "Aphelios", "Ashe", "Caitlyn", "Corki", "Draven", "Ezreal", "Jhin", "Jinx", "Kaisa", "Kalista", "KogMaw", "Lucian", "Miss Fortune", "Samira", "Senna", "Quinn", "Sivir", "Veigar", "Tristana", "Twitch", "Varus", "Vayne", "Xayah", "Yasuo", "Yone"]
    support = ["Alistar", "Bard", "Blitzcrank", "Brand", "Braum", "Galio", "Janna", "Karma", "Karthus", "Leona", "Lulu", "Lux", "Maokai", "Miss Fortune", "Morgana", "Nami", "Nautilus", "Pantheon", "Pyke", "Rakan", "Rell", "Senna", "Seraphine", "Shaco", "Sona", "Soraka", "Swain", "Taric", "Teemo", "Thresh", "Twitch", "VelKoz", "Vex", "Xerath", "Yuumi", "Zilean", "Zyra"]
    randselection = random.randint(0,len(locals()[name])-1)
    return locals()[name][randselection]

client.run(TOKEN)


