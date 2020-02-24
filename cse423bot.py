import discord
from discord.ext import commands

import asyncio

import datetime

import bot_reply

description = "This is a bot to provide early alerts before planned meetings. Use the prefix '!' before any of the commands below."
bot = commands.Bot(command_prefix='!', description=description)

twelve_half = 45000

async def reminder():
        channel = bot.get_channel(#channel goes here)
        # if the next message is not muted, we send the alert
        # otherwise we unmute for the next message to be sent
        if(bot_reply.mute == False):
            await channel.send("Hey! We have a meeting in a half-hour!")
        else:
            bot_reply.mute = False

async def message_schedule():
    await bot.wait_until_ready()
    most_recent = 0;
    current = int(datetime.datetime.now().strftime("%s"))
    # finds the most relevant alert time in the event the bot has crashed and
    # needs to restart
    for i in range(0, len(bot_reply.meeting_times)):
        next_time = datetime.datetime.strptime(bot_reply.meeting_times[i], '%Y-%m-%d').timestamp()
        if (current <= (next_time + twelve_half)):
            most_recent = i;
            break;

    # runs while the bot is open
    while not bot.is_closed():
        current = int(datetime.datetime.now().strftime("%s"))
        next_time = datetime.datetime.strptime(bot_reply.meeting_times[most_recent], '%Y-%m-%d').timestamp()

        print("current = " + str(current))
        print("next_time + twelve_half = " + str(next_time + twelve_half))
        print("next_time + twelve_half - current = " + str(next_time + twelve_half - current))

        # will wait the amount of time until the next alert
        # next time + twelve_half is the next alert time releative to epoch
        # current is when the loop started relative to epoch
        # so (next_time + twelve_half) - current is the amount of time relative to start
        print(next_time + twelve_half - current)
        # sleep till the next
        await asyncio.sleep(next_time + twelve_half - current)

        # run the alert and move to the next date
        await reminder()
        most_recent += 1


def main():
        token = input("Enter token: ")
        bot.load_extension('alerts')
        bot.load_extension('other')
        bot.loop.create_task(message_schedule())
        bot.run(token)
if __name__ == '__main__':
    main()
