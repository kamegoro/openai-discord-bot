import discord
import traceback
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix="/", intents=intents)


@bot.event
async def on_ready():
    print("ログインしました")


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = "".join(
        traceback.TracebackException.from_exception(orig_error).format()
    )
    await ctx.send(error_msg)


@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        if message.author.bot:
            return

        await message.channel.send(f"{message.author.mention} さん、何かご用ですか？")
    await bot.process_commands(message)


token = os.environ["DISCORD_TOKEN"]
bot.run(token)
