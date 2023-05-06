import nextcord
from nextcord.ext import commands
import json

with open("index.json", "r") as config:
    
    data = json.load(config)
    
    token = data['token']


intentos = nextcord.Intents()

intentos.dm_messages = True
intentos.members = True
intentos.guild_messages = True
intentos.guilds = True
intentos.message_content = True

bot = commands.Bot(
    
    intents = intentos,
    activity= nextcord.Activity(type=nextcord.ActivityType.playing, name ="/ayuda v1.00 | Arqui#9588"),
    status= nextcord.Status.online
    
)

comandos = [
    
    "General.invitame",
    "General.send",
    "General.calc",
    "General.ayuda",
    "General.ping",
    "Utilidades.create-embed",
    "Utilidades.blacklist",
    "Utilidades.nuke",
    "Utilidades.ban",
    "Utilidades.unban",
    "Utilidades.autorole",
    "Utilidades.kick",
    "Utilidades.antibot",
    "Utilidades.poll",
    "Utilidades.avatar",
    "Utilidades.purge",
    "Utilidades.nick",
    "Utilidades.create-dm",
    "Utilidades.welcomes",
    "Utilidades.arqui",
    "Utilidades.server",
    "Utilidades.verify",
    "Utilidades.code",
    "Utilidades.user",
    "Utilidades.afk",
    "Eventos.on_guild_remove",
    "Eventos.on_guild_join",
    "Eventos.on_message",
    "Eventos.on_member_join"
    
]


print('Lista de comandos cargados {}'.format(comandos))


if __name__ == '__main__':
    
    for comando in comandos:
        
        try:
            
            bot.load_extension(comando)
            print('Se cargo correctamente el comando: {}'.format(comando))
            
        except Exception as e:
            
            print(f"Cargo incorrectamente el comando: {comando}")
            
                        
          
@bot.event
async def on_ready():
    
    await bot.sync_application_commands()
    
    print('Se inicio el bot: {}'.format(bot.user))
    
    print('Versión de nextcord: {}'.format(nextcord.__version__))
    

bot.run(token)
