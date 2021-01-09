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
    @commands.has_role("Developers")
    async def almanac(self, ctx, type, arg):
        if type == False:
            await ctx.send("You need to add the type!")
        
        if type != "plant" or "zombie":
            await ctx.send("That's not a type!")

        if arg == False:
            await ctx.send(f"You need to add the {type}")

        with open('almanac.json', 'w') as file:
            await ctx.send(file[type].arg)

def setup(client):
    client.add_cog(dev(client))