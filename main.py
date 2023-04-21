import asyncio
import discord
from discord.ext import commands
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='s', intents=intents)


@bot.command(name='et_timer')
async def my_randint(ctx, h, a, m, b):
    await ctx.send(f'The timer should start in {h} hours and {m} minutes')
    await asyncio.sleep(int(h) * 3600 + int(m) * 60)
    await ctx.send('Time X has come!')


TOKEN = "MTA4NjI1MDg4NjUyNDg1MDIwNg.GcfnF1.c6ncCWkzNr76YIyRbajNHoZBa0noInl5WSyOn4"

bot.run(TOKEN)
