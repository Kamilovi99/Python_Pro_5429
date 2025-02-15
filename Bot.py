import discord
from discord.ext import commands
import random, os

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='$', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Iniciado como {bot.user} (ID: {bot.user.id})')
    print('------')


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
    meme = random.choice(os.listdir('M2L1/img'))
    with open(f'M2L1/img{meme}','rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
    
bot.run('Token')
