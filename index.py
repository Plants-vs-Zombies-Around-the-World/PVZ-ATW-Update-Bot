import discord
import os
import random
from discord.ext import commands
from discord.utils import get

client = commands.Bot(command_prefix='?')
client.remove_command('help')

intents = discord.Intents(members=True)

@client.event
async def on_ready():
    print("Ready!")
    await client.change_presence(activity=discord.Game(name='Plants vs Zombies 2: It\'s About Time!'))

@client.event
async def on_member_join(member):
    role = get(member.server.roles, name="Member")
    await client.add_roles(member, role)

@client.command()
@commands.cooldown(1, 900)
async def suggest(ctx, suggest):
    embed = discord.Embed(color=discord.Color.green())

    embed.set_footer(text=f"code {random.randint(100000, 999999)}")
    embed.add_field(name=f"Suggestion by {ctx.author}", value=f"{suggest}")

    channel = client.get_channel(797447065423708190)

    await channel.send(embed=embed)

@client.command()
@commands.has_role("Developers")
async def update(ctx, update_title, update_desc):
    embed = discord.Embed(title="New update!", color=discord.Color.green())

    embed.set_footer(text=f"update by {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.add_field(name=update_title, value=update_desc)

    channel = client.get_channel(797463887951167528)
    await channel.send(embed=embed)

@client.command()
async def github(ctx):
    await ctx.send("https://github.com/Plants-vs-Zombies-Around-the-World")

@client.command()
async def almanac(ctx):
    await ctx.send(file=discord.File(r'./lol/almanac.json'))

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension((f'cogs.{filename[:-3]}'))

client.run(lol)
