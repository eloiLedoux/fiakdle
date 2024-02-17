import discord
from discord.ext import tasks
import json
import datetime

import construire_info
import cropper

# Opens the file in read-only mode and assigns the contents to the variable cfg to be accessed further down
with open('config.json', 'r') as cfg:
  # Deserialize the JSON data (essentially turning it into a Python dictionary object so we can use it in our code) 
  data = json.load(cfg) 

TOKEN = data["token"]

bot = discord.Bot()

fiakjour_url = "../images/fiak-du-jour.jpg"

fiak = construire_info.construire_fiak()

@bot.command(description="Répète un peu pour voir.")
async def print(ctx, print):
    await ctx.respond(print)

@bot.command(description="Défini le channel comme channel de jeu.")
async def channelid(ctx):
    fiak.setChannelJeu(ctx.channel.id)
    send_message.start() 
    await ctx.respond(f"Le jeu se déroule désormais dans ce channel {fiak.getChannelJeu()}!")

@bot.command(description="Affiche l'image à deviner.")
async def affiche(ctx):
    cropper.crop_image(fiak.getImgUrl(), fiakjour_url, fiak.getZoom())
    await ctx.respond(file=discord.File(fiakjour_url))

@bot.command(description="Réduit le niveau de difficulté de l'image.")
async def agmtaide(ctx):
    fiak.augmenterAide()
    await ctx.respond(f"Niveau d'aide augmenté à {fiak.getAide()}")


utc = datetime.timezone.utc #Attention, c'est l'heure anglaise donc -1h par rapport à la France
times = [
    datetime.time(hour=23, tzinfo=utc),
    datetime.time(hour=11, tzinfo=utc),
    datetime.time(hour=17, minute=30, tzinfo=utc),
    datetime.time(hour=22, tzinfo=utc)
]

@tasks.loop(time=times) #without quotation marks Reddit won't let me use the at sign without them
async def send_message():
    if fiak.hasChannelJeu():
        channel = bot.get_channel(fiak.getChannelJeu())
        fiak.augmenterAide()
        cropper.crop_image(fiak.getImgUrl(), fiakjour_url, fiak.getZoom())
        await channel.send(file=discord.File(fiakjour_url))


bot.run(TOKEN)