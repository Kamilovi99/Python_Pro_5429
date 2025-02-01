import discord
import random
#The intents variable stores the bot's priviliges
intents = discord.Intents.default()
#Enabling the message-reading privelege
intents.message_content = True
#pipCreating a bot in the client variable and transferring it the priveleges
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("¡Hola!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$smash'):
        await message.channel.send("Los personajes que más uso en Super smash bros son Lucario y Robin")
    elif message.content.startswith('$spoiler'):
        await message.channel.send("Metal Sonic y Amy Rose son los personajes de la escena post-creditos de Sonic 3 La película")
    elif message.content.startswith('$contexto'):
        await message.channel.send("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    elif message.content.startswith("$HUB"):
        await message.channel.send("Prueba mi juego, Rouge-clickfood: https://hub.kodland.org/en/project/317776")
    elif message.content.startswith("$emoji"):
        def gen_emodji():
            emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
            return random.choice(emodji)
        await message.channel.send(gen_emodji())
    elif message.content.startswith("$pkmn"):
        await message.channel.send("Mi pokémon favorito es Typhlosion")
    elif message.content.startswith("$coin"):
        def flip_coin():
            flip = random.randint(0, 2)
            if flip == 0:
                return "Cara"
            else:
                return "Cruz"
        await message.channel.send(flip_coin())
    elif message.content.startswith("$amistad"):
        await message.channel.send("Mi código de amigo de Nintendo Switch:SW-6451-6068-0523")
    elif message.content.startswith("$dice"):
        def roll_dice():
            roll = random.randint(1, 6)
            if roll == 1:
                return "Sale 1"
            elif roll == 2:
                return "Sale 2"
            elif roll == 3:
                return "Sale 3"
            elif roll == 4:
                return "Sale 4"
            elif roll == 5:
                return "Sale 5"
            elif roll == 6:
                return "Sale 6"
        await message.channel.send(roll_dice())    
    elif message.content.startswith("$help"):
        await message.channel.send("Estos son todos los comandos que uso, $hello, $bye, $smash, $spoiler, $contexto, $HUB, $emoji, $pkmn, $coin, $amistad, $dice y $help")

client.run("MTMzMjc5ODI0MjExMDU3NDYxMg.G6Jx2u.y-aEVoQJAOpVeyQYUSkRZ66r84UJbeTzXyXHUk")