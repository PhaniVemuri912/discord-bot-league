Top = ['Aatrox', 'Akali', 'Akshan', 'Camille', 'Cassiopeia', 'ChoGath', 'Darius', 'Dr. Mundo', 'Fiora', 'Gangplank', 'Garen', 'Gnar', 'Gragas', 'Graves', 'Gwen', 'Heimerdinger', 'Illaoi', 'Irelia', 'Jax', 'Jayce', 'Kayle', 'Kennen', 'Kled', 'Malphite', 'Mordekaiser', 'Nasus', 'Ornn', 'Poppy', 'Quinn', 'Renekton', 'Riven', 'Ryze', 'Sett', 'Shaco', 'Shen', 'Singed', 'Sion', 'Sylas', 'Tahm Kench', 'Teemo', 'Trundle', 'Tryndamere', 'Urgot', 'Viktor', 'Vladimir', 'Warwick', 'Wukong', 'Yasuo', 'Yone', 'Yorick']  
Jg = ["Amumu", "Brand", "Chogath", "Diana", "Dr. Mundo", "Ekko", "Elise", "Evelynn", "Fiddlesticks", "Gragas", "Graves", "Hecarim", "Ivern", "JarvenIV", "Jax", "Karthus", "Kayn", "Kha'Zix", "Kindred", "Kled", "Lee Sin", "Lillia", "Master Yi", "Nidalee", "Nocturne", "NUNU", "Olaf", "Ornn", "Poppy", "Rammu", "Reksai", "Rengar", "Sejuani", "Sett", "Shaco", "Shyvana", "Skarner", "Sylas", "Taliya", "Trundle", "Udyr", "Vi", "Viego", "Volibear", "Warwick", "Wukong", "Xin Zhao", "Zac"]
Mid = ["Aatrox", "Ahri", "Akali", "Akshan", "Anivia", "Annie", "Aurelion Sol", "Azir", "Brand", "Camile", "Cassiopeia", "Chogath", "Corki", "Ekko", "Fizz", "Galio", "Garen", "Heimerdinger", "Irelia", "Ivern", "Jayce", "Kassadin", "Katarina", "Leblanc", "Lillia", "Lissandra", "Lucian", "Lux", "Malphite", "Malzahar", "Neeko", "Nocturne", "Nunu", "Orianna", "Patheon", "Pyke", "Qiyana", "Renekton", "Rumble", "Ryze", "Swain", "Sylas", "Syndra", "Talon", "Twisted Fate", "Viegar", "VelKoz", "Viktor", "Vladimir", "Xerath", "Yasuo", "Zed", "Ziggs", "Zilean", "Zoe", "Trydamere"]
Adc = ["Akshan", "Aphelios", "Ashe", "Caitlyn", "Corki", "Draven", "Ezreal", "Jhin", "Jinx", "Kaisa", "Kalista", "KogMaw", "Lucian", "Miss Fortune", "Samira", "Senna", "Quinn", "Sivir", "Veigar", "Tristana", "Twitch", "Varus", "Vayne", "Xayah", "Yasuo", "Yone"]
Sp = ["Alistar", "Bard", "Blitzcrank", "Brand", "Braum", "Galio", "Janna", "Karma", "Karthus", "Leona", "Lulu", "Lux", "Maokai", "Miss Fortune", "Morgana", "Nami", "Nautilus", "Pantheon", "Pyke", "Rakan", "Rell", "Senna", "Seraphine", "Shaco", "Sona", "Soraka", "Swain", "Taric", "Teemo", "Thresh", "Twitch", "VelKoz", "Vex", "Xerath", "Yuumi", "Zilean", "Zyra"]
import random
bob = input()
if bob.lower() == "top":
    print(random.choice(Top))
else:
    breakpoint
if bob.lower() == "jg":
    print(random.choice(Jg))
else:
    breakpoint
if bob.lower() == "mid":
    print(random.choice(Mid))
else:
    breakpoint
if bob.lower() == "adc":
    print(random.choice(Adc))
else:
    breakpoint
if bob.lower() == "sp":
    print(random.choice(Sp))
else:
    breakpoint
    print("pls use *(lane) ")
