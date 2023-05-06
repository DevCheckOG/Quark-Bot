import nextcord
import os
import json
import re
from nextcord.ext import commands
from nextcord import PermissionOverwrite
from nextcord import slash_command, SlashOption
from nextcord.utils import get
from nextcord.ui import Button, View
from datetime import datetime


class blacklist(commands.Cog):
    
    def __init__ (self, bot : commands.Bot):
        
        self.bot = bot
        
    @slash_command(name= 'blacklist', description= 'Bloquea malas palabras/links en el servidor.')
    async def blacklist(self, interaction : nextcord.Interaction, canales_except : nextcord.TextChannel = SlashOption(
        
        name= 'canal_de_excepción',
        description= 'Canal que quieres que no se modere',
        required= False
        
    )):
        
        if interaction.user.guild_permissions.administrator in [True]:
            
    
            if canales_except == None:
                
                canal_except = canales_except = False
                
            else:
                
                canal_except = canales_except.id    
                
            
            class ModalBlacklist(nextcord.ui.Modal):
                
                def __init__ (self):
                    
                    super().__init__(
                        
                        title= '🤬 Blacklist'
                        
                    )
                    
                    self.links = nextcord.ui.TextInput(
                        
                        label= 'Links a bloquear',
                        min_length= 1,
                        max_length= 3000,
                        required= True,
                        placeholder= 'Escribe los links que desea bloquear, con espacios.',
                        style= nextcord.TextInputStyle.paragraph
                        
                    )
                    
                    self.add_item(self.links)
                    
                    
                    self.words = nextcord.ui.TextInput(
                        
                        label= 'Palabras a Bloquear',
                        min_length= 1,
                        max_length= 3000,
                        required= True,
                        placeholder= 'Escribe las palabras a bloquear, con espacios. '
                        
                    )
                    
                    self.add_item(self.words)
                    
                
                async def callback(self, interaction: nextcord.Interaction) -> None:
                    
                    links = re.findall(r'\b(?:www\.\w+\.\w+|\w+\.(?:com|net|tk))\b', self.links.value)
                    palabras = self.words.value.split()
                    
                    if os.path.exists('C:/Users/WIndows USER/Documents/Quark Bot/Eventos/data/{}.json'.format(interaction.guild_id)) in [True]:
                        
                        with open('C:/Users/WIndows USER/Documents/Quark Bot/Eventos/data/{}.json'.format(interaction.guild_id), 'w') as write:
                            
                            dict_a_guardar = {
                                
                                'LINKS' : links,
                                'PALABRAS' : palabras,
                                'CANALES' : canal_except
                                
                            }
                            
                            json.dump(dict_a_guardar, write, indent= 6)
                        
                        
                        embed_update_blacklist = nextcord.Embed(
                            
                            title= '✅ | Blacklist Update',
                            description= 'Se actualizo correctamente las palabras/links bloqueadas',
                            color= nextcord.Colour.yellow(),
                            timestamp= datetime.now()
                            
                        )   
                        
                        embed_update_blacklist.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024') 
                        
                        return await interaction.send(embed= embed_update_blacklist)
                    
                    else:
                        
                        ruta = os.path.join('C:/Users/WIndows USER/Documents/Quark Bot/Eventos/data/', '{}.json'.format(interaction.guild_id)) 
                        
                        with open(ruta, 'w') as write:
                            
                            dict_a_guardar = {
                                
                                'LINKS' : links,
                                'PALABRAS' : palabras,
                                'CANALES' : canal_except
                                
                            }
                            
                            json.dump(dict_a_guardar, write, indent= 6)
                        
                        
                        embed_create_blacklist = nextcord.Embed(
                            
                            title= '✅ | Blacklist Create',
                            description= 'Se guardo correctamente las palabras/links bloqueadas',
                            color= nextcord.Colour.blue(),
                            timestamp= datetime.now()
                            
                        )   
                        
                        embed_create_blacklist.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024') 
                        
                        return await interaction.send(embed= embed_create_blacklist)
                    
                    
                    
            modal = ModalBlacklist()
            
            return await interaction.response.send_modal(modal= modal)                
                            
        else: 
            
            embed_noperms = nextcord.Embed(
                
                title= '❌ | SIN PERMISOS',
                description= 'No tienes permisos suficientes para utilizar este comando.',
                color= nextcord.Colour.red(),
                timestamp= datetime.now()
                
            )    
            
                  
            embed_noperms.set_author(name= '{}'.format(self.bot.user), icon_url= self.bot.user.avatar)   
                
            embed_noperms.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')  
            
            
            button_noperms = Button(
                
                label= 'Soporte',
                emoji= '⚙️',
                style= nextcord.ButtonStyle.gray,
                url= 'https://discord.gg/Gs5FwKHTCW'
                
            )
            
            view = View()
            view.add_item(button_noperms)
            
            return await interaction.response.send_message(embed = embed_noperms, view= view)
        
        
        
        
def setup(bot : commands.Bot):
    
    bot.add_cog(blacklist(bot))                