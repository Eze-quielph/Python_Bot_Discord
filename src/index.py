import json, os
from discord.ext import commands
import discord

def main():
    if os.path.exists('config.json'):
        with open('config.json') as f:
            config_data = json.load(f)
    
    else:
        template ={'prefix': '!', "token": ""}
        with open('config.json', 'w') as f:
            json.dump(template, f)

    prefix = config_data["prefix"]
    token = config_data["token"]
    intent = discord.Intents.all()

    bot = commands.Bot(command_prefix=prefix, intents=intent)

    bot.command(name="saludar", description="Saluda o te vas del server")
    async def saludar(ctx):
        await ctx.reply("Que la picas macaco")

    bot.run(token)

if __name__== '__main__':
    main()