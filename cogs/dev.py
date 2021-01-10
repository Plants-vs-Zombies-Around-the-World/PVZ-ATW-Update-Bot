import discord
import json
import random
from discord.ext import commands

class dev(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_role("Developers")
    async def add_plant(self, ctx, plant, description):
        if plant == False:
            await ctx.send("You need to add a plant!")

        if description == False:
            await ctx.send("You need to add a description!")

        def write(description, filename='almanac.json'):
            with open(filename, 'w') as f:
                json.dump(description, f, indent=4)
        
        with open('almanac.json') as file:
            data = json.load(file)
            temp = data["plants"]
            y = {plant: description}
            temp.append(y)
        
        write(data)

    @commands.command()
    @commands.has_role("Developers")
    async def add_zombie(self, ctx, zombie, description):
        if zombie == False:
            await ctx.send("You need to add a plant!")

        if description == False:
            await ctx.send("You need to add a description!")

        def write(description, filename='almanac.json'):
            with open(filename, 'w') as f:
                json.dump(description, f, indent=4)
        
        with open('almanac.json') as file:
            data = json.load(file)
            temp = data["zombies"]
            y = {zombie: description}
            temp.append(y)
        
        write(data)
    
    @commands.command()
    async def almanac_zomb(self, ctx, arg):
        with open('almanac.json', 'r') as file:
            data = json.load(file)

            await ctx.send(data["zombie"[arg]])
    
    @commands.command()
    async def almanac_plants(self, ctx, arg):
        embed = discord.Embed(color=discord.Color.green())

        with open('almanac.json', 'r') as file:
            data = json.load(file.read())

            embed.add_field(name=data["plants"[arg][0]], value=data["plants"[arg][1]])

def setup(client):
    client.add_cog(dev(client))
