import discord
from discord.ext import commands

class help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="Help", color=discord.Color.blue())

        embed.set_thumbnail(url=f"{self.client.avatar_url}")
        embed.add_field(name="Help", value="`atw help` - Shows this message\n `atw rules` - Shows the discord server's rules\n `atw suggest` - Suggests stuff to the developers. Has a cooldown of 15 minutes.\n `atw github` - Shows github")

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(help(client))
