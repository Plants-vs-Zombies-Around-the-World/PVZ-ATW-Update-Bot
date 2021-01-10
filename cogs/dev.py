import discord
import json
import random
import os
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

        await ctx.send("Plant successfully added!")

    @commands.command()
    @commands.has_role("Developers")
    async def add_zombie(self, ctx, zombie, description):
        if zombie == False:
            await ctx.send("You need to add a zombie!")

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
        
        await ctx.send("Zombie succesfully added!")
    
    @commands.command()
    async def almanac_zomb(self, ctx, arg: int):

        with open('almanac.json', 'r') as file:
            data = json.load(file)

            await ctx.send(data["zombies"][arg])
    
    @commands.command()
    async def almanac_plants(self, ctx, arg: int):

        with open('almanac.json', 'r') as file:
            data = json.load(file)

            await ctx.send(data["plants"][arg])

    @commands.command()
    async def almanac_help(self, ctx):
        embed  = discord.Embed(color=discord.Colour.blurple())

        for file in os.listdir():
            if file == 'almanac.json':
                embed.add_field(file)
        
        embed.add_field(name="To get a plant or zombie, you have to use array lists", value="ex: sunflower = 0, so type `atw almanac_plants 0` to get sunflower, and so on and so forth. I know this sounds bad but I don't wanna fucking die of error finding, okay? I have still have a life!!!")

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(dev(client))
