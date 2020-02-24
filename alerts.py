import discord
from discord.ext import commands

import bot_reply

class Alerts(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def suspend(self, ctx):
        """ignore next upcoming alert"""

        if(bot_reply.mute == True):
            await ctx.send("The next alarm is already muted.")
        else:
            bot_reply.mute = True
            await ctx.send("The next alarm has been muted.")

    @commands.command()
    async def cancel(self, ctx):
        """cancel the alarm suspension"""

        if(bot_reply.mute == False):
            await ctx.send("The next alarm is not muted.")
        else:
            bot_reply.mute = False
            await ctx.send("The next alarm is no longer muted.")


def setup(bot):
    bot.add_cog(Alerts(bot))
