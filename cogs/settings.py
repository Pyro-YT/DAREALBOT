import discord
from discord.ext import commands
import time
import sys
import os
import darealmodule
import requests
import json
import aiohttp
import random

class Settings(commands.Cog):
    """Settings to allow for basic configuration & customizability."""

    def __init__(self, bot):
        self.bot = bot
        self.icon = "<:Settings:724611422926930022>"
        self.thumbnail = 'https://media.discordapp.net/attachments/714855923621036052/724610498569699348/maps-and-location.png?width=499&height=499'

    @commands.command(help='Hold')
    @commands.has_permissions(manage_roles=True)
    async def setprefix(self, ctx, prefix):
        """
        Hold
        """

        if len(prefix) > 12:
            embed=discord.Embed(title="The prefix is to long.", description=f'<:warningerrors:713782413381075536> The `<prefix>` aurgument can not be longer than 12 characters.', color=0x2f3136)
            embed.set_footer(icon_url=ctx.author.avatar_url_as(format="png"), text=darealmodule.Helping.get_footer(self, ctx))
            await ctx.send(embed=embed)
            return

        if len(prefix) <= 0:
            embed=discord.Embed(title="The prefix is short.", description=f'<:warningerrors:713782413381075536> The `<prefix>` aurgument can not be shorter than 1 character.', color=0x2f3136)
            embed.set_footer(icon_url=ctx.author.avatar_url_as(format="png"), text=darealmodule.Helping.get_footer(self, ctx))
            await ctx.send(embed=embed)
            return

def setup(bot):
    bot.add_cog(Settings(bot))
