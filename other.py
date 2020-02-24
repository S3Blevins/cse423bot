import discord
from discord.ext import commands

import bot_reply

from random import seed
from random import randint

class Other(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def goodbot(self, ctx):
        """let the bot know it's a good bot"""
        seed(1)
        index = randint(0, len(bot_reply.good_replies) - 1)
        await ctx.send(bot_reply.good_replies[index])

    @commands.command()
    async def badbot(self, ctx):
        """let the bot know it's a bad bot (don't recomend -it can be tempermental and borderline abusive)"""
        seed(1)
        index = randint(0, len(bot_reply.bad_replies) - 1)
        await ctx.send(bot_reply.bad_replies[index])

    @commands.command()
    async def info(self, ctx):
        """privides info on this bot"""

        help_string = ("Hello! I am the alert bot for our cse423 compilers discord "
        "server. The alarm will go off a half-hour before our "
        "scheduled meetings on Tuesday and Thursday. The goal is to "
        "allow for reminders for team meetings.")

        await ctx.send(help_string)


def setup(bot):
    bot.add_cog(Other(bot))
