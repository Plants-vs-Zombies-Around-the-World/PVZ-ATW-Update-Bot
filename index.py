import discord
import os
import random
from discord.ext import commands

client = commands.Bot(command_prefix='atw ')

@client.event
async def on_ready():
    print("Ready!")
    
@client.command(help="Gives server roles")
async def rules(ctx):
    embed = discord.Embed(color=discord.Color.green())

    embed.add_field(name="Rules:", value="1: No spamming\n 2: Don't be toxic\n 3: Don't question the mods unless you think what they're doing is bad\n 4: Don't create unnecessary drama\n 5: Don't cry if your suggestion isn't added into the game\n 6: No gore or porn. Try to make the server as PG as possible\n 7: No loopholes\n 8: Have fun!")

    await ctx.send(embed=embed)

@client.command()
async def suggest(ctx, suggest):
    embed = discord.Embed(color=discord.Color.green())

    embed.set_footer(text=f"code {random.randint(100000, 999999)}")
    embed.add_field(name=f"Suggestion by {ctx.author}", value=f"{suggest}")

    channel = client.get_channel(797446886667714570)

    await channel.send(embed=embed)

@client.command()
async def github(ctx):
    await ctx.send("https://github.com/dopaminw/PVZ-ATW-Github")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension((f'cogs.{filename[:-3]}'))

client.run("Nzk3NDQ4NzcyMjIwMDkyNDE3.X_moCw.o568meuapeQjsXEBq_Ja0MzxkkY")