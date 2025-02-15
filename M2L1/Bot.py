import discord
from discord.ext import commands
import random, os

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='Pon tu prefix', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Iniciado como {bot.user} (ID: {bot.user.id})')
    print('------')
    print('Para ver la lista de comandos pon $help')

@bot.command()
async def add(ctx, left: int, right: int):
    """Suma dos números."""
    await ctx.send(left + right)


@bot.command()
async def subtract(ctx, left: int, right: int):
    """Resta dos números."""
    await ctx.send(left - right)


@bot.command()
async def multiply(ctx, left: int, right: int):
    """Multiplica dos números."""
    await ctx.send(left * right)


@bot.command()
async def divide(ctx, left: int, right: int):
    """Multiplica dos números."""
    await ctx.send(left / right)

@bot.command()
async def roll(ctx, dice: str):
    """Tira un dado en formato NdN."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('¡El formato debe estar en NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Escoge entre varias opciones."""
    await ctx.send(random.choice(choices))


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repite una palabra un número de veces."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def joined(ctx, member: discord.Member):
    """Dice cuando un miembro se unió."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


@bot.command()
async def promo(ctx):
    """Muestra mi juego del HUB de Kodland."""
    await ctx.send('Prueba mi juego, Rouge-clickfood: https://hub.kodland.org/en/project/317776')


@bot.group()
async def cool(ctx):
    """Dice si un usuario es cool.

    En realidad esto solo revisa si un subcomando es usado.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} no es cool')


@cool.command(name='bot')
async def _bot(ctx):
    """¿Es el bot cool?"""
    await ctx.send('Si, el bot es cool.')


@bot.command()
async def meme(ctx):
    """Muestra unos momazos"""
    meme = random.choice(os.listdir('BDD/img'))
    with open(f'BDD/img/{meme}','rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)


@bot.command()
async def eco1(ctx):
    """Te dice como clasificar la basura."""
    await ctx.send('Para clasificar la basura existen varias canecas de colores, y cada color indica que tipo de basura le pertenece.')
    with open('BDD\media\Separarbasura.MP4', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def eco2(ctx):
    """Te dice como reciclar."""
    await ctx.send('Pasos para reciclar: 1.Separar los residuos en diferentes recipientes, 2.Limpiar los materiales a reciclar, 3.Secar los materiales, 4.Aplastar los envases, 5.Depositar los residuos en los contenedores correspondientes, 6.Indicar al recolector de basura cómo están clasificados los residuos')
    with open('BDD\media\TresR.MP4', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def eco3(ctx):
    """Te dice los beneficios del reciclaje."""
    await ctx.send('Estos son los beneficios del reciclaje:')
    with open('BDD\media\Reciclaje.png', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

bot.run('Pon el token de tu bot')
