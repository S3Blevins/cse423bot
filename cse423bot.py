import discord
from discord.ext import commands

import asyncio
import sched, time

description = "This is a bot to provide early alerts before planned meetings. Use the prefix '!' before any of the commands below."

bot = commands.Bot(command_prefix='!', description=description)


async def alert_message():
    await bot.wait_until_ready()
    counter = 0
    channel = bot.get_channel()#channel
    while not bot.is_closed():
        counter += 1
        await channel.send("test")
        await asyncio.sleep(10)


def main():
        token = input("Enter token: ")
        bot.load_extension('alerts')
        bot.load_extension('other')
        bot.loop.create_task(alert_message())
        bot.run(token)
if __name__ == '__main__':
    main()
