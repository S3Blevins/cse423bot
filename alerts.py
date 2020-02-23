import discord
from discord.ext import commands

class Alerts(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def alert(ctx):
        """set your own alert (will go off 30-mins before): hh:mm_MM:DD"""


    @commands.command()
    async def info(self, ctx):
        """privides info on this bot"""

        help_string = ("Hello! I am the alert bot for our cse423 compilers discord "
        "server. The alarm will go off a half-hour before our "
        "scheduled meetings on Tuesday and Thursday. The goal is to "
        "allow for reminders for team meetings.")

        await ctx.send(help_string)

    @commands.command()
    async def suspend(ctx):
        """ignore next upcoming alert"""
        return "suspend"

    @commands.command()
    async def cancel(ctx):
        """cancel the alarm suspension"""
        return "cancel"


def setup(bot):
    bot.add_cog(Alerts(bot))
