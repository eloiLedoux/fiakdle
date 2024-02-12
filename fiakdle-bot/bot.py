import discord
import json

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
channelJeu = None

@bot.command(description="Répète un peu pour voir.")
async def print(ctx, print):
    await ctx.respond(print)

@bot.command(description="Id du channel.")
async def channelid(ctx):
    channelJeu = ctx.channel.id
    await ctx.respond("Le jeu se déroule désormais dans ce channel !")

@bot.command(description="Affiche l'image à deviner.")
async def affiche(ctx):
    cropper.crop_image(fiak.getImgUrl(), fiakjour_url, fiak.getZoom())
    await ctx.respond(file=discord.File(fiakjour_url))

@bot.command(description="Réduit le niveau de difficulté de l'image.")
async def agmtaide(ctx):
    fiak.augmenterAide()
    await ctx.respond(f"Niveau d'aide augmenté à {fiak.getAide()}")

bot.run(TOKEN)