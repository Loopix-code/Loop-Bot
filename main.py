import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random
import time





bot = commands.Bot(command_prefix="!", description = "Bot pour tout le monde!")



@bot.event
async def on_ready():
    print("__________________")
    print("Logged in as: ")
    print("__________________")  
    print(bot.user.name)
    #print(bot.user.id)
    print("__________________")
    print("Ready")
    print("__________________ \n")

#@bot.event
#async def on_message(message):
#    if message.author == bot.user:
#        return
#    await message.channel.send(f"> {message.content}\n{message.author}")
#    await bot.process_commands(message)

@bot.event
async def on_message_delete(message):
    await message.channel.send(f"Le message de {message.author} a été supprimé !\n > {message.content} ")

@bot.event
async def on_message_edit(after, before):
    await before.channel.send(f"{after.author} a édité le message de {before.author}:\n > Avant -> {after.content}\n > Après -> {before.content}")


@bot.event
async def on_member_join(member):
    channel = member.guild.get_channel(731095996427272223)
    await channel.send(f"Ho ! Mais que vois la je ? \nUn {member.mention} sauvage ! ")

@bot.event
async def on_member_remove(member):
    channel = member.guild.get_channel(729266169110069330)
    await channel.send(f"😥{member.mention} s'est caché dans les brousailles.\nA une prochaine fois !")
    
    

#_________________________________________________________________________
# 
  
@bot.command(brief="!clear <nombre de message>")
@commands.has_permissions(manage_messages = True)
async def clear(ctx, nombre : int):
	messages = await ctx.channel.history(limit = nombre + 1).flatten()
	for message in messages:
		await message.delete()
        


@bot.command()
@commands.has_permissions(manage_messages = True)
async def clearall(ctx):
	messages = await ctx.channel.history(limit = 1000).flatten()
	for message in messages:
		await message.delete()

#Commandes d'administration
#_______________________________________________________________________________________________________________
@bot.command()
@commands.has_permissions(ban_members = True)                   #  Il faut avoir la permission de ban 
async def ban(ctx, user : discord.User, *reason):
	reason = " ".join(reason)
	await ctx.guild.ban(user, reason = reason)
	await ctx.send(f"{user} à été ban pour la raison suivante : {reason}.")



@bot.command()
@commands.has_permissions(ban_members = True)
async def unban(ctx, user, *reason):
	reason = " ".join(reason)
	userName, userId = user.split("#")
	bannedUsers = await ctx.guild.bans()
	for i in bannedUsers:
		if i.user.name == userName and i.user.discriminator == userId:
			await ctx.guild.unban(i.user, reason = reason)
			await ctx.send(f"{user} à été unban.")
			return
	#Ici on sait que lutilisateur na pas ete trouvé
	await ctx.send(f"L'utilisateur {user} n'est pas dans la liste des bans")

@bot.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, user : discord.User, *reason):
	reason = " ".join(reason)
	await ctx.guild.kick(user, reason = reason)
	await ctx.send(f"{user} à été kick.")
    
    
    


#_______________________________________________________________________________________________________________


@bot.command()
async def commandes(ctx):
    await ctx.send("**Voici les commandes disponibles sur ce bot:**  \n \n -commandes                   *Affiche toutes les commandes du bot* \n -ping                                 *Renvoie un message: Pong* \n -Say                                  *Envoie un message via le bot* \n -chinese                          *Convertit votre texte en caractères Chinois* ")
    print ("Commande help effectué !")

@bot.command()
async def serverInfo(ctx):
	server = ctx.guild
	numberOfTextChannels = len(server.text_channels)
	numberOfVoiceChannels = len(server.voice_channels)
	serverDescription = server.description
	numberOfPerson = server.member_count
	serverName = server.name
	message = f"Le serveur **{serverName}** contient *{numberOfPerson}* personnes ! \nLa description du serveur est {serverDescription}. \nCe serveur possède **{numberOfTextChannels}** salons écrit et **{numberOfVoiceChannels}** salon vocaux."
	await ctx.send(message)




#Commande Ping
@bot.command()
async def ping(ctx):
    await ctx.send("Pong")
    print("Pong")



#Commande "Say"
@bot.command()
async def say (ctx, *texte):
    await ctx.send(" ".join(texte))
        
    



#Commande "chinese"
@bot.command()
async def chinese (ctx, *text):
    chineseChar = "丹书ㄈ力已下呂廾工丿片乚爪ㄇ口尸厶尺ㄎ丁凵人山父了乙"
    chineseText = []
    for world in text:
        for char in world:
            if char.isalpha():
                index = ord(char) - ord("a")
                transformed = chineseChar[index]
                chineseText.append(transformed)
            else:
                chineseText.append(char)
            chineseText.append(" ")
    await ctx.send("".join(chineseText))
    print ("Commande chinese effectué !")



@bot.command()
async def sayconsole(ctx, *texte):
    print(" ".join(texte))


@bot.command()
async def bold (ctx, *text):
    boldChar = "𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭"
    boldText = []
    for world in text:
        for char in world:
            if char.isalpha():
                index = ord(char) - ord("a")
                transformed = boldChar[index]
                boldText.append(transformed)
            else:
                boldText.append(char)
            boldText.append(" ")
    await ctx.send("".join(boldText))
    print ("Commande bold effectué !")


@bot.command()
@commands.has_permissions(administrator = True)
async def private(ctx):
    await ctx.send ("Le code du Bot : \n https://drive.google.com/drive/folders/1Wp_FFT5lUBbFPwIaHhjPN9Pamh691O1S?usp=sharing")


    











#async def clear(ctx, nombre : int):
     #messages = await ctx.channel.history(limit = nombre + 1).flatten()
	 #for message in messages:
		#await message.delete()


#https://www.youtube.com/watch?v=FCCnkQ-mFDE Partie 4 


#musique du turfu
#@bot.command()
#async def musique(ctx):
#input("quel musique ?")  # Il faut definir "input" et on peut pas faire        def input ("quel musique ?") 






    
    








bot.run("NzI4NjQxMzIxNTUxNjU5MTQ5.XwhOmA.2Uo5WqNrbSVOtVtf4lBxweOufok")
































