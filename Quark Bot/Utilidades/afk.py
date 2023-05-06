import nextcord
import os
import json
from babel.dates import format_datetime
from nextcord.ext import commands
from nextcord import slash_command, SlashOption
from nextcord.ui import Button, View
from datetime import datetime 


class afk(commands.Cog):
    
    
    def __init__ (self, bot : commands.Bot):
        
        self.bot = bot
        
    
    @slash_command(name= 'afk', description= 'Activa el estado AFK y que no te molesten.')
    async def afk(self, interaction : nextcord.Interaction, razon : str = SlashOption(
        
        name= 'razón_del_afk',
        description= 'Razón de quedarse afk',
        required= False
        
        
    )):
        
        
        if razon in [None]:
            
            razon = 'No especifico una razón' 
            
        hora = datetime.now()    
            
        formato_hora = "EEEE dd 'de' MMM 'del' yyyy 'a las' h:mm a" 
        
        hora_afk = format_datetime(hora, formato_hora, locale= 'es')
            
        embed_afk = nextcord.Embed(
            
            title= '✅ | AFK',
            description= '''
            
`Usuario:` {}     

`Razón:` **{}**

`Tiempo:` **{}**      
            
            '''.format(interaction.user.mention, razon, hora_afk),
            color= nextcord.Colour.blue(),
            timestamp= datetime.now()
            
            
        )
        
        embed_afk.set_thumbnail(url = 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')
                    
        embed_afk.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')  
        
        
        if os.path.exists('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-afk/{}.json'.format(interaction.user.id)) != True:
            
            ruta = os.path.join('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-afk/', '{}.json'.format(interaction.user.id))
            
            with open(ruta, 'w') as write:
                
                dict_user = {
                    
                    'ID' : interaction.user.id
                    
                }
                
                json.dump(dict_user, write, indent= 4)
        
        return await interaction.response.send_message(embed= embed_afk)
        
        
        
def setup(bot: commands.Bot):
    bot.add_cog(afk(bot))               