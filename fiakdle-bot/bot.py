import discord
from discord.ext import tasks
from discord.ext.commands import has_permissions, MissingPermissions

import json
import datetime

import construire_info
import cropper
import traitement_reponse

DEFAULT_ID = 1

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
fiak = construire_info.construire_fiak(DEFAULT_ID)

reponse_absence_channel = "Aucun channel n'a été assigné pour le jeu."
reponse_mauvais_channel = "Le jeu se déroule dans un autre channel."
reponse_set_channel_jeu = "Le jeu se déroule désormais dans ce channel !"
reponse_absence_droits = "Vous ne disposez pas des droits d'administration nécessaires pour lancer cette commande."
reponse_erreur_inconnue = "Erreur inconnue."

winners_id = []

@bot.command(description="Répète un peu pour voir.")
async def print(ctx, print):
    await ctx.respond(print)

@bot.command(description="Défini le channel comme channel de jeu.")
@has_permissions(administrator=True)
async def channelid(ctx):
    fiak.setChannelJeu(ctx.channel.id)
    winners_id.clear()

    now = datetime.datetime.now(tz=utc)
    premiere_heure = now.replace(hour=premiere_heure_int)
    deuxieme_heure = now.replace(hour=deuxieme_heure_int)
    troisieme_heure = now.replace(hour=troisieme_heure_int)
    quatrieme_heure = now.replace(hour=quatrieme_heure_int)
    if now >= premiere_heure:
        fiak.setAide(0) #Suppérieur à 23h (ce qui ne sera plus le cas à minuit)
    elif now >= quatrieme_heure:
        fiak.setAide(3) #Suppérieur à 22h
    elif now >= troisieme_heure:
        fiak.setAide(2) #Suppérieur à 17h
    elif now >= deuxieme_heure:
        fiak.setAide(1) #Suppérieur à 11h
    else:
        fiak.setAide(0) #Après minuit, inférieur à 23h mais 0 quand même car inférieur à 11h

    if not fiak.getJeuEnCours():
        send_message.start()
        set_reset.start()
        fiak.setJeuEnCours(True)
    await ctx.respond(reponse_set_channel_jeu)

@channelid.error
async def channelid_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.respond(reponse_absence_droits, ephemeral=True)
    else:
        await ctx.respond(reponse_erreur_inconnue, ephemeral=True)

@bot.command(description="Affiche l'image à deviner.")
async def affiche(ctx):
    cropper.crop_image(fiak.getImgUrl(), fiakjour_url, fiak.getZoom())
    await ctx.respond(file=discord.File(fiakjour_url), ephemeral=True)

@bot.command(description="Propose une réponse au fiak du jour.")
async def reponse(ctx, personnage, manga):
    if fiak.hasChannelJeu():
        if ctx.channel.id == fiak.getChannelJeu():
            channel = bot.get_channel(fiak.getChannelJeu())
            user_id = ctx.author.id

            personnage_t = traitement_reponse.mise_en_forme(personnage)
            manga_t = traitement_reponse.mise_en_forme(manga)
            validPerso, validManga = fiak.guessFiak(personnage_t, manga_t)
                
            if user_id in winners_id:
                await ctx.respond(f"Vous avez déjà trouvé {fiak.getPerso()} de {fiak.getManga()} !", ephemeral=True)    
            elif validPerso and validManga:
                user = await bot.fetch_user(user_id)
                
                if user_id not in winners_id:
                    await channel.send(f"La réponse à été trouvée par {user.name} !")
                winners_id.append(user_id) 
                await ctx.respond(f"La réponse était bien {fiak.getPerso()} de {fiak.getManga()} !", ephemeral=True)
            elif validPerso and not validManga:
                await ctx.respond(f"C'est bien {fiak.getPerso()} mais pas le bon manga !")
            elif not validPerso and validManga:
                await ctx.respond(f"C'est bien {fiak.getManga()} mais pas le bon personnage !")
            else:
                await ctx.respond(f"Pas le bon personnage, pas le bon manga...")
        else:
            await ctx.respond(reponse_mauvais_channel, ephemeral=True)
    else:
        await ctx.respond(reponse_absence_channel, ephemeral=True)

times = [
    heure_premiere_aide,
    heure_deuxieme_aide,
    heure_troisieme_aide,
    heure_quatrieme_aide
]

@tasks.loop(time=times)
async def send_message():
    if fiak.hasChannelJeu():
        channel = bot.get_channel(fiak.getChannelJeu())
        fiak.augmenterAide()
        cropper.crop_image(fiak.getImgUrl(), fiakjour_url, fiak.getZoom())
        await channel.send(file=discord.File(fiakjour_url))

@tasks.loop(time=heure_premiere_aide)
async def set_reset():
    winners_id.clear()

bot.run(TOKEN)