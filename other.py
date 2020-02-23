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
        """let the bot know it's a bad bot (don't recomend -it's tempermental)"""
        seed(1)
        index = randint(0, len(bot_reply.bad_replies) - 1)
        await ctx.send(bot_reply.bad_replies[index])



def setup(bot):
    bot.add_cog(Other(bot))
