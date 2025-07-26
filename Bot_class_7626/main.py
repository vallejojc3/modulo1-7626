import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True  

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()#comando nuevo de la tarea
async def joined(ctx, member: discord.Member):
    """Dice cuándo se unió un miembro al servidor."""
    if member.joined_at:
        await ctx.send(f'{member.name} se unió el {discord.utils.format_dt(member.joined_at, style="F")}')
    else:
        await ctx.send(f'No pude obtener la fecha en que {member.name} se unió.')




bot.run("TOKEN")