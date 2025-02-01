import discord
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='$', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


@bot.command()
async def promo(ctx):
    """Shows my Kodland HUB game link."""
    await ctx.send('Prueba mi juego, Rouge-clickfood: https://hub.kodland.org/en/project/317776')


@bot.command()
async def sing(ctx):
    """Sing My little pony:friendship is magic intro."""
    await ctx.send('My litte pony, My little pony, ah ahh ahhh ahhhh, (My little pony), me preguntaba que era la amistad, (My little pony), hasta que su magía me quesieron dar, aventuras, diversión, es fuerte y fiel, de gran corazón, ser amable es la solución, la magía lo hace aún mejor porque es My little pony, y por siempre habrá una gran amistadddd, My little pony: La magía de la amistad')


@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')


@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')

bot.run('MTMzMjc5ODI0MjExMDU3NDYxMg.G6Jx2u.y-aEVoQJAOpVeyQYUSkRZ66r84UJbeTzXyXHUk')