import discord
from discord.ext import commands

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='escoge un prefix', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    print('Para ver la lista de comandos pon $ayuda')

@bot.command()
async def ayuda(ctx):
    await ctx.send('Estos son los comandos: $eco1, $eco2, $eco3')

@bot.command()
async def eco1(ctx):
    await ctx.send('Para clasificar la basura existen varias canecas de colores, y cada color indica que tipo de basura le pertenece.')
    with open('M2L2\media\Separarbasura.MP4', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def eco2(ctx):
    await ctx.send('Pasos para reciclar: 1.Separar los residuos en diferentes recipientes, 2.Limpiar los materiales a reciclar, 3.Secar los materiales, 4.Aplastar los envases, 5.Depositar los residuos en los contenedores correspondientes, 6.Indicar al recolector de basura cómo están clasificados los residuos')
    with open('M2L2\media\TresR.MP4', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def eco3(ctx):
    await ctx.send('Estos son los beneficios del reciclaje:')
    with open('M2L2\media\Reciclaje.png', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

bot.run('Coloca el token de tu bot')
