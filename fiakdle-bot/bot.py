import discord
from discord.ext import tasks
import json
import datetime

import construire_info
import cropper
import traitement_reponse


utc = datetime.timezone.utc #Attention, c'est l'heure anglaise donc -1h par rapport à la France
premiere_heure_int = 23
deuxieme_heure_int = 11
troisieme_heure_int = 17
quatrieme_heure_int = 22
heure_premiere_aide = datetime.time(hour=premiere_heure_int, tzinfo=utc)
heure_deuxieme_aide = datetime.time(hour=deuxieme_heure_int, tzinfo=utc)
heure_troisieme_aide = datetime.time(hour=troisieme_heure_int, tzinfo=utc)
heure_quatrieme_aide = datetime.time(hour=quatrieme_heure_int, tzinfo=utc)


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
    now = datetime.datetime.now(tz=utc)
    premiere_heure = now.replace(hour=premiere_heure_int)
    deuxieme_heure = now.replace(hour=deuxieme_heure_int)
    troisieme_heure = now.replace(hour=troisieme_heure_int)
    quatrieme_heure = now.replace(hour=quatrieme_heure_int)
    if now >= quatrieme_heure:
        fiak.setAide(3)
    elif now >= troisieme_heure:
        fiak.setAide(2)
    elif now >= deuxieme_heure:
        fiak.setAide(1)
    else:
        fiak.setAide(0)

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

@bot.command(description="Réduit le niveau de difficulté de l'image.")
async def reponse(ctx, personnage, manga):
    personnage_t = traitement_reponse.mise_en_forme(personnage)
    manga_t = traitement_reponse.mise_en_forme(manga)
    validPerso, validManga = fiak.guessFiak(personnage_t, manga_t)
    if validPerso and validManga:
        await ctx.respond(f"Réponse trouvée !")
    elif validPerso and not validManga:
        await ctx.respond(f"C'est bien {fiak.getPerso()} mais pas le bon manga !")
    elif not validPerso and validManga:
        await ctx.respond(f"C'est bien {fiak.getManga()} mais pas le bon personnage !")
    else:
        await ctx.respond(f"Pas le bon personnage, pas le bon manga...")


times = [
    heure_premiere_aide,
    heure_deuxieme_aide,
    heure_troisieme_aide,
    heure_quatrieme_aide
]

@tasks.loop(time=times) #without quotation marks Reddit won't let me use the at sign without them
async def send_message():
    if fiak.hasChannelJeu():
        channel = bot.get_channel(fiak.getChannelJeu())
        fiak.augmenterAide()
        cropper.crop_image(fiak.getImgUrl(), fiakjour_url, fiak.getZoom())
        await channel.send(file=discord.File(fiakjour_url))

bot.run(TOKEN)