import discord
import os
import random
from discord.ext import commands
from discord.utils import get

client = commands.Bot(command_prefix='atw ')
client.remove_command('help')

@client.event
async def on_ready():
    print("Ready!")
    await client.change_presence(activity=discord.Game(name='Plants vs Zombie\'s 2: It\'s About Time!'))

@client.event
async def on_member_join(member):
    role = get(member.server.roles, name="member")
    await client.add_roles(member, role)

@client.command()
async def rules(ctx):
    embed = discord.Embed(color=discord.Color.green())

    embed.add_field(name="Rules:", value="1: No spamming\n 2: Don't be toxic\n 3: Don't question the mods unless you think what they're doing is bad\n 4: Don't create unnecessary drama\n 5: Don't cry if your suggestion isn't added into the game\n 6: No gore or porn. Try to make the server as PG as possible\n 7: No loopholes\n 8: Have fun!")

    await ctx.send(embed=embed)

@client.command()
async def info(ctx):
    ctx.channel.purge(limit=1)

    embed = discord.Embed(title="Some info", color=discord.Color.green())

    embed.add_field(name="Server info:", value="This is a discord server for a fangame made by <@328186501475336204> , <@339319969873526794>, <@501082644168310816> , <@717624668009267241> , and more!")
    embed.add_field(name="Special Roles:", value="<@798162522036240447> : A role you can get by contributing to le github!!!\n <@798162582228959243> : A role you get by helping <@328186501475336204> with his therapy by just helping him with the bot! pleasedoitnowpleasedoitnowpleasedoitnowpleasedoitnow")

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
