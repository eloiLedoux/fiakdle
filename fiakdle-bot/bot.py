#Discord necessary imports
import discord
from discord.ext          import tasks
from discord.ext.commands import has_permissions, MissingPermissions

#Auxyliary imports
import json
import datetime
from random import randint
from random import choice

#Intern imports
import construire_info
import cropper
import traitement_reponse

#SO messages in str format
reponse_absence_channel = "Aucun channel n'a été assigné pour le jeu."
reponse_mauvais_channel = "Le jeu se déroule dans un autre channel."
reponse_set_channel_jeu = "Le jeu se déroule désormais dans ce channel !"
reponse_absence_droits  = "Vous ne disposez pas des droits d'administration nécessaires pour lancer cette commande."
reponse_absence_winners = "Aucun joueur n'a trouvé la réponse !"
reponse_erreur_inconnue = "Erreur inconnue."

# Opens the file in read-only mode and assigns the contents to the variable cfg to be accessed further down
with open('config.json', 'r') as cfg:
  # Deserialize the JSON data (essentially turning it into a Python dictionary object so we can use it in our code) 
  data = json.load(cfg) 
TOKEN      = data["token"]

#Attention, c'est l'heure anglaise donc -1h par rapport à la France
utc = datetime.timezone.utc 
HEURES_AIDE = [23, 11, 17, 22]
heure_reset = datetime.time(hour=22, minute=59, second=45, tzinfo=utc)

fiakjour_url = "../images/fiak-du-jour.jpg"
fiak         = construire_info.recuperer_etat()

# Fonction de mise à jour de l'aide en fonction de l'heure
def mise_a_jour_aide():
    now = datetime.datetime.now(tz=utc)
    for idx, heure in enumerate(HEURES_AIDE):
        if now.hour >= heure:
            fiak.setAide(idx)
            construire_info.sauvegarder_aide(idx)
            return 0
    fiak.setAide(0)  # Si aucune heure correspond

#Bot starting
bot = discord.Bot()

#COMMANDS

@bot.command(description="Défini le channel comme channel de jeu.")
@has_permissions(administrator=True)
async def channelid(ctx):
    nb_images = construire_info.nb_images_bdd()
    new_id    = randint(1, nb_images)
    construire_info.update_fiak(fiak, new_id)

    fiak.setChannelJeu(ctx.channel.id)
    fiak.clearWinner()

    mise_a_jour_aide()

    construire_info.sauvegarder_etat(fiak)

    await ctx.respond(reponse_set_channel_jeu)
    cropper.crop_image(fiak.getImgUrl(), fiakjour_url, fiak.getZoom())
    await ctx.respond(file=discord.File(fiakjour_url))

@bot.command(description="Affiche la liste des winners.")
async def winners(ctx):
    if fiak.hasWinner():
        liste_winners_str = '```Liste des gagnants :\n'
        for w in fiak.getWinners():
            user               = await bot.fetch_user(w)
            liste_winners_str += user.name + '\n'
        liste_winners_str     += str(len(fiak.getWinners())) + ' détraqué(e.s) et fier(e.s) de l\'être ! ```'
        await ctx.respond(liste_winners_str, ephemeral=True)
    else:
        await ctx.respond(reponse_absence_winners, ephemeral=True)

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
            manga_t      = traitement_reponse.mise_en_forme(manga)
            validPerso, validManga = fiak.guessFiak(personnage_t, manga_t)
                
            if user_id in fiak.getWinners():
                await ctx.respond(f"Vous avez déjà trouvé {fiak.getPerso()} de {fiak.getManga()} !", ephemeral=True)    
            elif validPerso and validManga:
                user = await bot.fetch_user(user_id)
                
                if user_id not in fiak.getWinners():
                    await channel.send(f"La réponse à été trouvée par {user.name} !")
                fiak.ajoutWinner(user_id)
                construire_info.sauvegarder_winners(fiak.getWinners())
                await ctx.respond(f"La réponse était bien {fiak.getPerso()} de {fiak.getManga()} !", ephemeral=True)
            elif validPerso and not validManga:
                await ctx.respond(f"C'est bien {fiak.getPerso()} mais pas le bon manga !")
            elif not validPerso and validManga:
                await ctx.respond(f"C'est bien {fiak.getManga()} mais pas le bon personnage !")
            else:
                await ctx.respond(f"Pas le bon personnage, pas le bon manga...")
        else:
            #await ctx.respond(reponse_mauvais_channel, ephemeral=True)
            await ctx.respond(f"Channel jeu : {fiak.getChannelJeu()}, channel actuel : {ctx.channel.id}", ephemeral=True)
    else:
        await ctx.respond(reponse_absence_channel, ephemeral=True)

#TASKS

# Envoi d'une aide pour l'heure donnée
async def envoi_aide(channel, index):
    fiak.setAide(index)
    construire_info.sauvegarder_aide(index)
    cropper.crop_image(fiak.getImgUrl(), fiakjour_url, fiak.getZoom())
    
    await channel.send(file=discord.File(fiakjour_url))

# Tâche unique qui envoie l'aide à des heures définies
@tasks.loop(time=[datetime.time(hour=h, tzinfo=utc) for h in HEURES_AIDE])
async def send_message_aide():
    if fiak.hasChannelJeu():
        channel  = bot.get_channel(fiak.getChannelJeu())
        now_hour = datetime.datetime.now(tz=utc).hour
        index    = HEURES_AIDE.index(now_hour) if now_hour in HEURES_AIDE else 0
        
        await envoi_aide(channel, index)

@tasks.loop(time=heure_reset)
async def set_reset():
    if fiak.hasChannelJeu():
        channel = bot.get_channel(fiak.getChannelJeu())
        if fiak.hasWinner():
            liste_winners_str = '```Liste des gagnants :\n'
            for w in fiak.getWinners():
                user               = await bot.fetch_user(w)
                liste_winners_str += user.name + '\n'
            liste_winners_str     += str(len(fiak.getWinners())) + ' détraqué(s) et fier(s) de l\'être ! ```'
            await channel.send(liste_winners_str)
        else:
            await channel.send(reponse_absence_winners)

        fiak.clearWinner()

        nb_images = construire_info.nb_images_bdd()
        new_id    = choice([i for i in range(0,nb_images) if not fiak.estDansBuffer(i)])
        fiak.ajoutBuffer(new_id)
        construire_info.update_fiak(fiak, new_id)
        construire_info.sauvegarder_etat(fiak)

#EXEC

mise_a_jour_aide()
send_message_aide.start()
set_reset.start()
fiak.setJeuEnCours(True)
bot.run(TOKEN)