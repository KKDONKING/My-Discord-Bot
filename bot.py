import discord
import datetime
import os
import sys
import commands.coin_flip as cf
from freddy import fnaf as fr

from dotenv import load_dotenv

from discord.ext import commands
sys.path.append('/v1.0/commands/coin_flip.py')
sys.path.append('/v1.0/commands/freddy.py')


load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

intents = discord.Intents.all()
discord.member = True

role_channel = 1132860437923381298  # role channel id goes here
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# ---------------------------------------EVENTS------------------------------------------


@bot.event
async def on_ready():
    print("Bot is online")


@bot.event
async def on_member_join(member):
    print(f"{member} joined")
    channel = member.guild.system_channel
    embed = discord.Embed(
        description=f'Welcome **{member.mention}** to the server',
        colour=discord.Colour.random(),
        timestamp=datetime.datetime.now(),

    )
    embed.add_field(
        name=f"You can get your role in <#{role_channel}>", value="")
    embed.set_thumbnail(url=f"{member.display_avatar}")
    await channel.send(embed=embed)


@bot.event
async def on_member_remove(member):
    print(f"{member} left")
    channel = member.guild.system_channel
    embed = discord.Embed(
        description=f'Rip **{member.mention}** Bozo',
        colour=discord.Colour.random(),
        timestamp=datetime.datetime.now(),
    )
    embed.add_field(name=f"You won't be missed", value="")
    embed.set_thumbnail(url=f"{member.display_avatar}")
    embed.set_image(
        url="https://media.tenor.com/OYp_uK4WcwkAAAAd/packwatch-ripbozo.gif")
    await channel.send(embed=embed)


# ---------------------------------------TASKS------------------------------------------
# utc = datetime.timezone.utc

# time = datetime.time(hour=8, minute=20, tzinfo=utc)
# @tasks.loop(time=time)
# async def my_task():
#     FNAF()
#     print("fnaf command invoked")


# @bot.event
# async def on_message(message):
#     print("essh command received")
#     if message.content == "I'm alive".lower():
#         embed = discord.Embed()
#         embed.set_image(
#             url="https://media.tenor.com/67LIumILNRsAAAAd/ltg-low-tier-god.gif")
#         await message.reply(embed=embed)
#     else:
#         return

# ---------------------------------------COMMANDS------------------------------------------

@bot.command()
async def coin_toss(ctx, member: discord.Member = None):
    print("coin_toss command invoked")
    if member is None:
        member = ctx.author
    coin_flipped, coin_sides = cf.coin_flip()
    coin_toss = discord.Embed(
        title=f"{member.name} flipped a coin",
        description=f'It\'s a **{coin_flipped}**',
        colour=discord.Colour.random(),
    )
    coin_toss.set_thumbnail(url=f"{coin_sides}")
    await ctx.send(embed=coin_toss)

#dice roll addition

@bot.command()
async def fnaf(ctx):

    fr()
    print("fnaf command invoked")
    await ctx.send(file=discord.File(f"./assets/images/fnaf.png"))

# class PersistentViewBot(commands.Bot):
#     def __init__(self):
#       intents - discord.Intents ().all()
#       super . __init__(command_prefix=commands.when_mentioned_or('.'),intents=intents)
#     async def setup_hook(self) -> None:
#       self.add_view(coin_toss())


# miscellaneous

# my_task()
# add the bot token inside the double quotes

bot.run(TOKEN)
