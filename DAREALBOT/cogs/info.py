import discord
from discord.ext import commands
import time
import sys
import os


class Info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Displays the average webstock latency.")
    async def ping(self, ctx):

        lst=[]
        for i in range(3):
            lst.append(round(self.bot.latency*1000))


        embed=discord.Embed(title="PONG", color=0x14cfa0)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url_as(format="png"))
        embed.add_field(name=f"Average websocket latency", value=f":ping_pong: | `{lst[0]}ms`", inline=False)
        embed.set_footer()
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Info(bot))
