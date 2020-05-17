import discord
from discord.ext import commands, tasks
import random
import os


class MyHelpCommand(commands.MinimalHelpCommand):
#     async def send_cog_help(self, cog):
#         embed = discord.Embed(title='{0.qualified_name} Commands'.format(cog), colour=self.COLOUR)
#         if cog.description:
#             embed.description = cog.description
#
#         filtered = await self.filter_commands(cog.get_commands(), sort=True)
#         for command in filtered:
#             embed.add_field(name=self.get_command_signature(command), value=command.short_doc or '...', inline=False)
#
#         embed.set_footer(text=self.get_ending_note())
#         await self.get_destination().send(embed=embed)
#
#         await self.send_pages()
#     def get_opening_note(self):
#         return f"""
# ```diff
# + Your prefix: {self.clean_prefix}
# + Mandatory Fields: <> ||  Optional Fields: []
# - Do not include '<>' or '[]' when using commands.```
#         Type `{self.clean_prefix}{self.invoked_with} [CategoryName]` to view more category information.\n"""
    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            emby = discord.Embed(description=page)
            await destination.send(embed=emby)

# class MyHelpCommand(commands.MinimalHelpCommand):
#     def get_command_signature(self, command):
#         return '{0.clean_prefix}{1.qualified_name} {1.signature}'.format(self, command)

bot = commands.Bot(command_prefix=['sudo.', 'Sudo.'], case_insensetive=True, help_command=MyHelpCommand())




bot.load_extension('jishaku')
# bot.remove_command("help")
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f"cogs.{filename[:-3]}")





bot.run('NTg5MDc1MjE4NjA2MTk0Njk5.XsEULw.nmsvmBj_8JPiqWsWh40z8911gRA')
