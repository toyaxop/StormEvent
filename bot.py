import discord
from mcstatus import JavaServer
from time import sleep
from datetime import datetime


default_intents = discord.Intents.default()
default_intents.members = True
client = discord.Client(intents=default_intents)
status_channel = 1028241547222859836
refresh_time = 300

@client.event
async def on_ready():
    print("Logged as {0.user}".format(client))
    serverproxy = JavaServer.lookup("mc.storm-event.fr:25565")
    serverlobby = JavaServer.lookup("mc.storm-event.fr:25566")
    serversurvie = JavaServer.lookup("mc.storm-event.fr:25567")
    serverevent = JavaServer.lookup("mc.storm-event.fr:25568")
    while True:
        try: #proxy
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            status = serverproxy.status()
            await client.get_channel(status_channel).send(f"Serveurs minecraft : ```[{current_time}] \n Etat proxy : allumé 🟩```")       
        except:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            await client.get_channel(status_channel).send(f"```[{current_time}] \n Etat proxy : OFF 🟥```")        
        try: #lobby
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            status = serverlobby.status()
            await client.get_channel(status_channel).send(f"```[{current_time}] \n Etat Serveur Lobby : allumé 🟩\n {status.players.online} joueurs connecté(e)s```")         
        except:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            await client.get_channel(status_channel).send(f"```[{current_time}] \n Etat Serveur Lobby : OFF 🟥```")        
        try: #survie
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            status = serversurvie.status()
            await client.get_channel(status_channel).send(f"```[{current_time}] \n Etat Serveur Survie : allumé 🟩\n {status.players.online} joueurs connecté(e)s```")     
        except:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            await client.get_channel(status_channel).send(f"```[{current_time}] \n Etat Serveur Survie : OFF 🟥```")
        try: #event
            now = datetime.now()
            status = serverevent.status()
            await client.get_channel(status_channel).send(f"```[{current_time}] \n Etat Serveur Event : allumé 🟩\n {status.players.online} joueurs connecté(e)s\n Refresh des msg toutes les {refresh_time} Secondes \n Bot développé par Toya.Xo#2088 ```")
            sleep(refresh_time)
        except:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            await client.get_channel(status_channel).send(f"```[{current_time}] \n Etat Serveur Event : OFF 🟥 \n Refresh toutes les {refresh_time / 60} Minutes \n Bot développé par Toya.Xo#2088 ```")
            sleep(refresh_time)

client.run(<TOKEN>)
