import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='$')


definitions = {
    'naturaleza': 'La naturaleza es el conjunto de todo lo que forma el universo y que no ha sido creado o modificado por el ser humano.',
    'agua': 'El agua es una sustancia líquida sin olor, color ni sabor que se encuentra en la naturaleza en diferentes estados y es esencial para la vida.',
    'oceanos': 'Los océanos son grandes extensiones de agua salada que cubren aproximadamente el 71% de la superficie de la Tierra.'
}

@bot.command(name='naturaleza')
async def naturaleza(ctx):
    await ctx.send(definitions['naturaleza'])

@bot.command(name='agua')
async def agua(ctx):
    await ctx.send(definitions['agua'])

@bot.command(name='oceanos')
async def oceanos(ctx):
    await ctx.send(definitions['oceanos'])

bot.run('MLQOBDUEWIO823HDAI267FEDS')
