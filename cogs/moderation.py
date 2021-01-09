import discord
from discord.ext import commands

class moderation(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    @commands.has_role("Admin")
    async def purge(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount+1)
    
    @commands.command()
    @commands.has_role("Admin")
    async def ban(self, ctx, member: discord.Member, reason):
        await member.ban()
        embed = discord.Embed(color=discord.Color.red())

        embed.add_field(name=f"{member} has been banned by {ctx.author} for reason: ", value=f"{reason}")

        await ctx.send(embed=embed)
    
    @commands.command()
    @commands.has_role("Admin")
    async def kick(self, ctx, member: discord.Member, reason):
        await member.kick()
        embed = discord.Embed(color=discord.Color.red())

        embed.add_field(name=f"{member} has been kicked by {ctx.author} for reason: ", value=f"{reason}")

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(moderation(client))